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
    INSERT INTO lyfter_car_rental.cars(brand, model, manufacture_year)
    VALUES (%s, %s, %s)
"""

values = ('Toyota', 'Corolla', 2024)

cursor.execute(consult, values)

connection.commit()

print("Added car")

cursor.close()
connection.close()