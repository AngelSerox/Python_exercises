# Importa la librería 'turtle', que proporciona una forma sencilla de dibujar
# gráficos en pantalla usando una "tortuga" virtual.
import turtle 

# Crea la ventana gráfica (screen) donde se realizarán los dibujos.
# 'ventana' es el objeto principal para la configuración del lienzo.
ventana = turtle.Screen()

# Establece el color de fondo de la ventana gráfica a "white" (blanco).
ventana.bgcolor("white")

# Crea un nuevo objeto "tortuga" (turtle), que es el pincel o cursor que dibuja.
# Todas las acciones de dibujo se realizarán a través de este objeto.
tortuga = turtle.Turtle()

# Establece la velocidad de la tortuga. Los valores van de 1 (más lento) a 10 (más rápido),
# o 0 para la velocidad máxima (sin animación). Aquí se establece en una velocidad lenta (1) para observar el dibujo.
tortuga.speed(1)

# --- INICIO DEL DIBUJO ---

# Un bucle que se repite 4 veces. Esto es necesario para dibujar los 4 lados de un cuadrado.
# Se usa '_' como nombre de variable porque el valor del contador del bucle no se utiliza.
for _ in range(4):
    # Mueve la tortuga hacia adelante 100 unidades (píxeles). 
    # Deja un rastro, dibujando así un lado del cuadrado.
    tortuga.forward(100)
    
    # Gira la tortuga 90 grados a la derecha. Esto la prepara para dibujar el siguiente lado
    # en un ángulo de 90 grados respecto al lado anterior (esquina de un cuadrado).
    tortuga.right(90)

# --- FIN DEL DIBUJO ---

# Mantiene la ventana abierta hasta que el usuario hace clic con el ratón en ella.
# Esto evita que la ventana se cierre inmediatamente después de terminar el dibujo.
ventana.exitonclick()
