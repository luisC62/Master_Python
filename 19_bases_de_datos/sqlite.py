"""
SQLite es un módulo que se instala con Python
Sólo hay que importarlo y empezar a trabajar con el
"""
#Importar módulo
import sqlite3

#Conexión a la base de datos (parámetro. Se crea el fichero si no existe)
conexion = sqlite3.connect('pruebas.db')

#Creamos un cursor (para poder ejecutar consultas sobre conexion)
cursor = conexion.cursor()

#Creamos la productos
# cursor.execute('''CREATE TABLE productos(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     titulo varchar(255), 
#     descriptcion text, 
#     precio int(255))''')

# #Guardar los cambios. Los cambios se guardan ejecutando commit de la conexión
# conexion.commit()

#Insertar datos
# cursor.execute("INSERT INTO productos VALUES (null, 'Segundo producto', 'Descripción del segundo', 666)")
# cursor.execute("INSERT INTO productos VALUES (null, 'Tercer producto', 'Descripción del tercero', 333)")
# cursor.execute("INSERT INTO productos VALUES (null, 'Cuarto producto', 'Descripción del cuarto', 111)")
# conexion.commit()

#Se pueden insertar varios registros de golpe
# productos = [
#     ("Ordenador portatil", "Buen PC", 1000),
#     ("Teléfono móvil", "Buen teléfono", 700),
#     ("Impresora", "HP", 100),
#     ("Tableta", "Tableta con Android", 500)
# ]
# cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos) #Para insertar múlltiples lineas
# conexion.commit()
#Consultas SELECT
cursor.execute("SELECT * FROM productos WHERE precio >300")
productos = cursor.fetchall()
for producto in productos:
    print("Identidad: ", producto[0])
    print("Título: ", producto[1])
    print("Descripción: ", producto[2])
    print("Precio: ", producto[3])
    print("\n------------------------")

#Borrar registros
#cursor.execute("DELETE FROM productos") #Borra todo el contenido de la tabla
#Cerramos la conexión

conexion.close() 

