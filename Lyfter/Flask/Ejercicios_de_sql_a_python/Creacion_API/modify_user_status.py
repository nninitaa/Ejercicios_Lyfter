from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/users/<int:id>", methods=["PATCH"])
def update_user_status(id):

    data = request.get_json()

    required = ["account_status"]

    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        consult = """
            UPDATE lyfter_car_rental.users
            SET account_status = %s
            WHERE id = %s
        """

        values = (data["account_status"], id)

        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404

        cursor.execute(consult, values)

        connection.commit()

        return jsonify({"message": "User status updated successfully"}), 200

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