"""
Modulos: Funcionalidades ya hechas para reutilizar.
En python existen muchos módulos que se pueden consultar aqui: https://docs.python.org/3/py-modindex.html

Se pueden utilizar módulos que ya vienen en el lenguaje, 
se pueden bajar módulos de internet y también podemos
crear nuestros propios módulos.
"""
#Importamos el módulo
import mimodulo #con eso se importan todas las funciones del archivo mimodulo.py

mimodulo.holaMundo("Luis") #forma de invocar a funciones que están en mimodulo.py

print(mimodulo.calculadora(10, 20))

#Otra manera de utilizar los módulos es la siguiente: Sólo importamos la función holaMundo
from mimodulo import holaMundo
#De esta manera la invocación es más sencilla:
holaMundo("Pepa")

#Para importar toda las funciones, y utilizarlas de la misma manera:
from mimodulo import *
print(calculadora(30, 30))

#Módulo fechas (ya viene por defecto en la instalación de python)
import datetime
print(datetime.date.today()) #Devuelve la fecha de hoy
fecha_completa = datetime.datetime.now() #Nos dá la fecha y la hora actuales (ideal para registros de eventos)
print(fecha_completa)
print(fecha_completa.year) #Muestra una propiedad del objeto. En este caso el año
print(fecha_completa.month)
print(fecha_completa.day)
fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S") #Ver la documentación del módulo datetime
print(f"Mi fecha personalizada: {fecha_personalizada}")
print(datetime.datetime.now().timestamp()) #timestamp es el tiempo en unix

#Módulo de matematicas (también viene por defecto en la instalación de python)
import math
print(f"Raiz cuadrada de 10 = {math.sqrt(10)}") #Funciones matemáticas
print(f"Número PI = {math.pi}") #Constantes matemáticas
print(f"Pi redondeado al alza= {math.ceil(math.pi)}") #redondeo al alza
print(f"Pi redondeado a la baja= {math.floor(math.pi)}") #redondeo a la baja
#El módulo de numeros aleatorios (random) no está incluido dentro de math
import random
print(f"Numero aleatorio entero entre 0 y 100: {random.randint(0, 100)}")


