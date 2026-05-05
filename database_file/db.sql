import sqlite3
import os

DB_PATH = os.path.join("database_file", "Ecc_signature.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# USER
cur.execute("""
CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    dob TEXT,
    email TEXT,
    city TEXT,
    contact TEXT
)
""")

# OWNER
cur.execute("""
CREATE TABLE IF NOT EXISTS owner (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    password TEXT,
    dob TEXT,
    email TEXT,
    city TEXT,
    contact TEXT
)
""")

# FILE
cur.execute("""
CREATE TABLE IF NOT EXISTS file (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    CDate TEXT,
    owner TEXT
)
""")

# CLOUD DATA
cur.execute("""
CREATE TABLE IF NOT EXISTS cloudadata (
    filename TEXT,
    owner TEXT,
    data TEXT,
    hsmsg TEXT,
    pvk TEXT,
    blockkey TEXT,
    status TEXT
)
""")

# REQUEST
cur.execute("""
CREATE TABLE IF NOT EXISTS request (
    filename TEXT,
    data TEXT,
    owner TEXT,
    status TEXT,
    email TEXT,
    hsmsg TEXT
)
""")

# SERVER
cur.execute("""
CREATE TABLE IF NOT EXISTS server (
    username TEXT,
    password TEXT
)
""")

# default server login
cur.execute("INSERT INTO server VALUES ('admin', 'admin')")

conn.commit()
conn.close()

print("Database created successfully!")