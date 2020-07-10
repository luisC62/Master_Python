#Marcos o frames
from tkinter import *

#Forma de establecer el lay-out de la aplicación

ventana = Tk()
ventana.title("Marcos (frames) | Master en Python")
ventana.geometry("700x700")

marco_padre = Frame(ventana, width = 250, height = 250)
marco_padre.config(bg = "lightblue", bd = 12, relief = "raised")
marco_padre.pack(side = BOTTOM, fill = X, expand = YES, anchor = S)

marco = Frame(marco_padre, width = 250, height = 250)
marco.config(bg = "red", bd = 12, relief = "raised")
marco.pack(side = RIGHT)
marco.pack_propagate(FALSE)

texto = Label(marco, text="Rojo")
texto.config(bg = "red", font = ("Arial, 20"))
texto.pack(side = RIGHT, anchor = CENTER)

marco = Frame(marco_padre, width = 250, height = 250)
marco.config(bg = "green", bd = 12, relief = "raised")
marco.pack(side = LEFT, anchor = SW)
marco.pack_propagate(FALSE)

texto = Label(marco, text="Verde")
texto.config(bg = "green", font = ("Arial, 20"))
texto.pack(side = LEFT, anchor = CENTER)

marco_padre = Frame(ventana, width = 250, height = 250)
marco_padre.config(bg = "lightblue", bd = 12, relief = "raised")
marco_padre.pack(side = TOP, fill = X, expand = YES, anchor = N)

marco = Frame(marco_padre, width = 250, height = 250)
marco.config(bg = "blue", bd = 12, relief = "raised")
marco.pack(side = LEFT)
marco.pack_propagate(FALSE)

texto = Label(marco, text="Azul")
texto.config(bg = "blue", font = ("Arial, 20"))
texto.pack(side = RIGHT, anchor = CENTER)

marco = Frame(marco_padre, width = 250, height = 250)
marco.config(bg = "orange", bd = 12, relief = "raised")
marco.pack(side = RIGHT)
marco.pack_propagate(FALSE)

texto = Label(marco, text="Naranja")
texto.config(bg = "orange", font = ("Arial, 20"))
texto.pack(side = LEFT, anchor = CENTER)
ventana.mainloop()