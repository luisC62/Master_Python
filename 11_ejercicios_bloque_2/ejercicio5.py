"""
Ejercicio 5.
Crear una lista de diccionairos con el contenido de esta tabla (videojuegos):
ACCION            AVENTURA              DEPORTES
GTA               Assasins Creed         FIFA 21
Call of Duty        Crash                PRO 21
Pugb              Prince of Persia       Moto GP 21

Mostrar esta información ordenada.
"""
videojuegos = [
    {
        "nombre": "GTA",
        "genero": "ACCION"
    },
    {
        "nombre": "Call of Duty",
        "genero": "ACCION"
    },
    {
        "nombre": "PUGB",
        "genero": "ACCION"
    },
    {
        "nombre": "Assasins Creed",
        "genero": "AVENTURA"
    },
    {
        "nombre": "Crash",
        "genero": "AVENTURA"
    },
    {
        "nombre": "Prince of Persia",
        "genero": "AVENTURA"
    },
    {
        "nombre": "FIFA 21",
        "genero": "DEPORTES"
    },
    {
        "nombre": "PRO 21",
        "genero": "DEPORTES"
    },
    {
        "nombre": "Moto GP 21",
        "genero": "DEPORTES"
    }
]

for contador in range(0, len(videojuegos)):
    print(f"El videojuego {videojuegos[contador]['nombre']} es del genero: {videojuegos[contador]['genero']}")

