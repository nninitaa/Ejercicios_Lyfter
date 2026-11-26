import os
from contextlib import contextmanager
import psycopg2

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 5432)),
        user=os.getenv("DB_USER", "postgres"),
        password=os.environ["DB_PASSWORD"],
        dbname=os.getenv("DB_NAME", "postgres"),
    )

@contextmanager
def get_cursor():
    connection = get_connection()
    cursor = connection.cursor()
    try:
        yield cursor
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        cursor.close()
        connection.close()
