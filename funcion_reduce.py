# La función reduce() sirve para reducir (combinar) todos los elementos de un iterable en un solo valor aplicando una función acumulativa.

# Está en el módulo functools, así que primero debes importarla:
" from functools import reduce "

# ¿Cómo funciona?

" reduce(función, iterable, valor_inicial?) "
# función: recibe dos valores → un acumulador y el siguiente elemento.
# iterable: lista, tupla, etc.

" valor_inicial (opcional): valor con el que comienza el acumulador. " 
# La función se aplica así:

" (((a1 ⊕ a2) ⊕ a3) ⊕ a4) ... "
# Donde ⊕ es la operación de tu función.

# Ejemplo 1: sumar todos los números.
from functools import reduce
nums = [1, 2, 3, 4]

resultado = reduce(lambda a, b: a + b, nums)

print(resultado)  
# 10

# Ejemplo 2: concatenar strings.
Concatenar strings
palabras = ["Hola", " ", "mundo"]

frase = reduce(lambda a, b: a + b, palabras)

print(frase)
# Hola mundo 
