"""
Una variable es un contenedor de información
que guardará un dato, se pueden crear muchas
variables y que cada una contenga un dato distinto
"""

#Crear variables y asignarles un valor
texto = "Master en Python"
texto2 = "con Victor Robles"
numero = 45
decimal = 6.7
print("----------------------")
#Mostrar el valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)

print("----------------------")
#Reasignar valor de algunas variables
numero = 77
decimal = 8.9
print(numero)
print(decimal)

print("----------------------")
#Concatenación (unión de strings)
nombre = "Luis"
apellido = "Carceles"
web ="luiscarceles.es"
#Concatenación simple:
print(nombre + " " + apellido + " - " + web)
#Otra manera equivalente de obtener el mismo resultado (montar con f):
print(f"{nombre} {apellido} - {web}")
#Otra manera es utilizar el método format:
print("Hola. Me llamo {} {}, y mi web es: {}".format(nombre, apellido, web))

