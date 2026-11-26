from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json()
    required = ["brand", "model", "manufacture_year", "car_status"]

    if not data or not all(field in data for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    connection = None
    cursor = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        consult = """
            INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status)
            VALUES (%s, %s, %s, %s)
        """
        values = (data["brand"], data["model"], data["manufacture_year"], data["car_status"])

        cursor.execute(consult, values)
         
        connection.commit()

        return jsonify({"message": "Car created successfully"}), 201

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