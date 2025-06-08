import os
import json
from database.user_db import save_user, load_users
from database.orders_db import save_order, get_all_orders

def test_full_order_flow():
    # --- STEP 1: Register a new user ---
    test_user = {
        "name": "Flow Tester",
        "email": "flow@test.com",
        "phone": "111222333",
        "address": "Flow Street 123",
        "postcode": "1010",
        "locality": "Flowville",
        "password": "test123"
    }
    save_user(test_user)
    users = load_users()
    matching_users = [u for u in users if u["email"] == test_user["email"]]
    assert len(matching_users) == 1
    customer_id = users.index(matching_users[0]) + 1  # Simulated ID

    # --- STEP 2: Simulate a cart with products ---
    items = [
        {"id": 1, "name": "Piano Class", "price": 30.0},
        {"id": 2, "name": "Guitar Lesson", "price": 45.0}
    ]
    delivery_method = "Standard"
    total_price = sum(item["price"] for item in items)

    # --- STEP 3: Save the order ---
    save_order(customer_id, items, delivery_method, total_price)

    # --- STEP 4: Verify the order is in orders.json ---
    orders = get_all_orders()
    matching_orders = [
        o for o in orders
        if o["customer_id"] == customer_id and o["total_price"] == total_price
    ]
    assert len(matching_orders) > 0

    print("✅ test_full_order_flow passed.")

if __name__ == "__main__":
    test_full_order_flow()
