import sqlite3
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database_file", "Ecc_signature.db")


def db_connect():
    return sqlite3.connect(DB_PATH)


# ---------------- USER ----------------
def user_reg(username, password, dob, email, city, cno):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)",
        (username, password, dob, email, city, cno)
    )
    conn.commit()
    conn.close()
    return True


def user_loginact(email, password):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM user WHERE email=? AND password=?", (email, password))
    result = cur.fetchall()
    conn.close()
    return result


# ---------------- OWNER ----------------
def owner_reg(username, password, dob, email, city, cno):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO owner VALUES (?, ?, ?, ?, ?, ?)",
        (username, password, dob, email, city, cno)
    )
    conn.commit()
    conn.close()
    return True


def owner_login(username, password):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM owner WHERE username=? AND password=?", (username, password))
    result = cur.fetchall()
    conn.close()
    return result


# ---------------- SERVER ----------------
def server_logact(username, password):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM server WHERE username=? AND password=?", (username, password))
    result = cur.fetchall()
    conn.close()
    return result


# ---------------- FILE ----------------
def upload_file(fname, filename, username):
    conn = db_connect()
    cur = conn.cursor()

    current_time = str(datetime.datetime.now())

    # Only store filename (safe for deployment)
    cur.execute(
        "INSERT INTO file(filename, CDate, owner) VALUES (?, ?, ?)",
        (filename, current_time, username)
    )

    conn.commit()
    conn.close()
    return True


def owner_viewfiles(username):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT rowid, filename, CDate FROM file WHERE owner=?", (username,))
    result = cur.fetchall()
    conn.close()
    return result


# ---------------- CLOUD ----------------
def upload_clouddata(fname, owner, data, hmsg, pvk, bkey):
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO cloudadata VALUES (?, ?, ?, ?, ?, ?, ?)",
        (fname, owner, data, hmsg, pvk, bkey, "pending")
    )

    conn.commit()
    conn.close()
    return True


def server_viewdata():
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM cloudadata")
    result = cur.fetchall()
    conn.close()
    return result


# ---------------- ML RESULT ----------------
def addf_act(fname, result):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("UPDATE cloudadata SET status=? WHERE filename=?", (result, fname))
    conn.commit()
    conn.close()
    return True


# ---------------- USER FLOW ----------------
def user_viewfile(email):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT filename, owner FROM file")
    result = cur.fetchall()
    conn.close()
    return result


def user_down(email):
    conn = db_connect()
    cur = conn.cursor()
    cur.execute("SELECT filename, owner FROM request WHERE email=? AND status='yes'", (email,))
    result = cur.fetchall()
    conn.close()
    return result