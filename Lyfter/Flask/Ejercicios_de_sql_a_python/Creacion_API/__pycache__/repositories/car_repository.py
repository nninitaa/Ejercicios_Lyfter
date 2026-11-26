from db import get_cursor
from exceptions import NotFoundError
from repositories.base import build_where

FILTERABLE_COLUMNS = ["id", "brand", "model", "manufacture_year", "car_status"]
CAR_AVAILABLE = "available"
CAR_RENTED = "rented"

def create(brand, model, manufacture_year, car_status):
    query = """
        INSERT INTO lyfter_car_rental.cars (brand, model, manufacture_year, car_status)
        VALUES (%s, %s, %s, %s)
    """
    with get_cursor() as cursor:
        cursor.execute(query, (brand, model, manufacture_year, car_status))

def find_all(filters=None):
    where, values = build_where(filters or {}, FILTERABLE_COLUMNS)
    query = f"""
        SELECT id, brand, model, manufacture_year, car_status
        FROM lyfter_car_rental.cars
        {where}
    """
    with get_cursor() as cursor:
        cursor.execute(query, values)
        rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "brand": row[1],
            "model": row[2],
            "manufacture_year": row[3],
            "car_status": row[4],
        }
        for row in rows
    ]

def update_status(car_id, car_status):
    query = """
        UPDATE lyfter_car_rental.cars
        SET car_status = %s
        WHERE id = %s
    """
    with get_cursor() as cursor:
        cursor.execute(query, (car_status, car_id))
        if cursor.rowcount == 0:
            raise NotFoundError("Car not found")