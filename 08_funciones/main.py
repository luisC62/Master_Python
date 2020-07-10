"""
FUNCIONES:
Una función es un conjunto de instrucciones, agrupadas baja un nombre concreto, que pueden
reutilizarse invocando a la función tantas veces como sea necesario.

#Estructura de una función:

def nombreDeMiFuncion(parametros):
    Bloque o conjunto de instrucciones

#Para invocar la función:

nombreDeMiFuncion(mis_parametros)

"""

#Ejemplo 1
#Definición de la función
print("############## EJEMPLO 1 #################")
def muestraNombres():
    print("Luis")
    print("David")
    print("Marta")
    print("\n")

#Invocación de la función
muestraNombres()

#Ejemplo 2 (parámetros)
print("############## EJEMPLO 2 #################")
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    print(f"Y tienes {edad} años")

tu_nombre = input("Introduce tu nombre: ")
tu_edad = input("¿Cuantos años tienes?: ")
mostrarTuNombre(tu_nombre, tu_edad)

#Ejemplo 3 (tabla de multiplicar)
print("############## EJEMPLO 3 #################")
miNumero = int(input("Introduce el número del que quieras obtener la tabla de multiplicar: "))

def crearTablaMultiplicar(numero):
    if numero < 1 or numero > 10:
        print("El número ha de ser mayor que 0 y menor que 11")
    else:
        print(f"-------Tabla de multiplicar del {numero}---------")
        for cont in range(1, 11):
            print(f"{numero} por {cont} = {numero * cont}")

crearTablaMultiplicar(miNumero)

#Ejemplo 3.1 (mostrar todas las tablas de multiplicar del 1 al 10)
print("############## EJEMPLO 3.1 #################")
for tabla in range(1, 11):
    crearTablaMultiplicar(tabla)