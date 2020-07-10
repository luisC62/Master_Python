'''
Crear un programa que tenga:
(Ok)- Ventana
(Ok)- Tamaño fijo
(Ok)- No redimensionable
(Ok)- Un Menu (Inicio, Añadir, Información, Salir)
(Ok)- Diferentes pantallas
(Ok)- Formulario para añadir productos
(Ok)- Guardar datos temporalmente
(Ok)- Mostrar datos listados en la pantalla principal
(Ok)- Opción de salir
'''
from tkinter import *
from tkinter import ttk  #Widgets adicionales (TreeView)

#Creación y configuración de la ventana principal
ventana = Tk()
ventana.title("Proyecto con Python y Tkinter (por LC)")
#ventana.geometry("500x500")
ventana.minsize(500, 500) #A medida que añadamos, se irá haciendo más grande.
ventana.resizable(0, 0)

#Pantallas (cada pantalla es una función)
#Definción de campos comunes
info_label = Label(ventana, text = "Información")
home_label = Label(ventana, text = "Inicio")
product_box = Frame(ventana, width = 250)
add_label = Label(ventana, text = "Añadir producto")
data_label = Label(ventana, text = "Creado por Luis Cárceles 2020")
#Definimos la tabla para mostrar los productos
Label(product_box).grid(row = 0)
product_table = ttk.Treeview(product_box, height = 12, columns = 2)
product_table.grid(row = 1, column = 0, columnspan = 2)
product_table.heading("#0", text = 'Producto', anchor = W)
product_table.heading("#1", text = 'Precio', anchor = W)

#Campos del formulario para añadir productos (nombre y precio)
products = []
name_data = StringVar()
price_data = StringVar()

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c") #Necesario para poder guardar el contenido del campo Text
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)
    home()

add_frame = Frame(ventana)
add_name_label = Label(add_frame, text = "Nombre del producto: ")
add_name_entry = Entry(add_frame, textvariable = name_data)
add_price_label = Label(add_frame, text = "Precio de producto: ")
add_price_entry = Entry(add_frame, textvariable = price_data)
add_description_label = Label(add_frame, text = "Descripción: ")
add_description_entry = Text(add_frame)
boton = Button(add_frame, text = "Guardar", command = add_product)

#Funciones
def home():
    #Encabezado
    borrarPantallas()
    home_label.config(
        fg = "white",
        bg = "black",
        font = ("Arial", 30),
        padx = 210,
        pady = 20
    )
    home_label.grid(row = 0, column = 0)
    #Listar productos
    product_box.grid(row = 1)

    '''
    for product in products:
        if (len(product) == 3):
            product.append("added")
            Label(product_box, text = product[0]).grid()
            Label(product_box, text = product[1]).grid()
            Label(product_box, text = product[2]).grid()
            Label(product_box, text = "--------------------").grid()
    '''
    for product in products:
        if (len(product) == 3):
            product.append("added")
            product_table.insert('', 0, text = product[0], values = (product[1]))
            
    return True

def add():
    #Encabezado
    borrarPantallas()
    add_label.config(
        fg = "white",
        bg = "black",
        font = ("Arial", 30),
        padx = 120,
        pady = 20
    )
    add_label.grid(row = 0, column = 0, columnspan = 2)

    #Montaje del formulario
    add_frame.grid(row = 1)
    add_name_label.grid(row =1, column = 0, padx = 5, pady = 5, sticky = E)
    add_name_entry.grid(row =1, column = 1, padx = 5, pady = 5, sticky = W)
    add_price_label.grid(row =2, column = 0, padx = 5, pady = 5, sticky = E)
    add_price_entry.grid(row =2, column = 1, padx = 5, pady = 5, sticky = W)
    add_description_label.grid(row =3, column = 0, padx = 5, pady = 5, sticky = NE)
    add_description_entry.grid(row =3, column = 1, padx = 5, pady = 5, sticky = W)
    add_description_entry.config(
        width = 30,
        height = 5,
        font = ("Consolas", 12),
        padx = 15,
        pady = 15
    )
    boton.grid(row = 4, column = 1, sticky = W)
    boton.config(
        padx = 15,
        bg = "green",
        fg = "white"
    )
    return True

def info():
    #Encabezado
    borrarPantallas()
    info_label.config(
        fg = "white",
        bg = "black",
        font = ("Arial", 30),
        padx = 150,
        pady = 20
    )
    info_label.grid(row = 0, column = 0)

    #Montaje de la información
    data_label.grid(row = 1, column = 0)
    return True

def borrarPantallas():
    home_label.grid_remove()
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()
    product_box.grid_remove()

    return True



#Cargar la pantalla de inicio
home()

#Creación del menú
menu_superior = Menu(ventana)
menu_superior.add_command(label = "Inicio", command = home)
menu_superior.add_command(label = "Añadir", command = add)
menu_superior.add_command(label = "Información", command = info)
menu_superior.add_command(label = "Salir", command = ventana.quit)

#Cargar menú
ventana.config(menu = menu_superior)

#Cargar la ventana
ventana.mainloop()