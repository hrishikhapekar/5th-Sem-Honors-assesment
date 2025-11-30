# Legacy pricing logic library
# This module contains critical business logic for pricing calculations

def calculate_price(product_id, quantity, unit_price):
    """
    Calculate the total price for a product order.
    
    Args:
        product_id: The ID of the product
        quantity: The quantity ordered
        unit_price: The unit price of the product
    
    Returns:
        float: The total price
    """
    return quantity * unit_price
