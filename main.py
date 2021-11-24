import sqlite3

conn = sqlite3.connect("lite.db")

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Store (Item VARCHAR, Quantity INTEGER, price REAL)")
cur.execute("INSERT INTO store VALUES ('Wine Glass', 8,10.5)")
conn.commit()
conn.close()
