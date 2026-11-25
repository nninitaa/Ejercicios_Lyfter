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
    UPDATE lyfter_car_rental.rentals
    SET rent_state = %s
    WHERE id = %s
"""

values = ('finished', 1)

cursor.execute(consult, values)

connection.commit()

print("Finished the rent")

cursor.close()
connection.close()