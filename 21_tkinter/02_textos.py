from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

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
#Ejemplo de uso de parámetros de palabra clave
def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos}. Veo que eres de {pais}"

#Utilización de los parámetros de palabra clave en la función pruebas
otrotexto = Label(ventana, text=pruebas(nombre = "Luis", apellidos = "Cárceles", pais = "Finlandia"))
otrotexto.config(
    justify = RIGHT,
    font = ("Arial, 15"),
    bg = "orange",
    cursor = "circle"
)
texto.pack()
otrotexto.pack(anchor = E)

ventana.mainloop()