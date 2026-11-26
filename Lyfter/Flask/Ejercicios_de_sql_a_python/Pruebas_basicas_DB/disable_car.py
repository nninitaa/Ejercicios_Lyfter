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

    car_id = 6

    consult = """
        UPDATE lyfter_car_rental.cars
        SET car_status = %s
        WHERE id = %s AND car_status <> %s
    """
    values = ('disabled', car_id, 'rented')

    cursor.execute(consult, values)

    if cursor.rowcount == 0:
        print("Car not found or is already rented")
    else:
        connection.commit()
        print("Car disabled")

except Exception as error:
    if connection:
        connection.rollback()
    print(f"Error: {error}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()