#Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
first_list = ["This", "is"]
second_list = ["a", "text"]

for i in range(len(first_list)):
    print(f"{first_list[i]} {second_list[i]}")

#Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
my_string = "Hello World"

for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])

#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
def swap_last(lists):
    if len(lists) > 1:
        lists[0], lists[-1] = lists[-1], lists[0]

    return lists

my_list = [10, 20, 30, 40, 50]
print(f"Original: {my_list}")
print(f"Switch: {swap_last(my_list)}")

#Cree un programa que elimine todos los números impares de una lista.
def remove(list):
    new_list = []
    for element in list:
        if element % 2 == 0:
            new_list.append(element)
    return new_list

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
no_oddnumbers = remove(list)
print("Original: " + str(list))
print("No odd numbers: " + str(no_oddnumbers))

#Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
text = (input("Type a list of 10 numbers separated by commas: "))
numbers = [int(num.strip()) for num in text.split(",")]

max_value = None
for num in numbers:
    if max_value is None or num > max_value:
        max_value = num

print("Maximum Value: ", max_value)