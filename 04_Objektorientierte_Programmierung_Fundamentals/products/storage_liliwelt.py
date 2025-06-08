import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import sqlite3
from errors.custom_exceptions import DatabaseError, ConnectionError, SaveError, NotFoundError
from products.products_liliwelt import Product, PrivateLesson, GroupWorkshop, Course

# Class to manage data connection and operations
class Storage:
    def __init__(self, database_name):
        self.database_name = database_name
        self.connection = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database_name)
        except sqlite3.Error as e:
            raise ConnectionError(f"Could not connect to the database: {e}")

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def create_tables(self):
        try:
            self.connect()
            cursor = self.connection.cursor()

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
        except sqlite3.Error as e:
            raise SaveError(f"Failed to create tables: {e}")

    def save_product(self, product):
        try:
            self.connect()
            cursor = self.connection.cursor()

            if isinstance(product, PrivateLesson):
                cursor.execute("""
                    INSERT INTO private_lessons (name, price, duration, level, audience, modality, teacher_name, instrument)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (product.name, product.price, product.duration, product.level,
                      product.audience, product.modality, product.teacher_name, product.instrument))
                product.id = cursor.lastrowid

            elif isinstance(product, GroupWorkshop):
                cursor.execute("""
                    INSERT INTO group_workshops (name, price, duration, level, audience, modality, theme, max_participants)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (product.name, product.price, product.duration, product.level,
                      product.audience, product.modality, product.theme, product.max_participants))
                product.id = cursor.lastrowid

            elif isinstance(product, Course):
                cursor.execute("""
                    INSERT INTO courses (name, price, duration, level, audience, modality, num_sessions, certificate)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (product.name, product.price, product.duration, product.level,
                      product.audience, product.modality, product.num_sessions, int(product.certificate)))
                product.id = cursor.lastrowid

            else:
                raise ValueError("Unknown product type")

            self.connection.commit()
            self.disconnect()

        except sqlite3.Error as e:
            raise SaveError(f"Failed to save product: {e}")

    def load_all_private_lessons(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM private_lessons")
        rows = cursor.fetchall()
        lessons = [PrivateLesson(*row[1:]) for row in rows]
        self.disconnect()
        return lessons

    def load_all_group_workshops(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM group_workshops")
        rows = cursor.fetchall()
        workshops = [GroupWorkshop(*row[1:]) for row in rows]
        self.disconnect()
        return workshops

    def load_all_courses(self):
        self.connect()
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM courses")
        rows = cursor.fetchall()
        courses = [Course(*row[1:]) for row in rows]
        self.disconnect()
        return courses

    def load_all_products(self):
        return (
            self.load_all_private_lessons()
            + self.load_all_group_workshops()
            + self.load_all_courses()
        )

if __name__ == "__main__":
    storage = Storage("../liliwelt.db")
    storage.create_tables()
    products = storage.load_all_products()
    for p in products:
        print(p.get_info())
