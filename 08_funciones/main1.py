#Ejemplo 4 (parámetros opcionales)
print("############## EJEMPLO 4 #################")

def getEmpleado(nombre, dni = 0): #dni: Parámetro opcional. Por defecto es cero
    print(f"Nombre: {nombre}")
    if dni != 0:
        print(f"DNI: {dni}")

getEmpleado("David", 33333333)

getEmpleado("Luis")

#Ejemplo 5 (Parámetros opcionales y return)
print("############## EJEMPLO 5 #################")

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

print(calculadora(1,2))
print(calculadora(2,2,True))

#Ejemplo 6 (Funciones dentro de otras funciones)
print("############## EJEMPLO 6 #################")
def getNombre(nombre):
    texto = f"El nombre del usuario es: {nombre} \n"
    return texto

def getApellido(apellido):
    texto = f"El apellido del usuario es: {apellido} \n"
    return texto

def getNombreCompleto(nombre, apellido):
    texto = getNombre(nombre) + getApellido(apellido)
    return texto

print(getNombreCompleto("Luis", "Cárceles"))