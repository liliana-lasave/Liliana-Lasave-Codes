import os
import json

# Path to the orders storage file
ORDERS_FILE = "data/orders.json"

def save_order(customer_id, items, delivery_method, total_price):
    """
    Save a new order to the orders.json file.

    Parameters:
    - customer_id (int): ID of the customer placing the order
    - items (list): List of products included in the order
    - delivery_method (str): Delivery option selected by the customer
    - total_price (float): Total price of the order
    """
    order = {
        "customer_id": customer_id,
        "items": items,
        "delivery_method": delivery_method,
        "total_price": total_price
    }

    # Load existing orders if the file exists
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as f:
            orders = json.load(f)
    else:
        orders = []

    # Append the new order
    orders.append(order)

    # Ensure the directory exists before saving
    os.makedirs(os.path.dirname(ORDERS_FILE), exist_ok=True)

    # Save all orders back to the file
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)

def get_all_orders():
    """
    Retrieve all saved orders from the orders.json file.

    Returns:
    - list: A list of all previously saved orders
    """
    # Return an empty list if the file does not exist
    if not os.path.exists(ORDERS_FILE):
        return []

    # Load and return the orders from the file
    with open(ORDERS_FILE, "r") as f:
        return json.load(f)
