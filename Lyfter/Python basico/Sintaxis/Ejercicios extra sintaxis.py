#Ejercicio 1
price = float(input("Ingrese el precio: "))

if price < 100:
    discount = price * 0.02
else:
    discount = price * 0.10

final_price = price - discount

print("El descuento aplicado es: ", discount)
print("El precio final a pagar es: ", final_price)

#Ejercicio 2
seconds = int(input("Ingrese el tiempo en segundos: "))

limit_seconds = 600

if seconds > limit_seconds:
    print("Mayor")
elif seconds == limit_seconds:
    print("Igual")
else: 
    missing = limit_seconds - seconds
    print(f"Faltan {missing} segundos")

#Ejercicio 3
number = int(input("Ingrese un número: "))

total_sum = 0

for i in range(1, number + 1):
    total_sum += i

print(f"La suma de los números del 1 al {number} es: {total_sum}")

#Ejercicio 4
import random 

secret_number = random.randint(1, 10)
guess = 0

print("Adivina el numero entre 1 y 10")

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

#Ejercicio 5
number1 = int(input("Ingrese un primer número: "))
number2 = int(input("Ingrese un segundo número: "))
number3 = int(input("Ingrese un tercer número: "))

if number1 == 30 or number2 == 30 or number3 == 30 or (number1 + number2 + number3 == 30):
    print("Correcto")
else: 
    print("Incorrecto")

#Ejercicio 6 (Escala de Celsius, Fahrenheit y Kelvin)
celsius = float(input("Ingrese la temperatura en Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print(f"Temperatura en Celsius: {celsius}")
print(f"Temperatura en Fahrenheit: {fahrenheit}")
print(f"Temperatura en Kelvin: {kelvin}")

#Ejercicio 7
number = int(input("Ingrese un número del 1 al 10: "))

for i in range(1, 13):
    result = number * i
    print(number, "x", i, "=", result)