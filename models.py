import sqlite3

DB_NAME = "database.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Users table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        role TEXT
    )
    """)

    # Rides table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS rides (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        lat REAL,
        lng REAL,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()