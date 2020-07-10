#Tkinter
#Módulo para crear interfaces gráficas de usuario

from tkinter import *

#Creamos la ventana raiz
ventana = Tk() #Creamos un objeto

#Ajustar el título de la ventana
ventana.title("Interfaz gráfica con Python (por LC)")

#Cargamos el "favicon"
ventana.iconbitmap("./imagenes/alarm.ico")

#Ajustar el tamaño de la ventana
ventana.geometry("750x400")

#Bloquear el tamaño de la ventana
ventana.resizable(0, 0)

#Arrancar y mostrar la ventana hasta que se cierre
ventana.mainloop()