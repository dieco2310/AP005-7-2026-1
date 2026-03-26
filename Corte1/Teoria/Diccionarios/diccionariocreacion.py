############## DICCIONARIOS BÁSICOS ##############

# Diccionarios con pares clave-valor
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Mostrar contenido
print(sensors)
print(num_cameras)

# Diccionario con strings como claves y valores
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)

# NOTA: listas no pueden ser claves (porque son mutables)
# powers = {[1,2,4]:2}  # Esto generaría error

# Pero sí pueden ser valores
children = {
    "von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
    "Corleone": ["Sonny", "Fredo", "Michael"]
}
print(children)

# Diccionario vacío
my_empty_dictionary = {}
print(my_empty_dictionary)

# Añadir elemento
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Antes:", menu)

menu["cheesecake"] = 8
print("Después:", menu)

# Sobrescritura completa
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)

# Agregar múltiples elementos
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Antes:", sensors)

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("Después:", sensors)

user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)

user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

# Modificar valores existentes
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Antes:", menu)

menu["oatmeal"] = 5
print("Después:", menu)

oscar_winners = {
    "Best Picture": "La La Land",
    "Best Actor": "Casey Affleck",
    "Best Actress": "Emma Stone",
    "Animated Feature": "Zootopia"
}

print("Antes:", oscar_winners)

oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("Cambio 1:", oscar_winners)

oscar_winners["Best Picture"] = "Moonlight"
print("Cambio 2:", oscar_winners)

# Comprensión de diccionarios
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

students = {k: v for k, v in zip(names, heights)}
print(students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

pares = zip(drinks, caffeine)
print(pares)

drinks_to_caffeine = {k: v for k, v in pares}
print(drinks_to_caffeine)

songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {k: v for k, v in zip(songs, playcounts)}
print(plays)

plays.update({"Purple Haze": 1})
plays.update({"Respect": 94})
print("Actualizado:", plays)

# Diccionario dentro de otro diccionario
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)