#Pruebas con el módulo de mysql connector
import mysql.connector

#Conexión a la base de datos
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="", 
  database = "master_python"
)
# print(database) #Nos dice que el objeto es del tipo mysql.connector (no nos hemos conectado a una base de datos todavía)

# Con un cursor podemos empezar a hacer consultas a la base de datos.
mycursor = mydb.cursor(buffered = True)

# Creación de la base de datos
#mycursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

#mycursor.execute("SHOW DATABASES") #Para listar las bases de datos en el servidor
# for bd in mycursor:
#   print(bd)

# Creación de tablas (Una vez conectado a la base de datos)
# mycursor.execute('''
# CREATE TABLE IF NOT EXISTS vehiculos(
#   id int(10) auto_increment not null,
#   marca varchar(40) not null,
#   modelo varchar(40) not null,
#   precio float (10,2) not null,
#   CONSTRAINT pk_vehiculo PRIMARY KEY(id)
# )
# ''')

#Consultar cuantas tablas hay
# mycursor.execute("SHOW TABLES")
# for tabla in mycursor:
#   print(tabla)

#Inserción de registros: Ojo! no olvidar hacer el commit() de la base de datos, no del cursor
# mycursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra', 18500)")
# mydb.commit()

#Podemos insertar tuplas
# coches = [
#   ('Seat', 'Ibiza', 5000),
#   ('Renalult', 'Clio', 15000),
#   ('Citroen', 'Saxo', 2000),
#   ('Mercedes', 'Clase C', 35000)
# ]

# mycursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)
# mydb.commit()

#Sentencias de consulta con SELECT
# mycursor.execute("SELECT * FROM vehiculos")
# resultado = mycursor.fetchall()

# for coche in resultado:
#   print(coche)

#Para borrar registros de la tabla
#por ejemplo para borrar todos los vehiculos Renault:
# mycursor.execute("DELETE FROM vehiculos WHERE marca ='Renalult'")
# mydb.commit()

#Para actualizar registros de la base de datos
mycursor.execute("UPDATE vehiculos SET modelo = 'Leon' WHERE marca ='Seat'")
mydb.commit()
