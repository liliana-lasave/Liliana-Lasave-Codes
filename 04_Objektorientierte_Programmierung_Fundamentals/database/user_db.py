import json
import os

# Define the path to the data folder
DATABASE_DIR = "data"

# Define the full path to the customers.json file
CUSTOMERS_FILE = os.path.join(DATABASE_DIR, "customers.json")


# This function loads all users from the JSON file.
# If the file does not exist, it returns an empty list.
def load_users():
    if not os.path.exists(CUSTOMERS_FILE):
        return []
    with open(CUSTOMERS_FILE, "r") as f:
        return json.load(f)


# This function saves a new user to the customers.json file.
# It creates the "data" folder if it does not exist.
def save_user(user_data):
    # Make sure the "data" folder exists
    os.makedirs(DATABASE_DIR, exist_ok=True)

    # Load existing users
    users = load_users()

    # Add the new user to the list
    users.append(user_data)

    # Write all users back to the file
    with open(CUSTOMERS_FILE, "w") as f:
        json.dump(users, f, indent=4)
