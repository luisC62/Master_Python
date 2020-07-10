'''
CALCULADORA:
- Dos campos de texto 
- 4 botones para las operaciones
- Mostrar el resultado en una alerta
'''
from tkinter import *
from tkinter import messagebox as MessageBox
#Ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.config(bd = 25)

def sumar():
    try:
        resultado.set(float(numero1.get()) + float(numero2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos")
    

def restar():
    try:
        resultado.set(float(numero1.get()) - float(numero2.get()))
        mostrarResultado()

    except:
        MessageBox.showerror("Error", "Introduce bien los datos")

def multiplicar():
    try:
        resultado.set(float(numero1.get()) * float(numero2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos")
    

def dividir():
    try:
        resultado.set(float(numero1.get()) / float(numero2.get()))
        mostrarResultado()
    except:
        MessageBox.showerror("Error", "Introduce bien los datos")
    

def mostrarResultado():
    MessageBox.showinfo("Resultado", f"El resultado es: {resultado.get()}")
    numero1.set("")
    numero2.set("")


#Marco
marco = Frame(ventana, width=250, height=200 )
marco.config(
    padx = 15,
    pady = 15,
    bd = 5,
    relief = SOLID
)
marco.pack(side = TOP, anchor = CENTER)
marco.pack_propagate(False) #Para que no se deforme al meter elementos.

#Variables
numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

#Campo para el primer número
Label(marco, text = "Primer número: ").pack()
Entry(marco, textvariable = numero1, justify = "center").pack()

#Campo para el segundo número
Label(marco, text = "Segundo número: ").pack()
Entry(marco, textvariable = numero2, justify = "center").pack()

Label(marco, text="").pack() #A modo de separación

#Botones
Button(marco, text = "Sumar", command = sumar).pack(side = "left", fill = X, expand = YES)
Button(marco, text = "Restar", command = restar).pack(side = "left", fill = X, expand = YES)
Button(marco, text = "Multiplicar", command = multiplicar).pack(side = "left", fill = X, expand = YES)
Button(marco, text = "Dividir", command = dividir).pack(side = "left", fill = X, expand = YES)



ventana.mainloop()