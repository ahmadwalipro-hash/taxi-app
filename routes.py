from flask import Blueprint, request, jsonify, session
import sqlite3

routes = Blueprint("routes", __name__)

def connect():
    return sqlite3.connect("database.db")

# REQUEST RIDE
@routes.route("/request_ride", methods=["POST"])
def request_ride():
    if "user_id" not in session:
        return jsonify({"error": "login required"})

    data = request.json

    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO rides (user_id, lat, lng, status)
    VALUES (?, ?, ?, ?)
    """, (session["user_id"], data["lat"], data["lng"], "pending"))

    conn.commit()
    conn.close()

    return jsonify({"message": "ride requested"})

# GET RIDES (Driver)
@routes.route("/rides")
def rides():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM rides")
    data = cur.fetchall()

    conn.close()

    return jsonify(data)

# ACCEPT RIDE
@routes.route("/accept/<int:id>", methods=["POST"])
def accept(id):
    conn = connect()
    cur = conn.cursor()

    cur.execute("UPDATE rides SET status='accepted' WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return jsonify({"message": "accepted"})