#Recorrer listas
peliculas = ["Batman", "Spiderman", "Superman"]

print("\n*************** LISTADO DE PELICULAS **********************")
for pelicula in peliculas:
    print(pelicula)
#Añadimos elementos a la lista
nueva_pelicula = ""
while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce una película nueva: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

#Para obtener el índice, utilizar el método index()
for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)} {pelicula}")

"""
Listas multidimendisionales
Son listas de más de una dimensión: Listas dentro de listas.
"""
print("\n*************** LISTA DE CONTACTOS **********************")
contactos = [
    ['Antonio', 'antonio@antonio.com'],
    ['Luis', 'luis@luis.com'],
    ['Marta', 'marta@marta.com']
]
print(contactos)
#Para imprimir el email del segundo contacto:
print(contactos[1][1])
#Para recorrer la lista:
for contacto in contactos:
    for elemento in contacto:
        print(elemento)
    print("\n")