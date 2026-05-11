email = "usuario@email.com"
username = "usuario123"
password = "pa$$word137"

result = email + " " + username + " " + password
print(result)
#usuario@email.com usuario123 pa$$word137

name = "jhon"
year = 2026
user_name = name + str(year)

print(f"Su usuario es: {user_name}")
#Su usuario es: jhon2026

first_days = ["Lunes", "Martes", "Miercoles"]
second_days = ["Jueves", "Viernes"]
week = first_days + second_days

print(week)
#['Lunes', 'Martes', 'Miercoles', 'Jueves

yourname = input("Ingrese su nombre: ")
last_name = input("Ingrese su apellido: ")
yourage_raw = input("Ingrese su edad: ")

yourage = int(yourage_raw)

if 0 <= yourage <= 1:
    category = "Bebé"
elif 1 < yourage <= 12:
    category = "Niño"
elif 12 < yourage <= 15:
    category = "Pre-adolescente"
elif 15 < yourage <= 17:
    category = "Adolescente"
elif 18 <= yourage <= 24:
    category = "Adulto joven"
elif 24 < yourage <= 40:
    category = "Adulto"
elif 40 < yourage <= 60:
    category = "Adulto mayor"
else:
    category = "Rango fuera de los parámetros"

full_name = yourname + " " + last_name
print("Hola " + full_name + "!")
print(f"Tu edad es {yourage}, por lo tanto tu categoria es: {category}.")

import random 

secret_number = random.randint(1, 100)
guess = 0

print("Adivina el numero entre 1 y 100")

while guess != secret_number:
    try:
        guess = int(input("Ingresa un numero: "))
        if guess < secret_number:
            print("Muy bajo")
        elif guess > secret_number:
            print("Muy alto")
        else: 
            print("Correcto")
    except ValueError:
        print("Error numero invalido")

number1 = int(input("Ingrese un primer numero: "))
number2 = int(input("Ingrese un segundo numero: "))
number3 = int(input("Ingrese un tercer numero: "))

highest = max(number1, number2, number3)
print(f"El numero mayor es:{highest}")

total = int(input("¿Cuantas notas desea ingresar?: "))

total_sum = 0
approved_sum = 0
failed_sum = 0

approved_count = 0
failed_count = 0

for i in range(total):
    grade = float(input(f"Ingrese la nota {i+1}"))

    total_sum += grade

    if grade >= 70:
        approved_count += 1
        approved_count += grade
    else:
        failed_sum += 1
        failed_sum += grade
overall_avg = total_sum / total
if approved_count > 0:
    approved_avg = approved_sum / approved_count
else:
    approved_avg = 0

if failed_count > 0:
    failed_avg = failed_sum / failed_count
else: 
    failed_avg = 0

print("Aprobadas:", approved_count)
print("Desaprobadas:", failed_count)
print("Promedio general:", overall_avg)
print("Promedio aprobadas:", approved_avg)
print("Promedio desaprobadas:", failed_avg)
