from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/rentals", methods=["GET"])
def get_rentals():

    filters = request.args
    conditions = []
    values = []

    for column, value in filters.items():

        if column in ['id', 'id_users', 'id_cars', 'rent_date', 'rent_state']:

            conditions.append(f"{column} = %s")
            values.append(value)

    consult = """
        SELECT id, id_users, id_cars, rent_date, rent_state
        FROM lyfter_car_rental.rentals
    """

    if conditions:
        consult += " WHERE " + " AND ".join(conditions)

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(consult, values)
        results = cursor.fetchall()
        rentals = []

        for rental in results:
            rentals.append({
                "id": rental[0],
                "id_users": rental[1],
                "id_cars": rental[2],
                "rent_date": rental[3],
                "rent_state": rental[4]
            })

        return jsonify(rentals), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if connection:
            connection.close()