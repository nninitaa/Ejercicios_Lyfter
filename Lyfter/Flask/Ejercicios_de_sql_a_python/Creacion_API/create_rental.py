from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json()
    required = ["id_users", "id_cars", "rent_date", "rent_state"]

    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        consult = """
            INSERT INTO lyfter_car_rental.rentals (id_users, id_cars, rent_date, rent_state)
            VALUES (%s, %s, %s, %s)
        """
        values = (data["id_users"], data["id_cars"], data["rent_date"], data["rent_state"])

        cursor.execute(consult, values)
         
        connection.commit()

        return jsonify({"message": "Rent created successfully"}), 201

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