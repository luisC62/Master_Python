"""
Ejercicio 7.
Hacer un programa que muestre todos los númreros impares 
entre dos números que decida el usuario
"""
numero1 = int(input("Intruduce el primer numero: "))
numero2 = int(input("Intruduce el segundo numero: "))

if numero2 - numero1 > 2:
    for numero in range(numero1 + 1, numero2 +1):
        if numero % 2 == 1:
            print(numero)
elif numero1 - numero2 > 2:
    for numero in range(numero2 + 1, numero1 +1):
        if numero % 2 == 1:
            print(numero)

