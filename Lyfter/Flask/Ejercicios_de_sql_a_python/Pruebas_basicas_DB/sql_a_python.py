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
    INSERT INTO lyfter_car_rental.users(name, email, username, password, birthdate)
    VALUES (%s, %s, %s, %s, %s)
"""

values = ('ana', 'anamoya56@gmail.com', 'ana_moya', '4n4m0y4', '1999-02-03')

cursor.execute(consult, values)

connection.commit()

print("Usuario agregado")

cursor.close()
connection.close()