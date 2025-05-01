# Create the database and insert data
import sqlite3

conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

cursor.executemany("INSERT INTO sales VALUES (?, ?, ?)", [
    ("Apple", 10, 1.5),
    ("Banana", 5, 0.8),
    ("Apple", 7, 1.5),
    ("Orange", 3, 1.2),
    ("Banana", 8, 0.8),
    ("Orange", 5, 1.2)
])

conn.commit()
conn.close()

print("Database created and data added.")
