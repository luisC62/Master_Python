nombre ="Luis Cárceles"
frase ="       frase    con  muchos      espacios      "
year = 2020
#Funciones generales: print, type, instance, str.strip(), del, len, string.find(), string.replace(), string.lower(), string.upper()
#Para ver más funciones, consultar la documentación de python
print(nombre)
print(type(nombre))

#detectar si es una instancia de un objeto
comprobar = isinstance(nombre, str)  
if comprobar: 
    print("Ok, es un string")
if not isinstance(nombre, float):
    print("La variable no es un número real")

#Se accede a un método general del objeto str que elimina los espacios al principio y final
print(year)
print(frase)
print(frase.strip()) 

#Borra la variable year de la memoria del programa
del year  
#print(year) dará error a partir de 

#len sirve para ver cuantos caracteres tiene un string o elementos elementos tiene una lista
print(len(nombre))

#Para buscar palabras en un string:
frase="La vida es bella"
print("vida empieza en el caracter: " + str(frase.find("vida")))

#Para reemplazar palabras en un string
print(frase.replace("bella", "un regalo"))

#mayúsculas y minúsculas
print(nombre.lower())
print(nombre.upper())