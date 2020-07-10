"""
FOR Estructura:

for variable in elemento_interable (lista, rango, diccionaraio, ... etc):
    bloque_de_instrucciones

"""
resultado = 0
for contador in range(0, 10): #Contador ya está inicializado a 0
    resultado += contador
    print(f"Voy por el {contador}, y la suma es: {resultado}") #Ojo!. range no incluye el último (10 == stop)

#Ejemplo con tablas de multiplicar
print("\n################### EJEMPLO ######################")
numero_usuario = int(input("¿De que número quieres ver su tabla de multiplicar? ")) #Ojo!! input solo recibe strings!!

if numero_usuario>=1 and numero_usuario<=10:
    for contador in range(1, 11): #Contador ya está inicializado a 1
        if numero_usuario == 7:
            print(f"El número {numero_usuario} está prohibido")
            break #break se utiliza para forzar la salida del bucle for
        print(f"{numero_usuario} multiplicado por {contador} es: {numero_usuario * contador}")
    else:
        print(f"Tabla de multiplicar del {numero_usuario} finalizada") #else dentro de for sólo lo tiene python
