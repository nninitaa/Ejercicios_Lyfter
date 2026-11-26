import psycopg2


connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="irina2008araya",
    dbname="postgres",
)
print("Connected to the database")

cursor = connection.cursor()

consult = """
    UPDATE lyfter_car_rental.cars
    SET car_status = %s
    WHERE id = %s
"""

values = ('available', '2')

cursor.execute(consult, values)

connection.commit()

print("Changed car status")

cursor.close()
connection.close()