import sqlite3, hashlib, datetime, threading

from errors.custom_exceptions import SaveError, DatabaseError

# ---------- Invoice helpers ----------

from gui.invoicing import create_pdf, send_email  # NEW


def _hash(pw: str) -> str:
    return hashlib.sha256(pw.encode()).hexdigest()


class Storage:
    """Handles all DB operations: users, products, cart, orders, invoices."""

    def __init__(self, db_path: str = "liliwelt.db"):

        self.db_path = db_path

        self.conn: sqlite3.Connection | None = None

    # ---------- connection helpers ----------

    def connect(self):

        self.conn = sqlite3.connect(self.db_path)

    def disconnect(self):

        if self.conn:
            self.conn.close()

            self.conn = None

    # ---------- table creation ----------

    def create_tables(self):

        try:

            self.connect()

            cur = self.conn.cursor()

            # Users

            cur.execute("""

                CREATE TABLE IF NOT EXISTS users (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    username TEXT UNIQUE,

                    password_hash TEXT,

                    is_company INTEGER,

                    company_id TEXT,

                    address TEXT,

                    postcode TEXT,

                    locality TEXT,

                    email TEXT,

                    phone TEXT,

                    birthdate TEXT,

                    company_number TEXT

                )

            """)

            # Product tables

            cur.execute(
                "CREATE TABLE IF NOT EXISTS private_lessons (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)")

            cur.execute(
                "CREATE TABLE IF NOT EXISTS group_workshops (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)")

            cur.execute(
                "CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)")

            # Cart table

            cur.execute("""

                CREATE TABLE IF NOT EXISTS cart_items (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    table_name TEXT,

                    product_id INTEGER,

                    name TEXT,

                    price REAL,

                    quantity INTEGER

                )

            """)

            # Orders + items

            cur.execute("""

                CREATE TABLE IF NOT EXISTS orders (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    datetime TEXT,

                    user_id INTEGER,

                    is_company INTEGER,

                    method TEXT,

                    total REAL

                )

            """)

            cur.execute("""

                CREATE TABLE IF NOT EXISTS order_items (

                    order_id INTEGER,

                    table_name TEXT,

                    product_id INTEGER,

                    quantity INTEGER,

                    price REAL

                )

            """)

            # Invoices

            cur.execute("""

                CREATE TABLE IF NOT EXISTS invoices (

                    id INTEGER PRIMARY KEY AUTOINCREMENT,

                    order_id INTEGER,

                    pdf_path TEXT,

                    sent_at TEXT

                )

            """)

            self.conn.commit()

        finally:

            self.disconnect()

    # ---------- internal fetch helper ----------

    def _fetch(self, query, params=()):

        try:

            self.connect()

            cur = self.conn.cursor()

            cur.execute(query, params)

            return cur.fetchall()

        finally:

            self.disconnect()

    # ---------- user helpers ----------

    def get_username(self, uid):

        self.connect()

        cur = self.conn.cursor()

        cur.execute("SELECT username FROM users WHERE id=?", (uid,))

        name = cur.fetchone()[0]

        self.disconnect()

        return name

    def get_user_email(self, uid):

        self.connect()

        cur = self.conn.cursor()

        cur.execute("SELECT email FROM users WHERE id=?", (uid,))

        mail = cur.fetchone()[0]

        self.disconnect()

        return mail

    # ---------- user management ----------

    def register_user(self, *, username, password, address, postcode, locality,

                      email, phone, is_company, company_number=None, birthdate=None):

        try:

            self.connect()

            cur = self.conn.cursor()

            cur.execute(

                """INSERT INTO users

                    (username, password_hash, is_company, company_id, address, postcode,

                     locality, email, phone, birthdate, company_number)

                   VALUES (?,?,?,?,?,?,?,?,?,?,?)""",

                (username, _hash(password), int(is_company), company_number,

                 address, postcode, locality, email, phone, birthdate, company_number)

            )

            self.conn.commit()

        except sqlite3.IntegrityError:

            self.disconnect()

            raise SaveError("Username already exists")

        finally:

            self.disconnect()

    def authenticate(self, username, password):

        rows = self._fetch(

            "SELECT id, is_company, company_id FROM users WHERE username=? AND password_hash=?",

            (username, _hash(password))

        )

        return rows[0] if rows else None

    # ---------- product loaders ----------

    def load_all_private_lessons(self):

        rows = self._fetch("SELECT id,name,price FROM private_lessons")

        return [dict(table='private_lessons', id=r[0], name=r[1], price=r[2]) for r in rows]

    def load_all_group_workshops(self):

        rows = self._fetch("SELECT id,name,price FROM group_workshops")

        return [dict(table='group_workshops', id=r[0], name=r[1], price=r[2]) for r in rows]

    def load_all_courses(self):

        rows = self._fetch("SELECT id,name,price FROM courses")

        return [dict(table='courses', id=r[0], name=r[1], price=r[2]) for r in rows]

    def load_all_products(self):

        return (self.load_all_private_lessons()

                + self.load_all_group_workshops()

                + self.load_all_courses())

    # ---------- cart ----------

    def load_cart(self):

        rows = self._fetch("SELECT table_name, product_id, name, price, quantity FROM cart_items")

        return [dict(table=r[0], id=r[1], name=r[2], price=r[3], quantity=r[4]) for r in rows]

    def save_cart(self, items):

        """Overwrite the cart_items table with current cart."""

        try:

            self.connect()

            cur = self.conn.cursor()

            cur.execute("DELETE FROM cart_items")

            for it in items:
                cur.execute(

                    "INSERT INTO cart_items (table_name, product_id, name, price, quantity) VALUES (?,?,?,?,?)",

                    (it['table'], it['id'], it['name'], it['price'], it['quantity'])

                )

            self.conn.commit()

        finally:

            self.disconnect()

    # ---------- orders + invoicing ----------

    def save_order(self, cart, user_id, is_company, method, total):

        """

        Stores order + items, generates a PDF invoice and e-mails it.

        Returns the order_id.

        """

        # 1. Save order and items -----------------

        try:

            self.connect()

            cur = self.conn.cursor()

            dt = datetime.datetime.now().isoformat(timespec='seconds')

            cur.execute(

                "INSERT INTO orders (datetime, user_id, is_company, method, total) VALUES (?,?,?,?,?)",

                (dt, user_id, int(is_company), method, total)

            )

            order_id = cur.lastrowid

            for it in cart:
                cur.execute(

                    "INSERT INTO order_items (order_id, table_name, product_id, quantity, price) VALUES (?,?,?,?,?)",

                    (order_id, it['table'], it['id'], it['quantity'], it['price'])

                )

            self.conn.commit()

        finally:

            self.disconnect()

        # 2. Create invoice PDF -------------------

        customer = {

            "name": self.get_username(user_id),

            "email": self.get_user_email(user_id)

        }

        items = [

            {"name": it["name"], "qty": it["quantity"], "price": it["price"]}

            for it in cart

        ]

        pdf_path = create_pdf(order_id, customer, items, total)

        # 3. Send e-mail in background ------------

        threading.Thread(

            target=lambda: send_email(pdf_path, customer),

            daemon=True

        ).start()

        # 4. Log invoice path in DB ---------------

        try:

            self.connect()

            cur = self.conn.cursor()

            cur.execute(

                "INSERT INTO invoices(order_id, pdf_path, sent_at) VALUES (?,?,datetime('now'))",

                (order_id, pdf_path)

            )

            self.conn.commit()

        finally:

            self.disconnect()

        return order_id

