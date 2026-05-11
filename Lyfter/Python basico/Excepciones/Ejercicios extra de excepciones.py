def ask_name():
    print("Ingrese su nombre: ")
    name = input()
    if name.isnumeric():
        raise ValueError("El nombre no puede ser un número.")
    return name

def ask_age():
    while True:
        try:
            edad = int(input("Ingrese su edad: "))
            return edad
        except ValueError:
            print("Error: Por favor, ingrese un número válido para la edad.")

def show_result(name, age):
    print(f"Hola {name}, su edad es {age}.")

def main():
    name = ask_name()
    age = ask_age()
    show_result(name, age)

main()

# Ejercicio 2
my_list = ["1", "2", "tres", "4", "cinco"]
def convert_wholenumber(my_list):
    for e in my_list:
        try: 
            number = int(e)
            print(number)
        except ValueError:
                print(f"Error: No se pudo convertir '{e}' a un número entero.")  

convert_wholenumber(my_list)

# Ejercicio 3
second_list = ["1.5", "2.3", "tres", "4.0", "cinco"]
def sum_values(second_list):
    sum = 0
    for e in second_list:
        try:
            number = float(e)
            sum += number
            print(f"{e} sumado correctamente.")
        except ValueError:
            print(f"Elemento invalido: {e}")

    return sum

print("Suma total:", sum_values(second_list))