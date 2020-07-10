#Variable sin contenido
nada = None
#Para mostrar el tipo de dato se utiliza la función type
print(type(nada))

#Strings
cadena  ="Hola soy Luis Cárceles"
print(cadena)
print(type(cadena))

#Integer
entero  =99
print(entero)
print(type(entero))

#Float
flotante  = 4.4
print(flotante)
print(type(flotante))

#Boolean
booleano  = True
print(booleano)
print(type(booleano))

#List
lista = [10, 20, 30, 100, 200]
print(lista)
print(type(lista))

#List
listamixta = [40, "treinta", 30, "muchos"]
print(listamixta)
print(type(listamixta))

#Tuple
tuplaNoCambia = ("Master", "en", "Python")
print(tuplaNoCambia)
print(type(tuplaNoCambia))

#Dictionary
#Array asociativos o variable JSON (clave: valor)
diccionario = {
    "nombre": "Luis",
    "apellido": "Cárceles",
    "curso": "Master en Python"
}
print(diccionario)
print(type(diccionario))

#Range
rango = range(9)
print(rango)
print(type(rango))

print("---------Conversión de tipos-----------")
texto = "Hola, soy un texto"
numerito = 667
print(texto + " " + str(numerito))

numeraco = float(numerito)
print(numeraco)