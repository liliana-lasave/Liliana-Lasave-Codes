import sqlite3

def get_all_products():
    """
    Fetches all products from the data:
    - private_lessons
    - group_workshops
    - courses
    Combines them into a single unified list of dictionaries,
    each including the name, price, and a category label.
    """

    # Connect to the SQLite data file
    conn = sqlite3.connect("liliwelt.db")
    cursor = conn.cursor()
    products = []

    # -------------------------------
    # Read from private_lessons table
    # -------------------------------
    cursor.execute("SELECT name, price FROM private_lessons")
    for row in cursor.fetchall():
        products.append({
            "name": row[0],  # product name
            "price": row[1],  # product price
            "category": "Private Lesson"  # label for filtering
        })

    # -------------------------------
    # Read from group_workshops table
    # -------------------------------
    cursor.execute("SELECT name, price FROM group_workshops")
    for row in cursor.fetchall():
        products.append({
            "name": row[0],
            "price": row[1],
            "category": "Group Workshop"
        })

    # -------------------
    # Read from courses table
    # -------------------
    cursor.execute("SELECT name, price FROM courses")
    for row in cursor.fetchall():
        products.append({
            "name": row[0],
            "price": row[1],
            "category": "Course"
        })

    # Close the data connection
    conn.close()

    # Return a combined list of all products
    return products

