import os
import json
from database import user_db

# Override the path for test purpose
TEST_DATABASE_DIR = "tests/data"
TEST_CUSTOMERS_FILE = os.path.join(TEST_DATABASE_DIR, "customers_test.json")

# Override the constants in user_db module
user_db.DATABASE_DIR = TEST_DATABASE_DIR
user_db.CUSTOMERS_FILE = TEST_CUSTOMERS_FILE

def test_user_registration():
    # Ensure the test directory exists
    os.makedirs(TEST_DATABASE_DIR, exist_ok=True)

    # Clear the test file before running the test
    if os.path.exists(TEST_CUSTOMERS_FILE):
        os.remove(TEST_CUSTOMERS_FILE)

    # Define a test user
    test_user = {
        "name": "Test User",
        "address": "123 Test Street",
        "postcode": "12345",
        "locality": "Testville",
        "email": "test@example.com",
        "phone": "123456789",
        "password": "testpass"
    }

    # Save the test user
    user_db.save_user(test_user)

    # Load users from the test file
    users = user_db.load_users()

    # Check that the test user is in the list
    matching_users = [user for user in users if user["email"] == "test@example.com"]
    assert len(matching_users) == 1
    assert matching_users[0]["name"] == "Test User"

    print("test_user_registration passed.")

if __name__ == "__main__":
    test_user_registration()
