def configurar_perfil(nombre, tema='claro', notificaciones=True, idioma='es'):
    
    #Configura las preferencias de un perfil de usuario.

    #:param nombre: Nombre del usuario (obligatorio).
    #:param tema: Tema de la interfaz ('claro' o 'oscuro'). Valor por defecto es 'claro'.
    #:param notificaciones: Si se reciben notificaciones. Valor por defecto es True.
    #:param idioma: Idioma de la interfaz. Valor por defecto es 'es'.
    
    print(f"--- Configuración para {nombre} ---")
    print(f"Tema seleccionado: {tema}")
    print(f"Notificaciones activadas: {notificaciones}")
    print(f"Idioma de la interfaz: {idioma}")
    print("-" * 25)

# 1. Uso Básico y Flexibilidad del Orden
# Podemos pasar los argumentos en cualquier orden siempre que usemos el nombre del parámetro (keyword).
print("Ejemplo 1: Cambiando el orden con Keyword Arguments")
configurar_perfil(
    notificaciones=False,
    tema='oscuro',
    nombre='Ana',
    idioma='en'
)

# 2. Argumentos con Valores por Defecto (Mixing Default and Keyword)
# Podemos omitir los parámetros que tienen un valor por defecto y Python usará ese valor.
# Solo pasamos los que queremos cambiar o el obligatorio.
print("Ejemplo 2: Usando valores por defecto (omitiendo 'tema' e 'idioma')")
configurar_perfil(
    nombre='Beto',
    notificaciones=False  # Solo cambiamos 'notificaciones'
)

# 3. Combinación de Posicionales y Palabra Clave
# Se pueden combinar ambos, pero los argumentos posicionales deben ir PRIMERO.
print("Ejemplo 3: Combinando Posicional y Keyword")
# 'Carlos' se asigna por posición a 'nombre'
# 'idioma' y 'tema' se asignan por palabra clave
configurar_perfil('Carlos', idioma='fr', tema='oscuro')

# ESTO DARÍA UN ERROR (SyntaxError): Los Keyword Arguments deben seguir a los Positional Arguments
# configurar_perfil(tema='oscuro', 'David')
