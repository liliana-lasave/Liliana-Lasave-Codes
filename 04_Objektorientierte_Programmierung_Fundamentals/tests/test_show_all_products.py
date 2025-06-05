import sqlite3
import os

# Automatically find the path to the database file (go up one level from tests/)
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'liliwelt.db'))

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# List of product tables to check
tables = ["private_lessons", "group_workshops", "courses"]

# Loop through each table and print its contents
for table in tables:
    print(f"\nContents of table '{table}':")
    try:
        cursor.execute(f"SELECT * FROM {table}")
        rows = cursor.fetchall()
        if not rows:
            print("No records found.")
        else:
            for row in rows:
                print(row)
    except sqlite3.OperationalError as e:
        print(f"Error querying {table}: {e}")

# Close the database connection
conn.close()