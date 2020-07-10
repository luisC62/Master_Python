from tkinter import *
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.config(bd = 70)
def sacarAlerta():
    MessageBox.showinfo("Alerta", "Soy Luis Cárceles")

Button(ventana, text="Mostrar alerta!!!", command = sacarAlerta).pack() #Ojo!. Nombre de la función, sin paréntesis

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "¿Quieres continuar?")
    if resultado != "yes":
        MessageBox.showinfo("Chau!", f"Adios {nombre}")
        ventana.destroy()

Button(ventana, text="Salir", command = lambda: salir("Luis Cárceles")).pack() #consultar las funciones lambda

ventana.mainloop()