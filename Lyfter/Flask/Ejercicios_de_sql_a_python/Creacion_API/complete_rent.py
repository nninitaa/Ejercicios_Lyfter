from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/rentals/<int:id>", methods=["PATCH"])
def complete_rental(id):

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        consult = """
            UPDATE lyfter_car_rental.rentals
            SET rent_state = %s
            WHERE id = %s
            RETURNING id_cars
        """
        values = ("finished", id)

        cursor.execute(consult, values)
        result = cursor.fetchone()
         
        if result is None:
            connection.rollback()
            return jsonify({"error": "Rental not found"}), 404

        car_id = result[0]
        
        consult = """
            UPDATE lyfter_car_rental.cars
            SET car_status = %s
            WHERE id = %s
        """

        values = ('available', car_id)

        cursor.execute(consult, values)

        connection.commit()

        return jsonify({"message": "Rental completed successfully"}), 200

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