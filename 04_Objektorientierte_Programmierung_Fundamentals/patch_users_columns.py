import sqlite3, os

db = os.path.abspath("liliwelt.db")

conn = sqlite3.connect(db)

cur = conn.cursor()

for col in (

        "address TEXT", "postcode TEXT", "locality TEXT",

        "email TEXT", "phone TEXT", "birthdate TEXT", "company_number TEXT"

):

    try:

        cur.execute(f"ALTER TABLE users ADD COLUMN {col}")

        print("added", col.split()[0])

    except sqlite3.OperationalError:

        print("already has", col.split()[0])

conn.commit()

conn.close()

