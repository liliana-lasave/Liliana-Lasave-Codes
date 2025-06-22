import sqlite3

# Ruta completa al archivo .db
db_path = r"C:\Users\052801\Qualifizierung\Github\Liliana-Lasave-Codes-Klon\04_Objektorientierte_Programmierung_Fundamentals\liliwelt.db"

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Mostrar tablas existentes
print("\nTablas disponibles:")
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
for t in tables:
    print("-", t[0])

# Intentar ver datos de la tabla 'users' si existe
if ('users',) in tables:
    print("\n--- CLIENTES (tabla users) ---")
    cursor.execute("SELECT * FROM users")
    for row in cursor.fetchall():
        print(row)
else:
    print("\n❌ No existe la tabla 'users'.")

# Ver productos si existe la tabla
if ('products',) in tables:
    print("\n--- PRODUCTOS (tabla products) ---")
    cursor.execute("SELECT * FROM products")
    for row in cursor.fetchall():
        print(row)
else:
    print("\n❌ No existe la tabla 'products'.")

conn.close()
