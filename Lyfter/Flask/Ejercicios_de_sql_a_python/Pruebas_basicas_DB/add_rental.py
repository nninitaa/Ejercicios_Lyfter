import psycopg2

connection = None
cursor = None

try:
    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        user="postgres",
        password="irina2008araya",
        dbname="postgres",
    )
    cursor = connection.cursor()
    print("Connected to the database")

    consult = """
        INSERT INTO lyfter_car_rental.rentals(id_users, id_cars)
        VALUES (%s, %s)
    """
    values = (2, 4)

    cursor.execute(consult, values)
    connection.commit()

    print("Added rent")

except Exception as error:
    if connection:
        connection.rollback()
    print(f"Error: {error}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()