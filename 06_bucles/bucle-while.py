"""
WHILE

Estructura de control que repite la ejecución de una serie de instrucciones, tantas veces
como sea necesario hasta que deje de cumplirse una condición.

Estructura:

while condición:
    bloque de instrucciones
    actualización de un contador para que el bucle sigua avanzando

"""

contador = 0 
while contador <= 100:
    print(f"El valor del contador actualizado es {contador}")
    contador += 1

#Para mostrar los números separados por comas:
print("\n-----------------------------------------------")
contador = 1
cadena =""
while contador <= 100:
    cadena += "," + str(contador)
    contador += 1
print(cadena)

#Tabla de multiplicar con el bucle while:
print("##################### EJEMPLO ##########################")
numero = int(input("¿Cual es el número del que quieres obtener la tabla?: "))
contador = 1
while numero <=10 and numero >= 0 and contador <=10:
    print(f"{numero} multiplicado por {contador} es igual a {numero * contador}")
    contador += 1
else: print("Fin de la tabla")