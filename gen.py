import json
import random

data = [
    {
        "precio": 182,
        "distancia": 200000,
        "nombre": "chorrillos",
        "id": 1
    }
]

# Crear una lista aleatoria con los datos proporcionados
lista_aleatoria = []
for _ in range(10):  # Generar 10 elementos aleatorios
    random_element = {
        "precio": random.randint(100, 300),
        "distancia": random.randint(100000, 300000),
        "nombre": random.choice(['chorrillos', 'miraflores', 'san isidro', 'barranco']),
        "id": random.randint(1, 100)
    }
    lista_aleatoria.append(random_element)

# Escribir la lista en formato JSON en un archivo
with open("lugares.json", "w", encoding="utf-8") as file:
    json.dump(lista_aleatoria, file, indent=4, ensure_ascii=False)
