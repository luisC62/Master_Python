"""
LISTAS (arrays)
Son colecciones o counto de datos/valores, bajo un único nombre.
Para acceder a esos valores podemos usar un índice numérico.
"""
#Ejemplo de lista
peliculas = ["Batman", "Spiderman", "Superman"]
#Para recorrer la lista utilizamos la variable índice
for indice in range(0, len(peliculas)):
    print(f"La película número {indice + 1} es: {peliculas[indice]}") 

#Otra manera de crear listas es utilizar la función list
cantantes = list(('Freddy Mercury', 'Paul McCartney', 'John Lennon')) 
#notar que pasamos una tupla a la función list()
def mostrarLista(lista):
    for indice in range(0, len(lista)):
        print(f"Elemento {indice} de la lista: {lista[indice]}")
mostrarLista(cantantes)

#Crear listas utilizando la función range
years = list(range(2020, 2050))
print(years)

#Los elementos de una lista pueden ser de tipos variados
variada = [44, "Luis", False, "Texto"]
print(variada)

#Los indices negativos son positivos contando desde el final:
print(cantantes[-1])

#Se pueden manejar sublistas de listas definidas
print(cantantes[1:3])

#Todos los elementos a partir de uno dado
print(peliculas[1:])

#Para añadir elementos a una lista utilizamos el método append
cantantes.append("Frank Sinatra")
print(cantantes)