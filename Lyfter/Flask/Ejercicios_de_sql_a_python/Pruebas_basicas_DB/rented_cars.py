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

    consult = """
        SELECT id, brand, model, manufacture_year, car_status
        FROM lyfter_car_rental.cars
        WHERE car_status = %s
    """
    values = ('rented',)

    cursor.execute(consult, values)
    cars = cursor.fetchall()

    if not cars:
        print("No rented cars")
    else:
        for car in cars:
            print(car)

except Exception as error:
    print(f"Error: {error}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()