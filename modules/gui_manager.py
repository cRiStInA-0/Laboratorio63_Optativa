import tkinter as tk
# Tkinter es la librería estándar de Python para GUI
# ============================================================
# FUNCIÓN PRINCIPAL: CREAR VENTANA GRÁFICA
# ============================================================
def crear_ventana():

 # ============================================================
 # CREAR VENTANA PRINCIPAL
 # ============================================================

 ventana = tk.Tk() # Crea la ventana raíz principal de Tkinter
 ventana.title("Panel de control - Sensores") # Título que aparece en la barra de ventana
 ventana.geometry("400x500") # Tamaño de la ventana
 ventana.config(bg="#1e1e1e") # Fondo oscuro

 # ============================================================
 # CREAR TÍTULO PRINCIPAL
 # ============================================================
 titulo = tk.Label(ventana, text="CONTROL POR VOZ - ESTADO Y SENSORES", #Texto
    font=("Arial", 16, "bold"), bg="#1e1e1e", fg="#00ffcc") #Fuente y color tanto de fondo como de texto
 titulo.pack(pady=10) #Margen

 # ============================================================
 # CREAR CANVAS (LIENZO) PARA LOS SENSORES
 # ============================================================

 # Canvas es como un "papel en blanco" donde podemos dibujar formas
 canvas = tk.Canvas(ventana, width=400, height=150, bg="#111", highlightthickness=0)
 canvas.pack(pady=20) #Posicionar el canvas en la ventana y ajustar el margen

 # ============================================================
 # DIBUJAR LUCES DE LOS SENSORES EN EL CANVAS
 # ============================================================

 # Crear etiquetas para cada sensor
 canvas.create_text(75, 15, text="Temperatura", fill="white", font=("Arial", 10, "bold"))
 canvas.create_text(195, 15, text="Proximidad", fill="white", font=("Arial", 10, "bold"))
 canvas.create_text(315, 15, text="Energía", fill="white", font=("Arial", 10, "bold"))

 # Crear luces redondas (óvalos) apagadas inicialmente (grey20) para los sensores
 temperatura = canvas.create_oval(25, 30, 125, 130, fill="grey20") 
 proximidad = canvas.create_oval(145, 30, 245, 130, fill="grey20")
 energia = canvas.create_oval(265, 30, 365, 130, fill="grey20")

 # ============================================================
 # CREAR ETIQUETA DE INSTRUCCIONES
 # ============================================================

 # Label de instrucciones
 texto_label = tk.Label(ventana, text="Pulsa '🎤 Escuchar' y da un comando.", 
    font=("Arial", 12), bg="#1e1e1e", fg="white") #Fuente y color tanto de fondo como de texto
 texto_label.pack(pady=10) #Margen

 # ============================================================
 # CREAR ETIQUETA DE RESULTADO
 # ============================================================

 # Label para mostrar resultados de reconocimiento
 resultado_label = tk.Label(ventana, text="...", 
    font=("Arial", 14, "bold"), bg="#1e1e1e", fg="#00ffcc") #Fuente y color tanto de fondo como de texto
 resultado_label.pack(pady=10) #Margen

 # ============================================================
 # RETORNAR TODOS LOS WIDGETS
 # ============================================================

 # Retorna una tupla con todos los widgets que main.py necesita
 # en el orden: ventana principal, canvas, y IDs de las 3 luces,
 # más las etiquetas de texto y resultado
 return ventana, canvas, temperatura, proximidad, energia, texto_label, resultado_label