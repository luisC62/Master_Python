"""
Ejercicio 4. Crear un script que tenga 4 variables: 
una lista, un string, un entero y un booleano, y que imprima un mensaje 
según el tipo de dato de cada variable. Usar funciones.
"""
miLista = [["a", "b", "c"], "cadena", 100, False]

def devolverClase(unaLista):
    for contador in range(0, len(unaLista)):
        print(f"El elemento {contador} de la lista es: {type(unaLista[contador])}, y su valor es: {unaLista[contador]}")

devolverClase(miLista)