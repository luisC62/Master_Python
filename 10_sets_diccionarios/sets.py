"""
Un SET es un tipo de dato que no tiene índice ni orden.
Se utiliza simplemente para almacenar una colección de valores.
"""
#Los Sets se definen con las llaves: {}
personas = {
    "Victor",
    "Manolo",
    "Luisa"
}
print(personas)
print(type(personas))

#Métodos asociados al tipo set:

#Para agregar elementos al set, se utiliza add
personas.add("Lola")
print(personas)
#Para eleminar elementos se utiliza remove
personas.remove("Manolo")
print(personas)
