from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/cars", methods=["GET"])
def get_cars():

    filters = request.args
    conditions = []
    values = []

    for column, value in filters.items():

        if column in ['id', 'brand', 'model', 'manufacture_year', 'car_status']:

            conditions.append(f"{column} = %s")
            values.append(value)

    consult =  """
        SELECT id, brand, model, manufacture_year, car_status
        FROM lyfter_car_rental.cars
    """

    if conditions:
        consult += " WHERE " + " AND ".join(conditions)

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(consult, values)
        results = cursor.fetchall()
        cars = []

        for car in results:
            cars.append({
                "id": car[0],
                "brand": car[1],
                "model": car[2],
                "manufacture_year": car[3],
                "car_status": car[4]
            })

        return jsonify(cars), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if connection:
            connection.close()