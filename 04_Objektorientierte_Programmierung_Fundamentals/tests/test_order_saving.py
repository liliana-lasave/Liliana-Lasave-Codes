import os
import json
from database.orders_db import save_order, get_all_orders

# Path to the orders file
ORDERS_FILE = "database/orders.json"

def test_order_is_saved_correctly():
    """
    Test to verify that a new order is saved correctly into the orders file.
    """

    # Test order details
    customer_id = 1
    items = [
        {"name": "Guitar Lesson", "price": 30.0},
        {"name": "Singing Workshop", "price": 45.0}
    ]
    delivery_method = "Email"
    total_price = 75.0

    # Make sure the orders file exists and load current orders
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as f:
            existing_orders = json.load(f)
    else:
        existing_orders = []

    # Save the test order
    save_order(customer_id, items, delivery_method, total_price)

    # Retrieve all orders again
    updated_orders = get_all_orders()

    # Check that a new order has been added
    assert len(updated_orders) == len(existing_orders) + 1

    # Get the last order added
    last_order = updated_orders[-1]

    # Assert that all fields match what was saved
    assert last_order["customer_id"] == customer_id
    assert last_order["items"] == items
    assert last_order["delivery_method"] == delivery_method
    assert last_order["total_price"] == total_price

    print("test_order_is_saved_correctly passed.")

if __name__ == "__main__":
    test_order_is_saved_correctly()
