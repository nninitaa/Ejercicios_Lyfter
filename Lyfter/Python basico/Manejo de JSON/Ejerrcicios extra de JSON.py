import json

def json_archive():
    try:
        with open('pokemon.json', 'r', encoding='utf-8') as archive:
            pokemon_list = json.load(archive)

        for pokemon in pokemon_list:
            name = pokemon.get('name', 'Unknown')
            type = pokemon.get('type', 'Unknown')
            level = pokemon.get('level', 'Unknown')

            print(f"Name: {name}")
            print(f"Type: {type}")
            print(f"Level: {level}")
            print("-" * 20)
    except FileNotFoundError:
        print("The file 'pokemon.json' does not exist.")     

json_archive()

def ask_type():
    try:
        with open('pokemon.json', 'r', encoding='utf-8') as archive:
            pokemon_list = json.load(archive)

        pokemon_type = input("Enter the type of Pokémon you want to search for: ")
        found_pokemon = [pokemon for pokemon in pokemon_list if pokemon.get('type', '').lower() == pokemon_type.lower()]

        if found_pokemon:
            print(f"Pokémon found with type '{pokemon_type}':")
            for pokemon in found_pokemon:
                name = pokemon.get('name', 'Unknown')
                level = pokemon.get('level', 'Unknown')
                print(f"Name: {name}, Level: {level}")
                print("-" * 20)
        else:
            print(f"No Pokémon of type '{pokemon_type}' found.")
    except FileNotFoundError:
        print("The file 'pokemon.json' does not exist.")

ask_type()

def principal_stadistics():
    try:
        with open('pokemon.json', 'r', encoding='utf-8') as archive:
            pokemon_list = json.load(archive)

        for pokemon in pokemon_list:
            name = pokemon.get('name', 'Unknown')
            stats = pokemon.get('stats', {})
            attack = stats.get('attack', 'Unknown')
            defense = stats.get('defense', 'Unknown')
            speed = stats.get('speed', 'Unknown')

            print(f"Name: {name}")
            print(f"Attack: {attack}")
            print(f"Defense: {defense}")
            print(f"Speed: {speed}")
            print("-" * 20)
    except FileNotFoundError:
        print("The file 'pokemon.json' does not exist.")

principal_stadistics()

def average_level():
    try:
        with open('pokemon.json', 'r', encoding='utf-8') as archive:
            pokemon_list = json.load(archive)

        type_dict = {}

        for pokemon in pokemon_list:
            type = pokemon.get('type', 'Unknown')
            level = pokemon.get('level', 0)
            if type not in type_dict:
                type_dict[type] = []
            type_dict[type].append(level)

        for type, levels in type_dict.items():
            average = sum(levels) / len(levels)
            print(f"Average level for type '{type}': {average:.2f}")
            print("-" * 20)

    except FileNotFoundError:
        print("The file 'pokemon.json' does not exist.")

average_level()