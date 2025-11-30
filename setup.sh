#!/bin/bash

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migration
python migrate.py

# Copy nginx config (requires sudo)
sudo cp nginx.conf /etc/nginx/sites-available/inventory-api
sudo ln -sf /etc/nginx/sites-available/inventory-api /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx

# Setup systemd service (update paths in service file first)
sudo cp inventory-api.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable inventory-api
sudo systemctl start inventory-api

echo "Setup completed! Check service status with: sudo systemctl status inventory-api"