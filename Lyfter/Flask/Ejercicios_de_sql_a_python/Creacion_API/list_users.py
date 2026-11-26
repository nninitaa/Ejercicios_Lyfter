from flask import Flask, jsonify, request
from db import get_connection

app = Flask(__name__)

@app.route("/users", methods=["GET"])
def get_users():

    filters = request.args
    conditions = []
    values = []

    for column, value in filters.items():

        if column in ['id', 'name', 'email', 'username', 'birthdate', 'account_status']:

            conditions.append(f"{column} + %s")
            values.append(value)

    consult = """
        SELECT id, name, email, username, birthdate, account_status
        FROM lyfter_car_rental.users
    """

    if conditions:
        consult += " WHERE " + " AND ".join(conditions)

    connection = None

    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(consult, values)
        results = cursor.fetchall()
        users = []

        for user in results:
            users.append({
                "id": user[0],
                "name": user[1],
                "email": user[2],
                "username": user[3],
                "birthdate": user[4],
                "account_status": user[5]
            })

        return jsonify(users), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500

    finally:
        if connection:
            connection.close()