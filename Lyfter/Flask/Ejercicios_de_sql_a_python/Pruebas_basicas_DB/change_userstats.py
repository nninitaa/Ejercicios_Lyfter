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
        UPDATE lyfter_car_rental.users
        SET account_status = %s
        WHERE id = %s
    """
    values = ('overdue', 2)

    cursor.execute(consult, values)

    if cursor.rowcount == 0:
        print("User not found")
    else:
        connection.commit()
        print("Changed user status")

except Exception as error:
    if connection:
        connection.rollback()
    print(f"Error: {error}")

finally:
    if cursor:
        cursor.close()
    if connection:
        connection.close()