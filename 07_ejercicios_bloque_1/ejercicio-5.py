"""
Ejercicio 5
Hacer un programa que muestre todos los números entre dos números
que diga el usuario. 
"""
numero1 = int(input("Intruduce el primer numero: "))
numero2 = int(input("Intruduce el segundo numero: "))

if numero1 < numero2:
    for numero in range(numero1 + 1, numero2):
        print(numero)
elif numero1 > numero2:
    for numero in range(numero2 + 1, numero1):
        print(numero)
else:
    print("No hay números")    #numero1 == numero2
