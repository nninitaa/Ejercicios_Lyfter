from db import get_cursor
from exceptions import CarNotAvailableError, NotFoundError
from repositories.base import build_where
from repositories.car_repository import CAR_AVAILABLE, CAR_RENTED

FILTERABLE_COLUMNS = ["id", "id_users", "id_cars", "rent_date", "rent_state"]

def create(id_users, id_cars, rent_state):
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT car_status
            FROM lyfter_car_rental.cars
            WHERE id = %s
            FOR UPDATE
            """,
            (id_cars,),
        )
        car = cursor.fetchone()

        if car is None:
            raise NotFoundError("Car not found")

        if car[0] != CAR_AVAILABLE:
            raise CarNotAvailableError("Car is not available")

        cursor.execute(
            """
            INSERT INTO lyfter_car_rental.rentals (id_users, id_cars, rent_state)
            VALUES (%s, %s, %s)
            RETURNING id, rent_date
            """,
            (id_users, id_cars, rent_state),
        )
        rental = cursor.fetchone()

        cursor.execute(
            """
            UPDATE lyfter_car_rental.cars
            SET car_status = %s
            WHERE id = %s
            """,
            (CAR_RENTED, id_cars),
        )

    return {"id": rental[0], "rent_date": rental[1]}

def find_all(filters=None):
    where, values = build_where(filters or {}, FILTERABLE_COLUMNS)
    query = f"""
        SELECT id, id_users, id_cars, rent_date, rent_state
        FROM lyfter_car_rental.rentals
        {where}
    """
    with get_cursor() as cursor:
        cursor.execute(query, values)
        rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "id_users": row[1],
            "id_cars": row[2],
            "rent_date": row[3],
            "rent_state": row[4],
        }
        for row in rows
    ]
def update_state(rental_id, rent_state):
    query = """
        UPDATE lyfter_car_rental.rentals
        SET rent_state = %s
        WHERE id = %s
    """
    with get_cursor() as cursor:
        cursor.execute(query, (rent_state, rental_id))
        if cursor.rowcount == 0:
            raise NotFoundError("Rental not found")
        
def complete(rental_id):
    with get_cursor() as cursor:
        cursor.execute(
            """
            UPDATE lyfter_car_rental.rentals
            SET rent_state = %s
            WHERE id = %s
            RETURNING id_cars
            """,
            ("finished", rental_id),
        )
        result = cursor.fetchone()

        if result is None:
            raise NotFoundError("Rental not found")

        cursor.execute(
            """
            UPDATE lyfter_car_rental.cars
            SET car_status = %s
            WHERE id = %s
            """,
            (CAR_AVAILABLE, result[0]),
        )
