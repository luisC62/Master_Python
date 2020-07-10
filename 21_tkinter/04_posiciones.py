#Ejemplos con posiciones
from tkinter import *

ventana = Tk()
#ventana.geometry("500x500") #Si se comenta la línea el tamaño es atuomático

texto = Label(ventana, text="Bienvenido a mi programa")
#Configuración del texto
#Es parecido a configurar un CSS
texto.config(
    fg = "white",
    bg = "black",
    padx = 20,
    pady = 20,
    font = ("Arial, 20")
)
texto.pack(side = TOP) #Utilización de side.
#Ejemplo de uso de parámetros de palabra clave
def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}. Veo que eres de {pais}"

#Utilización de los parámetros de palabra clave en la función pruebas
otrotexto = Label(ventana, text= "Básico")
otrotexto.config(
    justify = RIGHT,
    font = ("Arial, 15"),
    bg = "orange",
    cursor = "circle",
    padx = 5,
    pady = 30
)
otrotexto.pack(side = TOP, fill = X, expand = YES) #Utilización de side (con parámetros)

otrotexto = Label(ventana, text= "Básico 1")
otrotexto.config(
    justify = RIGHT,
    font = ("Arial, 15"),
    bg = "Green",
    cursor = "circle",
    padx = 5,
    pady = 30
)
otrotexto.pack(side = LEFT, fill = X, expand = YES)

otrotexto = Label(ventana, text= "Básico 2")
otrotexto.config(
    justify = RIGHT,
    font = ("Arial, 15"),
    bg = "red",
    cursor = "circle",
    padx = 5,
    pady = 30
)
otrotexto.pack(side = LEFT, fill = X, expand = YES)

otrotexto = Label(ventana, text= "Básico 3")
otrotexto.config(
    justify = RIGHT,
    font = ("Arial, 15"),
    bg = "orange",
    cursor = "circle",
    padx = 5,
    pady = 30
)
otrotexto.pack(side = LEFT, fill = X, expand = YES)

ventana.mainloop()