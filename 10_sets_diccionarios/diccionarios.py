"""
Diccionarios o arrays asociativos almacenan pares clave-valor
las claves son como índices alfanuméricos del array
También se les conoce como objetos-json
"""
persona={
    "nombre": "Victor",
    "apellido": "Robles",
    "web": "victorrobles.com"
}
print(persona)
print(type(persona))
#Para acceder a un elemento del diccionario utilizar: [clave]
print(persona["apellido"])

#Diccionarios dentro de listas
contactos = [
    {
        "nombre": "Victor",
        "apellido": "Robles",
        "email": "victor@robles.com"
    },
    {
        "nombre": "Lola",
        "apellido": "Ruiz",
        "email": "lola@ruiz.com"
    },
    {
        "nombre": "Pepa",
        "apellido": "Puyol",
        "email": "pepa@puyol.com"
    }
]
#para acceder a un elemento: [incice de la lista][clave]
print(contactos[1]["nombre"])
#Para recorrer la lista de diccionarios
print("\n************** LISTA DE CONTACTOS ****************")
for c in contactos:
    print(f"Nombre: {c['nombre']}") #Ojo con las comillas dobles!!!. Utilizar comillas simples en esta sentencia.
    print(f"Email: {c['email']}")
    print("---------------------------")


