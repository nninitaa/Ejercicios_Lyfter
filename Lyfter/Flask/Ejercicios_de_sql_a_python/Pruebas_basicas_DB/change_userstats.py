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
    INSERT INTO lyfter_car_rental.rentals(id_users, id_cars)
        VALUES (%s, %s)
"""

values = (2, 4)

cursor.execute(consult, values)

connection.commit()

print("Added rent")

cursor.close()
connection.close()