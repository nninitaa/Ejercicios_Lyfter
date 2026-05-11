def show_menu():
    print("\nSeleccione una opcion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Borrar resultado")
    print("6. Salir")


def get_option():
    try:
        return int(input("Ingrese el número de la opción: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        return None


def get_number():
    try:
        return float(input("Ingrese un número: "))
    except ValueError:
        print("Error: Por favor, ingrese un número válido.")
        return None


def perform_operation(option, current, number):
    if option == 1:
        return current + number
    elif option == 2:
        return current - number
    elif option == 3:
        return current * number
    elif option == 4:
        if number != 0:
            return current / number
        else:
            print("Error: No se puede dividir por cero.")
            return current
    return current


def main():
    try:
        current_number = float(input("Ingrese un número inicial: "))
    except ValueError:
        print("Número inicial inválido. Usando 0 en su lugar.")
        current_number = 0

    while True:
        show_menu()
        option = get_option()

        if option is None:
            continue

        if option == 6:
            print("Saliendo del programa. ¡Hasta luego!")
            break

        if option < 1 or option > 6:
            print("Opción inválida.")
            continue

        if option == 5:
            current_number = 0
            print("El resultado ha sido borrado.")
            continue

        number = get_number()
        if number is None:
            continue

        current_number = perform_operation(option, current_number, number)
        print(f"El resultado actual es: {current_number}")



main()
