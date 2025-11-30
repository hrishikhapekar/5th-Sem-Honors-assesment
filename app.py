from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3
from lib import calculate_price

app = FastAPI()

class OrderRequest(BaseModel):
    product_id: int
    quantity: int

def get_db_connection():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/api/products")
def get_products():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT p.id, p.name, p.price, p.stock, c.name as category_name
        FROM products p
        JOIN categories c ON p.category_id = c.id
    ''')
    products = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return products

@app.post("/api/order")
def create_order(order: OrderRequest):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Get product details
    cursor.execute('SELECT * FROM products WHERE id = ?', (order.product_id,))
    product = cursor.fetchone()
    
    if not product:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product['stock'] < order.quantity:
        conn.close()
        raise HTTPException(status_code=400, detail="Insufficient stock")
    
    # Calculate price using legacy library
    total_price = calculate_price(order.product_id, order.quantity, product['price'])
    
    # Update stock
    new_stock = product['stock'] - order.quantity
    cursor.execute('UPDATE products SET stock = ? WHERE id = ?', (new_stock, order.product_id))
    conn.commit()
    conn.close()
    
    return {"total_price": total_price, "remaining_stock": new_stock}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)