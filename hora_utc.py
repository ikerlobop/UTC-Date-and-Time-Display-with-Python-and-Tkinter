# Versión: 1.0
# Autor: Iker Lobo Pérez
# Fecha: 18/07/2023
# Descripción: Programa que muestra la hora y fecha actuales en UTC

# Importamos la librería tkinter y datetime, timezone
import tkinter as tk
from datetime import datetime, timezone


# Función que actualiza la hora y fecha
def actualiza_hora(etiqueta):
    
    # ActualizaMOS la etiqueta con la hora y fecha actuales en UTC
    hora_actual_utc = datetime.now(timezone.utc)
    fecha_actual_utc = datetime.now(timezone.utc)

    # Formateamos la fecha y hora
    fecha_formateada = fecha_actual_utc.strftime(" %Y-%m-%d UTC")
    hora_formateada = hora_actual_utc.strftime(" %H:%M:%S UTC")

    # Actualizamos la etiqueta
    etiqueta["text"] = "Hora:" + hora_formateada + "\n" + "Fecha:" + fecha_formateada
    ventana.after(1000, lambda: actualiza_hora(etiqueta))

# Función que crea la interfaz
def crear_interfaz():
    ventana = tk.Tk()
    ventana.title("Tiempo UTC")
    ventana.geometry("300x100")

    etiqueta_hora = tk.Label(ventana, font=("Arial", 16), pady=20, justify="left")
    etiqueta_hora.pack()

    return ventana, etiqueta_hora

# Creamos la ventana y la etiqueta
ventana, etiqueta_hora = crear_interfaz()
actualiza_hora(etiqueta_hora)

# Bucle principal
ventana.mainloop()

