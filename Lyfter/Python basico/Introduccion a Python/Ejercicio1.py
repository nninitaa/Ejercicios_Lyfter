# Ask the user for a number
number = input("Ingrese un numero: ")

# Remove negative sign if it exists
number = number.replace("-", "")

# Remove decimal point if it exists
number = number.replace(".", "")

# Count digits
digit_count = len(number)

# Show result
print("El numero tiene", digit_count, "digitos")