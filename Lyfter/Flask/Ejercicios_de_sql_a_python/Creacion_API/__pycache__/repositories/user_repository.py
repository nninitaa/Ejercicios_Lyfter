from db import get_cursor
from exceptions import NotFoundError
from repositories.base import build_where

FILTERABLE_COLUMNS = ["id", "name", "email", "username", "birthdate", "account_status"]
def create(name, email, username, password, birthdate):
    query = """
        INSERT INTO lyfter_car_rental.users (name, email, username, password, birthdate)
        VALUES (%s, %s, %s, %s, %s)
    """
    with get_cursor() as cursor:
        cursor.execute(query, (name, email, username, password, birthdate))

def find_all(filters=None):
    where, values = build_where(filters or {}, FILTERABLE_COLUMNS)
    query = f"""
        SELECT id, name, email, username, birthdate, account_status
        FROM lyfter_car_rental.users
        {where}
    """
    with get_cursor() as cursor:
        cursor.execute(query, values)
        rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "name": row[1],
            "email": row[2],
            "username": row[3],
            "birthdate": row[4],
            "account_status": row[5],
        }
        for row in rows
    ]

def update_status(user_id, account_status):
    query = """
        UPDATE lyfter_car_rental.users
        SET account_status = %s
        WHERE id = %s
    """
    with get_cursor() as cursor:
        cursor.execute(query, (account_status, user_id))
        if cursor.rowcount == 0:
            raise NotFoundError("User not found")
