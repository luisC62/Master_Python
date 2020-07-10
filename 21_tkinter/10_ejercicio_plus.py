'''
CALCULADORA:
Refactorización del código del ejercicio anerior
Se crea la clase Calculadora
'''
from tkinter import *
from tkinter import messagebox as MessageBox

#Definición de la clase Calculadora
class Calculadora:
    
    def __init__(self, alertas):
        #Variables
        self.numero1 = StringVar()
        self.numero2 = StringVar()
        self.resultado = StringVar()
        self.alertas = alertas

    def sumar(self):
        try:
            self.resultado.set(float(self.numero1.get()) + float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")
        

    def restar(self):
        try:
            self.resultado.set(float(self.numero1.get()) - float(self.numero2.get()))
            self.mostrarResultado()

        except:
            self.alertas.showerror("Error", "Introduce bien los datos")

    def multiplicar(self):
        try:
            self.resultado.set(float(self.numero1.get()) * float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")
        

    def dividir(self):
        try:
            self.resultado.set(float(self.numero1.get()) / float(self.numero2.get()))
            self.mostrarResultado()
        except:
            self.alertas.showerror("Error", "Introduce bien los datos")
        

    def mostrarResultado(self):
        MessageBox.showinfo("Resultado", f"El resultado es: {self.resultado.get()}")
        self.numero1.set("")
        self.numero2.set("")

#Ventana principal
ventana = Tk()
ventana.title("Calculadora")
ventana.geometry("400x400")
ventana.config(bd = 25)

#Creamos el objeto calculadora
calculadora = Calculadora(MessageBox)

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


#Campo para el primer número
Label(marco, text = "Primer número: ").pack()
Entry(marco, textvariable = calculadora.numero1, justify = "center").pack()

#Campo para el segundo número
Label(marco, text = "Segundo número: ").pack()
Entry(marco, textvariable = calculadora.numero2, justify = "center").pack()

Label(marco, text="").pack() #A modo de separación

#Botones
Button(marco, text = "Sumar", command = calculadora.sumar).pack(side = "left", fill = X, expand = YES)
Button(marco, text = "Restar", command = calculadora.restar).pack(side = "left", fill = X, expand = YES)
Button(marco, text = "Multiplicar", command = calculadora.multiplicar).pack(side = "left", fill = X, expand = YES)
Button(marco, text = "Dividir", command = calculadora.dividir).pack(side = "left", fill = X, expand = YES)



ventana.mainloop()