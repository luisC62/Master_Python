#¿Como podemos lanzar excepciones personalizadas?

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

try:
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")  #Lanzamos una excepcion personalizada
    elif len(nombre) < 1:
        raise ValueError("El nombre no está completo") #Lanzamos otra excepción
    else:
        print(f"Bienvenido {nombre} al Master de Python")
except ValueError:
    print("Introduce los datos correctamente!!!")
