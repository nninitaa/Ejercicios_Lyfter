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
        UPDATE lyfter_car_rental.rentals
        SET rent_state = %s
        WHERE id = %s
        RETURNING id_cars
    """

    values = ('finished', 4)

    cursor.execute(consult, values)
    result = cursor.fetchone()
    print(result)

    if result is None:
        print("Alquiler no encontrado")

    else:
        car_id = result[0]

        cursor.execute("""
        UPDATE lyfter_car_rental.cars
        SET car_status = %s
        WHERE id = %s
""", ("available", car_id))

        connection.commit()

        print("Return confirmed")

except Exception as error:
        if connection:
            connection.rollback()

        print(f"Error: {error}")

finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()