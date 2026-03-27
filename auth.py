from flask import Blueprint, request, jsonify, session
import sqlite3

auth = Blueprint("auth", __name__)

def connect():
    return sqlite3.connect("database.db")

# REGISTER
@auth.route("/register", methods=["POST"])
def register():
    data = request.json

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO users (username, password, role)
    VALUES (?, ?, ?)
    """, (data["username"], data["password"], data["role"]))

    conn.commit()
    conn.close()

    return jsonify({"message": "registered"})

# LOGIN
@auth.route("/login", methods=["POST"])
def login():
    data = request.json

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    SELECT * FROM users WHERE username=? AND password=?
    """, (data["username"], data["password"]))

    user = cur.fetchone()
    conn.close()

    if user:
        session["user_id"] = user[0]
        session["role"] = user[3]
        return jsonify({"message": "success", "role": user[3]})

    return jsonify({"error": "invalid"})