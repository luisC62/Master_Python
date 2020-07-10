"""
Funciones predefinidas para listas
"""
cantantes = ['Frank Sinatra', 'Peter Gabriel', 'Sting', 'Bob Dylan']
numeros = [1, 2, 5, 8, 3, 4]

#Ordenar
print(numeros)
numeros.sort()
print(numeros)

#Añadir elementos
cantantes.append('Freddy Mercury')
print(cantantes)

#Insertar, en una posición dada
cantantes.insert(3, 'Joao Gilberto') #Inserta destrás de Sting
print(cantantes)

#Eliminar elementos de la lista
cantantes.pop(1)
print(cantantes) #Desaparece Peter Gabriel
cantantes.remove('Frank Sinatra') #El nombre ha de ser idéntico
print(cantantes)

#Dar la vuelta a una lista
numeros.reverse()
print(numeros)

#Buscar dentro de una lista
print('Bob Dylan' in cantantes) #Si se encuentra en la lista, devuelve true

#Contar elementos
print(len(cantantes)) #El mismo método para contar caracteres de un string

#Cuantas veces aparece un elemento en una lista
print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))
print(numeros)

#Conseguir el índice
print(cantantes)
print(cantantes.index("Bob Dylan")) #El índice que tiene Bob Dylan

#Unir listas
cantantes.extend(numeros)
print(cantantes)