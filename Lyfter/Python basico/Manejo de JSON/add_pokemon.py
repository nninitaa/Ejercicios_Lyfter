import json

def load_pokemon_data():
    try:
        with open('pokemon.json', 'r', encoding='utf-8') as archive:
            pokemon_data = json.load(archive)
    except FileNotFoundError:
        pokemon_data = []
    return pokemon_data

def ask_pokemon_details():
    name = input("Enter the name of the Pokémon: ")
    type = input("Enter the type of the Pokémon: ")
    level = input("Enter the level of the Pokémon: ")
    return {
        "name": name,
        "type": type,
        "level": level
    }

def save_pokemon(pokemon_data):
    with open('pokemon.json', 'w', encoding='utf-8') as archive:
        json.dump(pokemon_data, archive, indent=4)

def main():
    pokemon_data = load_pokemon_data()
    new_pokemon = ask_pokemon_details()
    pokemon_data.append(new_pokemon)
    save_pokemon(pokemon_data)  
    print(f"Pokémon '{new_pokemon['name']}' added successfully!")

main()