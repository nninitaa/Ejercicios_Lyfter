from flask import Flask, jsonify, request
import psycopg2
from db import get_connection

app = Flask(__name__)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    required = ["name", "email", "username", "password", "birthdate"]

    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        consult = """
            INSERT INTO lyfter_car_rental.users (name, email, username, password, birthdate)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (data["name"], data["email"], data["username"], data["password"], data["birthdate"])

        cursor.execute(consult, values)
        connection.commit()

        return jsonify({"message": "User created successfully"}), 201

    except psycopg2.errors.UniqueViolation:
        connection.rollback()
        return jsonify({"error": "Email or username already exists"}), 409

    except Exception as error:
        if connection:
            connection.rollback()
        return jsonify({"error": str(error)}), 500


    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    app.run(debug=True)