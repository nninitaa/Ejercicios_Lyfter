#Ejercicio normal de ordenamiento de burbuja

numbers = [8, 2, 6, 4, 10]

for i in range(len(numbers)): #O(n^2) Hay varios ciclos anidados, por lo que se multiplican sus tiempos de ejecución
    for j in range(len(numbers) - 1): 
        if numbers[j] > numbers[j + 1]: #O(1) Unicamente se compara dos elementos
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j] #O(1) Unicamente se intercambian dos elementos

print(numbers) #O(n) El tiempo de ejecución es constante 

#Ejercicio de ordenamiento de burbuja modificado para ordenar derecha a izquierda
numbers = [8, 2, 6, 4, 10]

for i in range(len(numbers)): #O(n^2) Hay varios ciclos anidados
    for j in range(len(numbers) - 1, 0, -1): 
        if numbers[j - 1] > numbers[j]: #O(1) Unicamente se compara dos elementos
            numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1] #O(1) Unicamente se intercambian dos elementos

print(numbers) #O(n) El tiempo de ejecución es constante 

def print_numbers_times_2(numbers_list): 
	for number in numbers_list:  #O(1) Ya que solamente lee cada numero de la lista dos veces
		print(number * 2) #O(1) Se imprime ese mismo numero multiplicado por 2

def check_if_lists_have_an_equal(list_a, list_b): 
	for element_a in list_a: #O(n^3) El ciclo se ejecuta n veces n * n = n^2
		for element_b in list_b: 
			if element_a == element_b: #O(1) Unicamente se compara dos elementos
				return True #O(1) Retorna verdadero si encuentra un elemento igual en ambas listas
				
	return False #O(1) Retorna falso si no encuentra un elemento igual en 1ambas listas

def print_10_or_less_elements(list_to_print): 
	list_len = len(list_to_print) #O(n) Lee la lista para obtener su longitud
 		print(list_to_print[index])#O(1) Imprime el elemento en la posición indice de la lista

def generate_list_trios(list_a, list_b, list_c): 
	result_list = [] #O(1) Se crea una lista vacia para almacenar los resultados
	for element_a in list_a: #O(n^3) El ciclo se ejecuta n veces n * n * n = n^3
		for element_b in list_b:
			for element_c in list_c: 	
				result_list.append(f'{element_a} {element_b} {element_c}') #O(1) Se agregan los elementos de las tres listas separados por un espacio
				
	return result_list #O(1) Retorna la lista 