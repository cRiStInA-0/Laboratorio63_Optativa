from tkinter import messagebox #Para mostrar el mensaje de alerta


def procesar_comando(text, canvas, sensores, resultado_label, ventana):

 temperatura, proximidad, energia = sensores
 text = text.lower() # Convertimos a minúsculas para evitar errores

 #Funciones if que busca similitud entre el texto y los "comandos"
 if "activar" in text and "robot" in text:
    #Se modifica el color de los canvas y la etiqueta
    canvas.itemconfig(temperatura, fill="green")
    canvas.itemconfig(proximidad, fill="green")
    canvas.itemconfig(energia, fill="green")
    resultado_label.config(text="🤖 Robot activado") 

 elif "temperatura" in text and "alta" in text:
    #Primero se comprueba que los sensores se encuentren encendidos
    if canvas.itemcget(temperatura, "fill") == "green":
      #Se modifica el color de los canvas y la etiqueta
      canvas.itemconfig(temperatura, fill="red")
      canvas.itemconfig(proximidad, fill="green")
      canvas.itemconfig(energia, fill="green")
      resultado_label.config(text="🌡️ La temperatura ha sido ajustada") 
      #Se muestra la alerta por temperatura demasiado elevada
      messagebox.showwarning("¡¡Alerta!!", "Temperatura elevada")
    else:
      resultado_label.config(text="El robot debe estar activo para continuar")

 elif "revisar" in text and "sensores" in text:
      #Se modifica la etiqueta
      resultado_label.config(text=estado_sensores(canvas.itemcget(temperatura, "fill"), canvas.itemcget(proximidad, "fill"), canvas.itemcget(energia, "fill")))

 elif "detener" in text and "robot" in text:
    #Se modifica el color de los canvas y la etiqueta
    canvas.itemconfig(temperatura, fill="grey20")
    canvas.itemconfig(proximidad, fill="grey20")
    canvas.itemconfig(energia, fill="grey20")
    resultado_label.config(text="💤 Robot desactivado") 

 elif "salir" in text:
    #Se modifica la etiqueta y se cierra la ventana
    resultado_label.config(text="👋 Cerrando programa...") 
    ventana.after(1000, ventana.destroy)
    
 else:
    #Se modifica la etiqueta
    resultado_label.config(text=" Comando no reconocido")


def estado_sensores(estadoTemp, estadoProx, estadoEnergia):
   """
   Comprueba el estado actual de los sensores y, en función del resultado
   devuelve un mensaje u otro
   """
   mensaje="Revisando sensores...\n"

   if estadoTemp=="grey20" and estadoProx=="grey20" and estadoEnergia=="grey20":
      mensaje+="Los sensores se encuentran actualmente apagados"
   elif estadoTemp=="green" and estadoProx=="green" and estadoEnergia=="green":
      mensaje+="Temperatura: Ambiental\nProximidad: No se ha encontrado ningún objeto\nEnergía: Estable"
   elif estadoTemp=="red" and estadoProx=="green" and estadoEnergia=="green":
      mensaje+="Temperatura: Demasiado alta (alerta)\nProximidad: No se ha encontrado ningún objeto\nEnergía: Estable"
   
   return mensaje