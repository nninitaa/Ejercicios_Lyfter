import csv

def videogames():
    with open('videogames.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Genre', 'Developer', 'Rating'])

        writer.writerow(['Sonic Colors', 'Platform', 'Sega', 'E10+'])
        writer.writerow(['Mario Kart 8 Deluxe', 'Racing', 'Nintendo', 'E'])
        writer.writerow(['Animal Crossing: New Horizons', 'Simulation', 'Nintendo', 'E'])
        writer.writerow(['The Sims 4', 'Simulation', 'Maxis', 'T'])

        n = int(input("How many videogames do you want to add? "))

        for i in range(n):
            print(f"Videogame {i+1}:")
            name = input("Videogame name: ")
            genre = input("Videogame genre: ")
            developer = input("Videogame developer: ")
            rating = input("ESRB rating: ")

            writer.writerow([name, genre, developer, rating])

    print("Videogames successfully added to the CSV file!")

videogames()


import csv

def videogames():
    with open('videogames.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter='\t')
        writer.writerow(['Name', 'Genre', 'Developer', 'Rating'])
        writer.writerow(['Sonic Colors', 'Platform', 'Sega', 'E10+'])
        writer.writerow(['Mario Kart 8 Deluxe', 'Racing', 'Nintendo', 'E'])
        writer.writerow(['Animal Crossing: New Horizons', 'Simulation', 'Nintendo', 'E'])
        writer.writerow(['The Sims 4', 'Simulation', 'Maxis', 'T'])

    n = int(input("How many videogames do you want to add? "))

    for i in range(n):
        print(f"\nVideogame {i+1}:")
        name = input("Videogame name: ")
        genre = input("Videogame genre: ")
        developer = input("Videogame developer: ")
        rating = input("ESRB rating: ")
        with open('videogames.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file, delimiter='\t')
            writer.writerow([name, genre, developer, rating])

    print("Videogames successfully added to the CSV file!")

videogames()
