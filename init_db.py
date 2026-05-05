import sqlite3
import os

DB_PATH = os.path.join("database_file", "Ecc_signature.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# USER TABLE
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

# OWNER TABLE
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

# FILE TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS file (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    file TEXT,
    filename TEXT,
    CDate TEXT,
    data TEXT,
    owner TEXT,
    pk TEXT,
    mk TEXT,
    privatekey TEXT
)
""")

# CLOUD DATA TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS cloudadata (
    filename TEXT,
    owner TEXT,
    f1 TEXT,
    skey TEXT,
    f2 TEXT,
    skey1 TEXT,
    f3 TEXT,
    skey2 TEXT,
    data TEXT,
    status TEXT
)
""")

# REQUEST TABLE
cur.execute("""
CREATE TABLE IF NOT EXISTS request (
    filename TEXT,
    data TEXT,
    owner TEXT,
    status TEXT,
    email TEXT,
    p1 TEXT,
    p2 TEXT,
    p3 TEXT,
    s1 TEXT,
    s2 TEXT,
    s3 TEXT
)
""")

conn.commit()
conn.close()

print("Database created successfully!")