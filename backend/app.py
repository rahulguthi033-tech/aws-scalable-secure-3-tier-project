
import os
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to AWS 3-Tier Infrastructure Project"
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "application": "AWS 3-Tier Backend"
    })


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME", "rahul_app"),
        port=int(os.getenv("DB_PORT", "3306"))
    )


@app.route("/api/db-health")
def db_health():
    if not all(os.getenv(key) for key in
               ["DB_HOST", "DB_USER", "DB_PASSWORD"]):
        return jsonify({
            "status": "not_configured"
        }), 503

    connection = None

    try:
        connection = get_db_connection()
        return jsonify({"status": "connected"})

    except mysql.connector.Error:
        return jsonify({"status": "error"}), 503

    finally:
        if connection and connection.is_connected():
            connection.close()


@app.route("/api/users")
def get_users():
    connection = None
    cursor = None

    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, name, email, created_at FROM users"
        )

        return jsonify(cursor.fetchall())

    except mysql.connector.Error:
        return jsonify({"error": "Database query failed"}), 503

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )

