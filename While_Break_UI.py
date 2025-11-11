import random   # Se importa el módulo 'random' para generar números aleatorios (avances de las tortugas)
import turtle   # Se importa el módulo 'turtle' para crear gráficos y animaciones con tortugas

# --- CONFIGURACIÓN DE LA VENTANA ---
ventana = turtle.Screen()        # Crea una ventana o lienzo donde se mostrará la carrera
ventana.title("Carrera de Caracoles")   # Establece el título de la ventana
ventana.bgcolor("lightblue")     # Cambia el color de fondo de la ventana
ventana.setup(width=800, height=600)  # Define el tamaño de la ventana (ancho y alto en píxeles)

# --- CREACIÓN DE LA TORTUGA 1 ---
Tortuga_1 = turtle.Turtle()      # Crea un objeto tortuga que se podrá mover en la pantalla
Tortuga_1.shape("turtle")        # Cambia la forma del puntero para que parezca una tortuga
Tortuga_1.color("red")           # Asigna el color rojo a la tortuga
Tortuga_1.penup()                # Levanta el lápiz para que no deje una línea al moverse
Tortuga_1.goto(-300, 100)        # Coloca a la tortuga en la posición inicial (x = -300, y = 100)

# --- CREACIÓN DE LA TORTUGA 2 ---
Tortuga_2 = turtle.Turtle()      # Crea la segunda tortuga
Tortuga_2.shape("turtle")        # También con forma de tortuga
Tortuga_2.color("blue")          # Color azul
Tortuga_2.penup()                # Levanta el lápiz (no dibuja líneas)
Tortuga_2.goto(-300, -100)       # Posición inicial diferente para que no se encimen

# --- META DE LA CARRERA ---
meta = 300   # La coordenada X que deben alcanzar para ganar (cuanto más grande, más larga la carrera)

# --- INICIO DE LA CARRERA ---
while True:
    # Cada tortuga avanza una distancia aleatoria entre 1 y 20 píxeles
    avance_tortuga_1 = random.randint(1, 20)
    avance_tortuga_2 = random.randint(1, 20)

    # Se mueven hacia adelante la cantidad indicada
    Tortuga_1.forward(avance_tortuga_1)
    Tortuga_2.forward(avance_tortuga_2)

    # Se imprime en la consola el avance de cada tortuga
    print(f"La tortuga 1 avanzó {avance_tortuga_1} pasos, para un total de: {Tortuga_1.xcor()} píxeles.")
    print(f"La tortuga 2 avanzó {avance_tortuga_2} pasos, para un total de: {Tortuga_2.xcor()} píxeles.")
    print("-----------------------------------------------------------")
    
    # Condición para terminar la carrera:
    # Si alguna tortuga llega o supera la meta (posición x >= 300), se rompe el bucle
    if Tortuga_1.xcor() >= meta or Tortuga_2.xcor() >= meta:
        break

# --- RESULTADO FINAL ---
# Se comparan las posiciones finales (coordenadas x) de las tortugas para determinar el ganador
if Tortuga_1.xcor() > Tortuga_2.xcor():
    print("🏁 La tortuga 1 es la ganadora 🐢 (roja)")
elif Tortuga_2.xcor() > Tortuga_1.xcor():
    print("🏁 La tortuga 2 es la ganadora 🐢 (azul)")
else:
    print("🤝 Esto es un empate")

# --- CIERRE DE LA VENTANA ---
ventana.exitonclick()   # Mantiene la ventana abierta hasta que el usuario haga clic en ella
