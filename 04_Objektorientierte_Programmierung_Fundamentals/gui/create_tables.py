import sqlite3
import os

# Always create and connect to the DB in the project root
db_path = os.path.join(os.path.dirname(__file__), "liliwelt.db")
print("✅ Creating DB at:", db_path)

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create main users table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    postcode TEXT,
    locality TEXT,
    email TEXT UNIQUE,
    phone TEXT,
    password TEXT,
    type TEXT
)
""")

# Private customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS private_customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    birthdate TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

# Company customers table
cursor.execute("""
CREATE TABLE IF NOT EXISTS company_customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    company_number TEXT,
    FOREIGN KEY (user_id) REFERENCES users(id)
)
""")

conn.commit()
conn.close()
print("✅ Tables created successfully.")
