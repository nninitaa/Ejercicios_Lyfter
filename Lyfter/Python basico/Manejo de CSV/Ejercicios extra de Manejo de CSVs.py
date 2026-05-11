import csv 
def videojuegos():
    with open('videojuegos.csv', 'r') as archive:
        reader = csv.reader(archive)
        for row in reader:
            print('Name:', row[0])
            print('Genre:', row[1])
            print('Developer:', row[2])
            print('Rating:', row[3])
            print('---------------------------------')

videojuegos()

# Filtrar por clasificación ESRB
import csv
rating_find = input("Ingrese la clasificación ESRB para filtrar los videojuegos: ").strip().upper()
def filter_by_rating(clasificacion):
    with open('videojuegos.csv', 'r') as archive:
        reader = csv.reader(archive)
        for row in reader:
            if row[3] == rating_find:
                print('Name:', row[0])
                print('Genre:', row[1])
                print('Developer:', row[2])
                print('Rating:', row[3])
                print('---------------------------------')

filter_by_rating()

# Total videojuegos por genero
import csv
def count_videogames_by_genre(genre):
    results = {}
    with open('videojuegos.csv', 'r', encoding='utf-8') as archive:
        reader = csv.reader(archive)
        next(reader)
        for row in reader:
            if row[3] == genre:
                results.append(row)
    return results

clasification = input("Ingrese la clasificación ESRB para contar los videojuegos por género: ").strip().upper()
videogames_by_genre = count_videogames_by_genre(clasification)
print(f"Total de videojuegos con clasificación {clasification}: {len(videogames_by_genre)}")

if videogames_by_genre:
    for game in videogames_by_genre:
        print('Name:', game[0])
        print('Genre:', game[1])
        print('Developer:', game[2])
        print('Rating:', game[3])
        print('---------------------------------')
    else:
        print(f"No se encontraron videojuegos con clasificación {clasification}.")

# Total videojuegos por desarrollador
import csv  
def count_videogames_by_developer():
    counter = {}
    with open('videojuegos.csv', 'r', encoding='utf-8') as archive:
        reader = csv.reader(archive)

        next(reader)
    # Saltar la fila de encabezado
        for row in reader:
            developer = row[2] 

            if developer in counter:
                counter[developer] += 1
            else:
                counter[developer] = 1
    return counter

print("Total de videojuegos por desarrollador:\n")
for developer in sorted(count_videogames_by_developer().keys()):
    amount = count_videogames_by_developer()[developer]
    print(f"{developer}: {amount}")

count_videogames_by_developer()
