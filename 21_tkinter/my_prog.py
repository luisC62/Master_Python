from tkinter import *

class Programa:
    def __init__(self): #Constructor
        self.title = "Mi título de ventana"
        self.icono = "./imagenes/alarm.ico"
        self.size = "750x400"
        self.ventana = Tk() #Creamos la ventana raiz
        
    def cargar(self):  #Método para cargar el programa
        
        #Ajustar el título de la ventana
        self.ventana.title(self.title)
        #Cargamos el "favicon"
        self.ventana.iconbitmap(self.icono)
        #Ajustar el tamaño de la ventana
        self.ventana.geometry(self.size)
        #Bloquear el tamaño de la ventana
        self.ventana.resizable(0, 0)
        
    def addTexto(self, texto):
        etiqueta = Label(self.ventana, text=texto)
        etiqueta.pack()

    def mostrar(self): #Metodo para mostrar la ventana
        #Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()