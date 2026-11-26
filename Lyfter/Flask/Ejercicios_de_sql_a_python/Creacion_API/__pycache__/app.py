import psycopg2.errors
from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

from exceptions import CarNotAvailableError, NotFoundError
from repositories import car_repository, rental_repository, user_repository

app = Flask(__name__)

@app.errorhandler(NotFoundError)
def handle_not_found(error):
    return jsonify({"error": str(error)}), 404


@app.errorhandler(CarNotAvailableError)
def handle_car_not_available(error):
    return jsonify({"error": str(error)}), 409


@app.errorhandler(psycopg2.errors.UniqueViolation)
def handle_unique_violation(error):
    return jsonify({"error": "Email or username already exists"}), 409


@app.errorhandler(psycopg2.errors.ForeignKeyViolation)
def handle_foreign_key_violation(error):
    return jsonify({"error": "Referenced user or car does not exist"}), 400


@app.errorhandler(Exception)
def handle_unexpected(error):
    if isinstance(error, HTTPException):
        return error
    return jsonify({"error": str(error)}), 500


def missing_fields(data, required):
    return not data or not all(field in data for field in required)


@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json(silent=True)
    if missing_fields(data, ["name", "email", "username", "password", "birthdate"]):
        return jsonify({"error": "Missing required fields"}), 400

    user_repository.create(
        data["name"], data["email"], data["username"],
        data["password"], data["birthdate"],
    )
    return jsonify({"message": "User created successfully"}), 201


@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(user_repository.find_all(request.args)), 200


@app.route("/users/<int:id>", methods=["PATCH"])
def update_user_status(id):
    data = request.get_json(silent=True)
    if missing_fields(data, ["account_status"]):
        return jsonify({"error": "Missing required fields"}), 400

    user_repository.update_status(id, data["account_status"])
    return jsonify({"message": "User status updated successfully"}), 200


@app.route("/users/<int:id>/overdue", methods=["PATCH"])
def flag_user_as_overdue(id):
    user_repository.update_status(id, "overdue")
    return jsonify({"message": "User flagged as overdue successfully"}), 200

@app.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json(silent=True)
    if missing_fields(data, ["brand", "model", "manufacture_year", "car_status"]):
        return jsonify({"error": "Missing required fields"}), 400

    car_repository.create(
        data["brand"], data["model"],
        data["manufacture_year"], data["car_status"],
    )
    return jsonify({"message": "Car created successfully"}), 201


@app.route("/cars", methods=["GET"])
def get_cars():
    return jsonify(car_repository.find_all(request.args)), 200


@app.route("/cars/<int:id>", methods=["PATCH"])
def update_car_status(id):
    data = request.get_json(silent=True)
    if missing_fields(data, ["car_status"]):
        return jsonify({"error": "Missing required fields"}), 400

    car_repository.update_status(id, data["car_status"])
    return jsonify({"message": "Car status updated successfully"}), 200

@app.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json(silent=True)
    if missing_fields(data, ["id_users", "id_cars", "rent_state"]):
        return jsonify({"error": "Missing required fields"}), 400

    rental = rental_repository.create(
        data["id_users"], data["id_cars"], data["rent_state"]
    )
    return jsonify({"message": "Rent created successfully", **rental}), 201


@app.route("/rentals", methods=["GET"])
def get_rentals():
    return jsonify(rental_repository.find_all(request.args)), 200


@app.route("/rentals/<int:id>", methods=["PATCH"])
def update_rental_status(id):
    data = request.get_json(silent=True)
    if missing_fields(data, ["rent_state"]):
        return jsonify({"error": "Missing required fields"}), 400

    rental_repository.update_state(id, data["rent_state"])
    return jsonify({"message": "Rental status updated successfully"}), 200


@app.route("/rentals/<int:id>/complete", methods=["PATCH"])
def complete_rental(id):
    rental_repository.complete(id)
    return jsonify({"message": "Rental completed successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
