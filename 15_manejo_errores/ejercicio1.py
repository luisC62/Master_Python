"""
Ejercicio 1. Copia de última pregunta del ejercicio 1 del bloque 2
Se modifica para que de un error al buscar el número y no encontrarlo en la lista
"""
# Crear la lista

numeros=[13, 64, 52, 73, 21, 7, 91, 63]

print("\n******** Buscar algún elemento que el usuario introduzca por teclado ********")
try:
    numero = int(input("Introduce un número de la lista: "))
    #El int tambien es susceptible de errores si se introduce una cadena cualquiera
    print(f"El número {numero} se encuentra en la posición: {numeros.index(numero)}")
    #Da ValueError si no está en la lista
except:
    print("El numero introducido no se encuentra en la lista")