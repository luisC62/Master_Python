"""
Ejercicio 3
Escribir un programa que muestre los cuadrados de los 60 primeros numeros naturales.
Resolverlo con un bucle for y con un bucle while
"""

print("Versión con un bucle for")
for contador in range(1, 61):
    print(f"El cuadrado del número {contador} es: {contador * contador}")


print("Versión con un bucle while")
contador = 1
while contador <= 60:
    print(f"El cuadrado del número {contador} es: {contador * contador}")
    contador += 1