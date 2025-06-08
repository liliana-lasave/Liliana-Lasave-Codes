# Shared cart list
CART = []

def add_to_cart(product):
    """Add a product to the cart."""
    CART.append(product)

def remove_from_cart(index):
    """Remove a product from the cart by its index."""
    if 0 <= index < len(CART):
        del CART[index]

def clear_cart():
    """Clear all products from the cart."""
    CART.clear()

def get_cart_items():
    """Return a copy of the current cart contents."""
    return CART.copy()
