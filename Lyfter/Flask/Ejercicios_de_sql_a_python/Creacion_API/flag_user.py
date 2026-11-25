from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/users/<int:id>/overdue", methods=["PATCH"])
def flag_user_as_overdue(id):

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

        values = ('overdue', id)

        cursor.execute(consult, values)


        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404

        connection.commit()

        return jsonify({"message": "User flagged as overdue successfully"}), 200

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