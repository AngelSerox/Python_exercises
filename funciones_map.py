# La función map() en Python es una herramienta de programación funcional que te permite 
# aplicar una función a cada elemento de un objeto iterable (como una lista, tupla o conjunto) 
# de manera eficiente.
def cuadrado(numero):
    return numero * numero

numeros = [1, 2, 3, 4, 5]

# Aplicar la función 'cuadrado' a cada elemento de 'numeros'
resultado_map = map(cuadrado, numeros)

# Convertir el objeto map a una lista para ver el resultado
lista_resultado = list(resultado_map)

print(lista_resultado)  # [1, 4, 9, 16, 25]
