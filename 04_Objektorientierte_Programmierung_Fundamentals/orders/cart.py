# This list holds the products currently in the cart
cart_items = []

def get_cart_items():
    """Returns the current list of items in the cart."""
    return cart_items

def add_to_cart(product):
    """Adds a product (dictionary) to the cart."""
    cart_items.append(product)

def remove_from_cart(product_id):
    """Removes an item from the cart based on its ID."""
    global cart_items
    cart_items = [item for item in cart_items if item['id'] != product_id]

def clear_cart():
    """Empties the cart completely."""
    global cart_items
    cart_items = []
