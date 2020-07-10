"""
Ejercicio 8.
Hacer un programa que extraiga un tanto por ciento (decidido por el usuario)
de un número que introduzca el usuario
"""

numero = float(input("Introduce el número: "))
porcentaje = float(input("Introduce el porcentaje que quieres que sea extraido: "))

resultado = numero - numero * porcentaje / 100
print(f"El resultado de extrar el {porcentaje} % de {numero} es: {resultado}")