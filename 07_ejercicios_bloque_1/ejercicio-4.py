"""
Ejercicio 4.
Pedir dos números al usuario, hacer todas las operaciones básicas de una calculadora
y mostrarlo por pantalla
"""

numero1 = int(input("¿Cual es el primer número: "))
numero2 = int(input("¿Cual es el segundo número: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 != 0:
    division = numero1 / numero2
    resto = numero1 % numero2

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta entre {numero1} y {numero2} es: {resta}")
print(f"La multiplicacion de {numero1} por {numero2} es: {multiplicacion}")

if numero2 != 0:
    print(f"El cociente de dividir {numero1} entre {numero2} es: {division}")
    print(f"El resto de dividir {numero1} entre {numero2} es: {division}")
else:
    print("La que el segundo número es cero, no se puede calcular ni el cociente ni el resto de la división")
