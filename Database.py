import sqlite3 as sql

conn = sql.connect("database.db")
print("Database created")

conn.execute("CREATE TABLE reservations (name TEXT, roomNum INTEGER, checkIn TEXT, checkOut TEXT, email TEXT)")
print("Table created")

conn.close()