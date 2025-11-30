import sqlite3

conn = sqlite3.connect('inventory.db')
cursor = conn.cursor()

cursor.execute('''
    SELECT p.name, c.name 
    FROM products p 
    JOIN categories c ON p.category_id = c.id 
    LIMIT 5
''')

results = cursor.fetchall()
for row in results:
    print(f"{row[0]} | {row[1]}")

conn.close()