#Ejercicio normal de ordenamiento de burbuja
def bubble_sort(list):
    n = len(list)

    for i in range(n):
     for j in range(n - i - 1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

    return list

#Ejercicio de ordenamiento de burbuja modificado para ordenar derecha a izquierda
numbers = [8, 2, 6, 4, 10]

for i in range(len(numbers)):
    for j in range(len(numbers) - 1, 0, -1):
        if numbers[j - 1] > numbers[j]:
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]

print(numbers)