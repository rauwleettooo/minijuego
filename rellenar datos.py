import sqlite3
import tkinter as tk

def comenzar_juego():
    nombre = entry_titulo.get().strip()
    if nombre:
        cursor.execute("INSERT INTO jugadores (nombre, puntuacion) VALUES (?, ?)", (nombre, 0))
        conexion.commit()
        root.destroy()
        mostrar_pregunta(nombre)
    else:
        label_aviso.config(text="Introduzca un nombre, por favor")

def mostrar_pregunta(nombre):
    ventana_pregunta1 = tk.Tk()
    ventana_pregunta1.title("Pregunta 1")
    ventana_pregunta1.geometry("340x250")

    pregunta = "¿CAPITAL DE COLOMBIA?"
    opciones = {
        "a": "Medellín",
        "b": "Bogotá",
        "c": "Cali"
    }
    respuesta_correcta = "b"

    label_pregunta = tk.Label(ventana_pregunta1, text=pregunta, font=('consolas', 16))
    label_pregunta.pack(pady=10)

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre,))
            conexion.commit()
        ventana_pregunta1.destroy()
        mostrar_pregunta2(nombre)
        

    for clave, texto in opciones.items():
        boton = tk.Button(ventana_pregunta1, text=f"{clave}) {texto}",
                          font=('consolas', 10), width=16, height=2,
                          command=lambda c=clave: responder(c))
        boton.pack(pady=5)

def mostrar_pregunta2(nombre):
    ventana_pregunta2 = tk.Tk()
    ventana_pregunta2.title("Pregunta 2")
    ventana_pregunta2.geometry("400x260")

    pregunta = "¿EN QUE AÑO SE DESCUBRIÓ AMÉRICA?"
    opciones = {
        "a": "1592",
        "b": "1492",
        "c": "1491"
    }
    respuesta_correcta = "b"

    label_pregunta = tk.Label(ventana_pregunta2, text=pregunta, font=('consolas', 16))
    label_pregunta.pack(pady=10)

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre,))
            conexion.commit()
        ventana_pregunta2.destroy()
        mostrar_pregunta3(nombre)
        

    for clave, texto in opciones.items():
        boton = tk.Button(ventana_pregunta2, text=f"{clave}) {texto}",
                          font=('consolas', 10), width=16, height=2,
                          command=lambda c=clave: responder(c))
        boton.pack(pady=5)

def mostrar_pregunta3(nombre):
    ventana_pregunta3 = tk.Tk()
    ventana_pregunta3.title("Pregunta 3")
    ventana_pregunta3.geometry("400x260")

    pregunta = "¿EN QUE FECHA MURIÓ FRANCO?"
    opciones = {
        "a": "20 de Noviembre de 1975",
        "b": "20 de Octubre de 1975",
        "c": "16 de Noviembre de 1975"
    }
    respuesta_correcta = "a"

    label_pregunta = tk.Label(ventana_pregunta3, text=pregunta, font=('consolas', 16))
    label_pregunta.pack(pady=10)

    def responder(eleccion):
        if eleccion == respuesta_correcta:
            label_aviso = tk.Label(ventana_pregunta3, text="Correcto", font=('consolas', 10))
            label_aviso.pack(pady=10)
            cursor.execute("UPDATE jugadores SET puntuacion = puntuacion + 10 WHERE nombre = ?", (nombre,))
            conexion.commit()
        ventana_pregunta3.destroy()
        mostrar_resultado(nombre)

    for clave, texto in opciones.items():
        boton = tk.Button(ventana_pregunta3, text=f"{clave}) {texto}",
                          font=('consolas', 10), width=30, height=2,
                          command=lambda c=clave: responder(c))
        boton.pack(pady=5)

        
def mostrar_resultado(nombre):
    resultado = tk.Tk()
    resultado.title("Resultado Final")
    resultado.geometry("400x350")

    # Mostrar la puntuación final 
    cursor.execute("SELECT puntuacion FROM jugadores WHERE nombre = ?", (nombre,))
    puntuacion = cursor.fetchone()[0]

    mensaje = f"{nombre}, tu puntuación final es: {puntuacion} puntos"
    label = tk.Label(resultado, text=mensaje, font=('consolas', 12))
    label.pack(pady=10)

    # Ranking general
    label_ranking = tk.Label(resultado, text="Ranking de Jugadores", font=('consolas', 12, 'bold'))
    label_ranking.pack(pady=5)

    encabezado = tk.Label(resultado, text="Jugador Puntos", font=('consolas', 10, 'bold'))
    encabezado.pack()

    # Mostrar todos los jugadores ordenados por puntuación
    cursor.execute("SELECT nombre, puntuacion FROM jugadores ORDER BY puntuacion DESC")
    jugadores = cursor.fetchall()

    for jugador, puntos in jugadores:
        fila = tk.Label(resultado, text=f"{jugador} - {puntos}", font=('consolas', 10))
        fila.pack()

    tk.Button(resultado, text="Cerrar", command=resultado.destroy).pack(pady=10)

    

# Conexión a la base de datos
conexion = sqlite3.connect('jugadores.db')
cursor = conexion.cursor()

# Crear tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS jugadores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        puntuacion INTEGER DEFAULT 0
    )
''')
conexion.commit()

# Ventana principal
root = tk.Tk()
root.title("LOG-IN DEL JUEGO")
root.geometry("340x180")

label_titulo = tk.Label(root, text="Introduce tu nombre", font=('consolas', 16))
label_titulo.pack(pady=10)

entry_titulo = tk.Entry(root, font=('consolas', 14))
entry_titulo.pack(pady=10)

boton_titulo = tk.Button(root, text="Comenzar", font=('consolas', 10), command=comenzar_juego)
boton_titulo.pack(pady=10)

label_aviso = tk.Label(root, text="", font=('consolas', 10))
label_aviso.pack(pady=10)

root.mainloop()

#VAYA GITANOOOOOOOOOO