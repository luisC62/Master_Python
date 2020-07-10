"""
Capturar excepciones y manejar errores en código
susceptible a fallos/errores.
"""
#Ejemplo
try:
    nombre = input("¿Cual es tu nombre?: ")
    if len(nombre) > 1:
        nombre_usuario = nombre
    print(nombre_usuario) #Da un error si introducimos una cadena vacía en nombre (nombre_usuario var no definida)
except:
    print("Error: Introduce un nombre correcto")
else: #Opcional
    print("Ha funcionado correctamente")
finally: #Opcional: Siempre se ejecuta
    print("Fin de ejecución del bloque")
