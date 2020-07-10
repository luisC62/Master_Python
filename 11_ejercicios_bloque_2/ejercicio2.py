"""
Ejercicio 2: Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
Plus: Usar while y for
"""
#Necesario pra generar números aleatorios enteros
from random import seed
from random import randint
#Simulamos la introducción de 120 valores

#Utilizando un bucle for
print("\n********** Utilizando un bucle for ************")
valores = [] #Lista vacía
for contador in range(0, 120):
	valores.append(randint(0, 100)) #Añadimos un valor aleatorio entre 0 y 100

print(valores)
print(f"Longitud de la lista: {len(valores)}")

#Utilizando un bucle while
print("\n********** Utilizando un bucle while ************")
valores = [] #Lista vacía
while len(valores) < 120:
    valores.append(randint(0, 100)) #Añadimos un valor aleatorio entre 0 y 100

print(valores)
print(f"Longitud de la lista: {len(valores)}")
