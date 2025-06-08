
import sqlite3

# Connect to the database (must be in the same directory as this script)
conn = sqlite3.connect("liliwelt.db")
cursor = conn.cursor()

# Query the products table
cursor.execute("SELECT * FROM private_lessons")
rows = cursor.fetchall()

# Display the results
print("Products found in private_lessons:")
for row in rows:
    print(row)

# Close the database connection
conn.close()
