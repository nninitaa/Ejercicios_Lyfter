#1. Cree un diccionario que guarde la siguiente información sobre un hotel:
hotel_information = {
    'name': 'Marriott',
    'number_of_stars': 5,
    'rooms': [
        {
            'number': 101,
            'floor': 300,
            'price_per_night': 100
        },
        {
            'number': 102,
            'floor': 400,
            'price_per_night': 150
        }
    ]
}
print(hotel_information)

#2. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
keys = ['first_name', 'last_name', 'role', 'email']
values = ['Irina', 'Araya', 'Student', 'irina.araya@example.com']

user = {}

for i in range(len(keys)):
    user[keys[i]] = values[i]

for k, v in user.items():
    print(f"{k}: {v}")

#3. Cree un programa que use una lista para eliminar keys de un diccionario.
data = {
    "name": "Irina",
    "age": 17,
    "city": "Cartago",
    "course": "Programming",
    "email": "irina.araya@example.com"
}

keys_to_remove = ["course"]

for key in keys_to_remove:
    removed_value = data.pop(key)
    print(f"Deleted data: {removed_value}")

print(data)