import sqlite3
from products_liliwelt import Product, PrivateLesson, GroupWorkshop, Course


# Class to manage database connection and operations
class Storage:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    # Open the database connection
    def connect(self):
        self.connection = sqlite3.connect(self.database_name)

    # Close the database connection
    def disconnect(self):
        if self.connection:
            self.connection.close()

    # Create all necessary tables if they do not exist
    def create_tables(self):
        self.connect()
        cursor = self.connection.cursor()

        # PrivateLesson table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS private_lessons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                duration TEXT,
                level TEXT,
                audience TEXT,
                modality TEXT,
                teacher_name TEXT,
                instrument TEXT
            )
        """)

        # GroupWorkshop table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS group_workshops (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                duration TEXT,
                level TEXT,
                audience TEXT,
                modality TEXT,
                theme TEXT,
                max_participants INTEGER
            )
        """)

        # Course table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                duration TEXT,
                level TEXT,
                audience TEXT,
                modality TEXT,
                num_sessions INTEGER,
                certificate INTEGER
            )
        """)

        self.connection.commit()
        self.disconnect()

    # Save a product object to the corresponding database table
    def save_product(self, product):
        self.connect()
        cursor = self.connection.cursor()

        if isinstance(product, PrivateLesson):
            cursor.execute("""
                INSERT INTO private_lessons (name, price, duration, level, audience, modality, teacher_name, instrument)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (product.name, product.price, product.duration, product.level,
                  product.audience, product.modality, product.teacher_name, product.instrument))

        elif isinstance(product, GroupWorkshop):
            cursor.execute("""
                INSERT INTO group_workshops (name, price, duration, level, audience, modality, theme, max_participants)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (product.name, product.price, product.duration, product.level,
                  product.audience, product.modality, product.theme, product.max_participants))

        elif isinstance(product, Course):
            cursor.execute("""
                INSERT INTO courses (name, price, duration, level, audience, modality, num_sessions, certificate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (product.name, product.price, product.duration, product.level,
                  product.audience, product.modality, product.num_sessions, int(product.certificate)))

        else:
            raise ValueError("Unknown product type")

        self.connection.commit()
        self.disconnect()

    # Load all private lessons from the database

    def load_all_private_lessons(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM private_lessons")
        rows = cursor.fetchall()
        lessons = [PrivateLesson(*row[1:]) for row in rows]
        self.disconnect()
        return lessons

    # Load all group workshops from the database
    def load_all_group_workshops(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM group_workshops")
        rows = cursor.fetchall()
        workshops = [GroupWorkshop(*row[1:]) for row in rows]

        self.disconnect()
        return workshops

    # Load all courses from the database
    def load_all_courses(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        courses = [Course(*row[1:]) for row in rows]

        self.disconnect()
        return courses

    # Load all products from all categories
    def load_all_products(self):
        return (
                self.load_all_private_lessons()
                + self.load_all_group_workshops()
                + self.load_all_courses()
        )


# Main script to test functionality
if __name__ == "__main__":
    storage = Storage("../liliwelt.db")
    storage.create_tables()  # Creates tables if they don't exist

    # Load all products and print their info
    products = storage.load_all_products()
    for p in products:
        print(p.get_info())

