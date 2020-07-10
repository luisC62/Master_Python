from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry("700x500")
texto = Label(ventana, text = "Hola. Soy Luis!!!").pack(anchor = W)

imagen = Image.open("./imagenes/minionsl.jpg")
render = ImageTk.PhotoImage(imagen)
Label(ventana, image=render).pack()

ventana.mainloop()