from tkinter import *

ventana = Tk()
ventana.geometry("500x400")
ventana.title("Formularios en Tkinter / Luis Cárceles")

#Utilizaremos el GRID

#Encabezado del formulario
encabezado = Label(ventana, text = "Formularios con Tkinter - Luis Cárceles")
encabezado.config(
    fg = "white",
    bg = "darkgray",
    font = ("Open Sans", 18),
    padx = 10,
    pady = 10
)
encabezado.grid(row = 0, column = 0, columnspan = 12, padx = 5, pady = 5, sticky = W)

#Etiqueta del campo de texto (Nombre)
label = Label(ventana, text = "Nombre")
label.grid(row = 1, column = 0, sticky = W, padx = 5, pady = 5)

#Campo de texto (Nombre)
campo_texto = Entry(ventana)
campo_texto.grid(row = 1, column = 1, sticky = W, padx = 5, pady = 5)
campo_texto.config(justify = "left", state = "normal")

#Etiqueta del campo de texto (Apellidos)
label = Label(ventana, text = "Apellidos")
label.grid(row = 2, column = 0, sticky = W, padx = 5, pady = 5)

#Campo de texto (Apellidos)
campo_texto = Entry(ventana)
campo_texto.grid(row = 2, column = 1, sticky = W, padx = 5, pady = 5)
campo_texto.config(justify = "left", state = "normal")

#Etiqueta del campo de texto (Descripción)
label = Label(ventana, text = "Descripción")
label.grid(row = 3, column = 0, sticky = NW, padx = 5, pady = 5)

#Campo de texto (Text)
campo_grande = Text(ventana)
campo_grande.grid(row = 3, column = 1)
campo_grande.config(
    width = 30, 
    height = 5,
    font = ("Arial", 12),
    padx = 15,
    pady = 15
)

#Boton
Label(ventana).grid(row = 4, column = 1) #A efectos de separación
boton = Button(ventana, text ="Enviar")
boton.config(bg = "green", fg = "white", padx = 10, pady = 10)
boton.grid(row = 5, column =1, sticky = W)

ventana.mainloop()