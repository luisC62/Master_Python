"""
Operadores de comparación
== Igual
!= Diferente
> Mayor que
< Menor que
>= Mayor o igual que
<= Menor o igual que

"""
# Ejemplo1 (Estructura if básica)
print("###############EJEMPLO 1#################")
color = input("Introduce un color: ")
if color=="rojo":
    print(f"El {color} es mi color favorito")
else:
    print(f"No me gusta el color {color}")

#Ejemplo2
print("\n###############EJEMPLO 2#################")
#year = input("¿En que año estamos?: ")
year = "0"
if int(year) != 2020:
    print(f"El año {year} es incorrecto")
else:
    print(f"El año {year} es correcto")

#Ejemplo3 (If's anidados)
print("\n###############EJEMPLO 3#################")
nombre = "Luis"
ciudad = "Barcelona"
continente = "Europa"
edad = 55
mayoria = 18
if edad >= mayoria:
    print(f"{nombre} es mayor de edad")
    if continente != "Europa":
        print(f"{nombre} no es europeo")
    else:
        print(f"{nombre} es europeo, y de {ciudad}")
else:
    print(f"{nombre} no es mayor de edad")

#Ejemplo4 (Elif)
print("\n###############EJEMPLO 4#################")
dia = input("Introduce el dia de la semana: ")
if int(dia) == 1:
    print("El dia es lunes")
elif int(dia) == 2:
    print("El dia es martes")
elif int(dia) == 3:
    print("El dia es miercoles")
elif int(dia) == 4:
    print("El dia es jueves")
elif int(dia) == 5:
    print("El dia es viernes")
elif int(dia) == 6:
    print("El dia es sábado")
elif int(dia) == 7:
    print("El dia es domingo")
elif int(dia) > 7:
    print(f"{int(dia)} no es un dia de la semana")
elif int(dia) == 0:
    print(f"{int(dia)} no es un dia de la semana")

#Ejemplo5 (Operadores lógicos)
print("\n###############EJEMPLO 5#################")
"""
Operadores lógicos:
and, or, not
(en otros lenguages se utilizaría && o OR)
"""
edad_minima = 18
edad_maxima = 65
edad_real = input("Dime tu edad: ")
if(int(edad_real) >= edad_minima and int(edad_real) <= edad_maxima):
    print(f"Con {edad_real} años estás en edad de trabajar")
else:
    print(f"Con {edad_real} años no estás en edad de trabajar")

#Ejemplo6 (Más ejemplos con condicionales)
print("\n###############EJEMPLO 6#################")
pais = input("¿Cual es tu pais de origen: ")
if (pais == "España" or pais == "Mexico" or pais =="Colombia"):
    print(f"En {pais} se habla español")
else:
    print(f"En {pais} NO se habla español")

#Ejemplo7 (Más ejemplos con condicionales)
print("\n###############EJEMPLO 7#################")

pais = input("¿Cual es tu pais de residencia: ")
if (not(pais == "España" or pais == "Mexico" or pais =="Colombia")):
    print(f"En {pais} se NO habla español")
else:
    print(f"En {pais} se habla español")

#Ejemplo8 (Más ejemplos con condicionales)
print("\n###############EJEMPLO 8#################")

pais = input("¿Cual es tu pais preferente: ")
if pais != "España" and pais != "Mexico" and pais !="Colombia":
    print(f"En {pais} se NO habla español")
else:
    print(f"En {pais} se habla español")