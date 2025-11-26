# Función para calcular el precio total aplicando descuentos e impuestos.
# Utiliza *args para manejar una cantidad variable de precios de productos
# y **kwargs para manejar opciones variables como el descuento y el impuesto.
def calcular_precio_total(*args, **kwargs):
    # 1. Suma todos los argumentos posicionales (*args) para obtener el subtotal.
    # En este caso, *args contiene los precios de los productos.
    precio_total = sum(args)

    # 2. Obtiene el descuento y el impuesto del diccionario de argumentos de palabra clave (**kwargs).
    # Se usa .get(clave, valor_por_defecto) para que la función no falle si
    # 'descuento' o 'impuesto' no están presentes; en ese caso, se usa 0.
    descuento = kwargs.get('descuento', 0)
    impuesto = kwargs.get('impuesto', 0)

    # 3. Aplica el descuento. Se resta el monto del descuento del precio_total.
    # El 20% de descuento se calcula como: precio_total * 0.2
    precio_total -= precio_total * descuento

    # 4. Aplica el impuesto. Se suma el monto del impuesto al precio_total ya descontado.
    # El 1% de impuesto se calcula como: precio_total * 0.01
    precio_total += (precio_total * impuesto)

    # 5. Devuelve el precio final.
    return precio_total

# Datos de entrada para la función:

# Lista de precios individuales de los productos. Se desempaquetará en *args.
lista_productos = [100, 65, 30]

# Diccionario con las opciones de descuento (0.2 = 20%) e impuesto (0.01 = 1%).
# Se desempaquetará en **kwargs.
dict_opcionales = {
    'descuento': 0.2,
    'impuesto': 0.01
}

# Llamada a la función utilizando los operadores de desempaquetado:
# - *lista_productos: Pasa 100, 65, 30 como argumentos posicionales separados a *args.
# - **dict_opcionales: Pasa 'descuento'=0.2 e 'impuesto'=0.01 como argumentos de palabra clave a **kwargs.
precio_final = calcular_precio_total(*lista_productos, **dict_opcionales)

# Muestra el resultado final (157.56)
print(precio_final)
