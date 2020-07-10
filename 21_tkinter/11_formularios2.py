from tkinter import *

ventana = Tk()
ventana.geometry("800x500")

encabezado = Label(ventana, text="Formularios avanzados")
encabezado.config(
    padx = 15,
    pady = 15,
    fg = "white",
    bg = "green",
    font = ("Open Sans", 18)
)
encabezado.grid(row = 0, column = 0, columnspan = 5, sticky = W)

#Botones check
Label(ventana, text ="¿A que te dedicas?").grid(row = 1, column = 0)

def mostrarprofesion():
    texto =""
    if web.get():
        texto += "Desarrollo web"
    if movil.get():
        if web.get():
            texto += " y desarrollo móvil"
        else:
            texto += "Desarrollo móvil"
    mostrar.config(text = texto, bg = "green")

web = IntVar()
movil = IntVar()
Checkbutton(
    ventana, 
    text = "Desarrollo Web",
    variable = web,
    onvalue = 1,
    offvalue = 0,
    command = mostrarprofesion
).grid(row = 2, column = 0)
Checkbutton(
    ventana, 
    text = "Desarrollo móvil",
    variable = movil,
    onvalue = 1,
    offvalue = 0,
    command = mostrarprofesion
).grid(row = 3, column = 0)

mostrar = Label(ventana, text = "")
mostrar.grid(row = 4, column = 0)

#Radio buttons
opcion = StringVar()
opcion.set(None)

def marcar():
    marcado.config(text = opcion.get())

Label(ventana, text = "¿Cual es tu género?: ").grid(row = 5)
Radiobutton(
    ventana, 
    text = "Masculino",
    variable = opcion,
    value = "Masculino",
    command = marcar
).grid(row = 6)
Radiobutton(
    ventana, 
    text = "Femenino",
    variable = opcion,
    value = "Femenino",
    command = marcar
).grid(row = 7)

marcado = Label(ventana, text="")
marcado.grid(row = 8)

#Option menu
def seleccionar():
    seleccionado.config(text = opcion.get())
opcion = StringVar()
opcion.set("Opción 1")
Label(ventana, text = "Selecciona un a opció  ").grid(row = 5, column = 1)
select = OptionMenu(ventana, opcion, "Opción 1", "Opción 2", "Opción 3")
select.grid(row = 6, column = 1)
Button(ventana, text = "Ver", command = seleccionar).grid(row = 7, column = 1)

seleccionado = Label(ventana, text ="")
seleccionado.grid(row = 8, column = 1)

ventana.mainloop()