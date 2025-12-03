# La función filter() en Python sirve para filtrar elementos de una secuencia (lista, tupla, etc.) 
# dejando solo aquellos que cumplan una condición.

# Su estructura es:

# filter(función_condición, secuencia)

# función_condición: una función que recibe un elemento y devuelve True o False.
# secuencia: cualquier objeto iterable (lista, tupla, string, etc.).

#filter() devuelve un iterador, no una lista. Si quieres ver el resultado directamente, debes convertirlo a lista:

def es_par(n):
    return n % 2 == 0

numeros = [1, 2, 3, 4, 5, 6]

resultado = filter(es_par, numeros)

print(list(resultado))  # [2, 4, 6]
