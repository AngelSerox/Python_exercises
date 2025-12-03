# La función sorted() sirve para ordenar cualquier iterable (listas, tuplas, strings, sets, etc.) y devuelve una nueva lista ordenada, sin modificar el original.

# Sintaxis:
# sorted(iterable, *, key=None, reverse=False)

#Parámetros:
  # iterable → la colección que quieres ordenar.
  # key → una función que define cómo se debe ordenar.
  # reverse → si es True, ordena de mayor a menor.

# Ejemplos básicos
# Ordenar una lista de números:
nums = [5, 1, 9, 3]
print(sorted(nums))  
# [1, 3, 5, 9]

# Ordenar de mayor a menor:
print(sorted(nums, reverse=True))
# [9, 5, 3, 1]

# Uso del parámetro key

# Aquí es donde se vuelve poderosa.

# Ordenar por longitud
palabras = ["python", "sol", "programar", "hola"]

print(sorted(palabras, key=len))
# ['sol', 'hola', 'python', 'programar']

# Ordenar ignorando mayúsculas/minúsculas
nombres = ["Juan", "ana", "Pedro", "maria"]

print(sorted(nombres, key=str.lower))
# ['ana', 'Juan', 'maria', 'Pedro']

# Ordenar listas de diccionarios
#Muy común al manejar datos.

personas = [
    {"nombre": "Ana", "edad": 22},
    {"nombre": "Luis", "edad": 30},
    {"nombre": "Sofía", "edad": 25}
]

print(sorted(personas, key=lambda p: p["edad"]))
"""[
 {'nombre': 'Ana', 'edad': 22},
 {'nombre': 'Sofía', 'edad': 25},
 {'nombre': 'Luis', 'edad': 30}
]"""
