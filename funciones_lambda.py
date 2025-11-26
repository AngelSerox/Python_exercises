# Una función lambda es una pequeña función anónima (sin nombre) de una sola expresión. 
# Son ideales para usarse como argumento key en funciones como sorted() o max() 
# porque permiten definir la lógica de extracción de la clave de forma concisa en una sola línea.

# Lista de estudiantes, donde cada elemento es una tupla (nombre, nota).
lista_estudiantes = [
    ('Edward', 4.2),
    ('Pepe', 2.5),
    ('Maria', 3.1),
    ('Carlos', 4.5)
]

# Ordena la lista utilizando la función sorted().
# La función lambda se encarga de extraer la clave de ordenamiento:
# key=lambda estudiante: estudiante[1] le indica a sorted() que use el elemento
# en el índice [1] (la nota) para comparar y ordenar las tuplas.
lista_ordenada = sorted(lista_estudiantes, key=lambda estudiante: estudiante[1])

# Imprime la lista ordenada por nota de menor a mayor.
# Salida esperada: [('Pepe', 2.5), ('Maria', 3.1), ('Edward', 4.2), ('Carlos', 4.5)]
print(lista_ordenada)
