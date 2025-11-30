# Deployment Instructions

## Prerequisites
- Ubuntu/Debian WSL or Linux VM
- Python 3.8+
- Nginx
- Git

## Quick Setup

1. **Environment Setup:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. **Database Migration:**
```bash
python migrate.py
```

3. **Test API locally:**
```bash
python app.py
# Test: curl http://localhost:8000/api/products
```

4. **Nginx Configuration:**
```bash
sudo cp nginx.conf /etc/nginx/sites-available/inventory-api
sudo ln -sf /etc/nginx/sites-available/inventory-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

5. **Systemd Service:**
```bash
# Update paths in inventory-api.service first
sudo cp inventory-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable inventory-api
sudo systemctl start inventory-api
```

6. **Public Access (ngrok):**
```bash
# Install ngrok first
ngrok http 80
```

## Testing Commands

**Database verification:**
```bash
sqlite3 inventory.db "SELECT p.name, c.name FROM products p JOIN categories c ON p.category_id = c.id LIMIT 5;"
```

**API testing:**
```bash
curl http://localhost/api/products
curl -X POST http://localhost/api/order -H "Content-Type: application/json" -d '{"product_id": 101, "quantity": 2}'
```

**Service status:**
```bash
sudo systemctl status inventory-api
```