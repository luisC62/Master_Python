"""
Ejercicio 1. Hacer un programa que tenga una lista de
8 números enteros y haga lo siguiente:
- Recorrer la lista y mostrarla.
- Hacer función que recorra listas de números y devuelva un string.
- Ordenarla y mostrarla.
- Mostrar su longitud.
- Buscar algún elemento (que el usuario pida por teclado).
"""
# Crear la lista

numeros=[13, 64, 52, 73, 21, 7, 91, 63]


# Recorrer y mostrar

print("####### Recorrer y mostrar #######")
for numero in numeros:
    print(numero)


# Crear funcion que recorra lista y devuelva string
def mostrarLista(lista):
    resultado=""
    for elemento in lista:
        resultado += str(elemento)
        resultado +="\n"
    return resultado
   
print("\n******** Función que recorre la lista y devuelve un string ********")
print(mostrarLista(numeros))

print("\n******** Ordenar y mostrar la lista ********")
numeros.sort()
print(mostrarLista(numeros))

print("\n******** Obtener la longitud de la lista ********")
print(f"La longitud de la lista de números es: {len(numeros)}")

print("\n******** Buscar algún elemento que el usuario introduzca por teclado ********")
numero = int(input("Introduce un número de la lista: "))
print(f"El número que hay que buscar es el: {numero}")
if numero in numeros:
    print(f"El número {numero} se encuentra en la posición: {numeros.index(numero)}")
else: 
    print(f"El número {numero} no se encuentra en la lista.")