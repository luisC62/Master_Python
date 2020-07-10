"""
Para trabajar con archivos, utilizaremos el paquete io, concretamente
el módulo open.
"""
from io import open
import pathlib

#Abrimos el archivo (o lo creamos si no existe)
#archivo = open("fichero_texto.txt", "a+") #Con los permisos a+
#Se puede utilizar pathlib para encontrar rutas:
ruta = str(pathlib.Path().absolute()) + "\\" + "fichero_texto.txt"
print(ruta)
archivo = open(ruta, "a+") #No olvidar los permisos de archivo

#Para escribir en el fichero utilizamos el método write del objeto archivo
archivo.write("***Soy un texto escrito desde un programa en python****\n")

#Para cerrar el archivo utilizamos el método close del objeto archivo
archivo.close() #Es conveniente cerrar todos los archivos con los que trabajemos.

archivo_lectura = open(ruta, "r") #Ahora abrimos el archivo con permiso sólo de lectura
#contenido = archivo_lectura.read()
#Para leer cada caracter del contenido
# for elemento in contenido:
#     print(elemento)
#Normalmente para ver el contenido del archivo se hace:
# print(contenido)
#Leer por lineas y meterlo en una lista
lista = archivo_lectura.readlines()
archivo_lectura.close()
print(lista)
for linea in lista: #Recorremos el contenido como si fuera una lista
    print(linea)

#Para hacer movimientos con archivos utilizaremos el módulo shutil
import shutil #Utilidades del shell activo del s.o.
# origen = str(pathlib.Path().absolute()) + "\\" + "fichero_texto.txt"
# destino = str(pathlib.Path().absolute()) + "\\" + "fichero_texto_copia.txt"
# #Para copiar el archivo utilizamos copyfile() de shutil
# shutil.copyfile(origen, destino)

#Renombrar o mover archivos 
# original = str(pathlib.Path().absolute()) + "\\" + "fichero_texto_copia.txt"
# nuevo = str(pathlib.Path().absolute()) + "\\" + "fichero_texto_copia_nuevo.txt"
# shutil.move(original, nuevo)

#Para eliminar archivos utilizaremos el módulo os
#import os
#os.remove(str(pathlib.Path().absolute()) + "\\" + "fichero_texto_copia_nuevo.txt")

#Para comporbar si un fichero o directorio existe
import os.path
print(os.path.abspath("."))
if (os.path.isfile("./fichero_texto.txt")):
    print("El archivo existe")
else: 
    print("El archivo no existe")

