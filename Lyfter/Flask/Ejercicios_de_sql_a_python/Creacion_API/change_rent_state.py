from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/rentals/<int:id>", methods=["PATCH"])
def update_rental_status(id):
    data = request.get_json()
    required = ["rent_state"]

    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        consult = """
            UPDATE lyfter_car_rental.rentals
            SET rent_state = %s
            WHERE id = %s
        """

        values = (data["rent_state"], id)

        cursor.execute(consult,values)

        if cursor.rowcount == 0:
            return jsonify({"error": "Rental not found"}), 404

        connection.commit()
        
        return jsonify({"message": "Rental status updated successfully"}), 200

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