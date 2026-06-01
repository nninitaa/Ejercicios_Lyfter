#Ejercicio normal de ordenamiento de burbuja
numbers = [8, 2, 6, 4, 10]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)

#Ejercicio de ordenamiento de burbuja modificado para ordenar de mayor a menor
numbers = [8, 2, 6, 4, 10]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] < numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print(numbers)