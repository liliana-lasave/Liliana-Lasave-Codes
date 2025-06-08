
import sqlite3

# Connect to the database
conn = sqlite3.connect("liliwelt.db")
cursor = conn.cursor()

# Function to clean duplicates by name and price in a given table
def clean_duplicates_in_table(table_name):
    print(f"Cleaning duplicates in: {table_name}")
    cursor.execute(f"""DELETE FROM {table_name}
        WHERE id NOT IN (
            SELECT MIN(id)
            FROM {table_name}
            GROUP BY name, price
        )
    """)
    conn.commit()

# Apply to all product tables
clean_duplicates_in_table("private_lessons")
clean_duplicates_in_table("group_workshops")
clean_duplicates_in_table("courses")

# Close connection
conn.close()

print("All duplicates by name and price removed from all product tables.")

import sqlite3

# Connect to the database
conn = sqlite3.connect("liliwelt.db")
cursor = conn.cursor()

# Delete duplicates keeping only one row for each name and price combination
cursor.execute("""
DELETE FROM private_lessons
WHERE id NOT IN (
    SELECT MIN(id)
    FROM private_lessons
    GROUP BY name, price
)
""")

# Commit changes and close the connection
conn.commit()
conn.close()

print("Duplicates (by name and price) removed.")

