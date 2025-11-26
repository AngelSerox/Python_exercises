def imprimir_nombre(primer_nombre,
                   segundo_nombre,
                   primer_apellido,
                   segundo_apellido):

    print(f"Hola {primer_nombre} {segundo_nombre} \
          {primer_apellido} {segundo_apellido} \
          bienvenido al curso de Python")

# Positional Arguments: Los argumentos se pasan en el orden en que se definen en la función.
# Los valores se asignan a los parámetros de la función basándose en su posición.
imprimir_nombre("Carlos", "Alberto", "Gomez", "Rojas")

# Keyword Arguments: Los argumentos se pasan utilizando el nombre del parámetro de la función,
# lo que permite pasarlos en cualquier orden.
imprimir_nombre(segundo_apellido="Rojas", primer_nombre="Carlos",
              primer_apellido="Gomez", segundo_nombre="Alberto")

# Mixed Arguments (Positional and Keyword): Se pueden combinar argumentos posicionales y de palabra clave.
# Los argumentos posicionales deben ir antes que los argumentos de palabra clave.
imprimir_nombre("Carlos", "Alberto", segundo_apellido="Rojas", primer_apellido="Gomez")

# Iterable Unpacking (usando *args): Si tienes una colección (como una tupla o lista) de argumentos
# y quieres pasarlos como argumentos posicionales, puedes usar el operador *.
# Esto "desempaqueta" el iterable y pasa sus elementos como argumentos individuales.
estudiante = ("Carlos", "Alberto", "Gomez", "Rojas")
imprimir_nombre(*estudiante)

# Dictionary Unpacking (usando **kwargs): Si tienes un diccionario donde las claves coinciden con
# los nombres de los parámetros de la función y los valores son los argumentos,
# puedes usar el operador ** para "desempaquetar" el diccionario y pasar los elementos
# como argumentos de palabra clave.
estudiante_dict = {
    'primer_apellido': 'Gomez',
    'primer_nombre': 'Carlos',
    'segundo_nombre': 'Alberto',
    'segundo_apellido': 'Rojas'
}

imprimir_nombre(**estudiante_dict)
