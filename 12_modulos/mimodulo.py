"""
Se suelen incluir funciones o clases (POO)
"""
#Una función 
def holaMundo(nombre):
    print(f"Hola. ¿Como estas {nombre}?")

#Otra función
def calculadora(numero1, numero2, basicas= False): #El parámetro básicas es opcional
    cadena ="-----------Calculadora----------------------"
    if numero2 == 0:
        cadena = "\nEl segundo parámetro no puede ser 0"
    else:
        cadena += f"\nSuma: {numero1} + {numero2} = {numero1 + numero2}"
        cadena += f"\nResta: {numero1} - {numero2} = {numero1 - numero2}"
        if not basicas:
            cadena += f"\nMultiplicación: {numero1} * {numero2} = {numero1 * numero2}"
            cadena += f"\nDivisión: {numero1} / {numero2} = {numero1 / numero2}"

    return cadena #Devolvemos el resultado