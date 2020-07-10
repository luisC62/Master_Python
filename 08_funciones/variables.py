"""
-Variable local: Se define dentro de la función. No puede utilizase fuera de la función.
-Variable global: Son las que se declaran fuera de la función y están disponibles dentro y fuera de ella.
"""

#Variable global
frase = "Ni los genios son tan genios, ni los mediocres son tan mediocres."

def holaMundo(): #La variable frase, dentro de la función, solo vale dentro de la función (ámbito local)
    frase = "Hola Mundo!!!"
    print(frase)

holaMundo()

def holaMundo2(): #Al no estar definida frase dentro de la función, utiliza la variable definida al principio (ámbito global)
    print(frase)

holaMundo2()

def holaMundo3():
    global website #Con la palabra clave global, se tiene acceso desde fuera de la función
    website = "www.luiscarceles.com"
    print(f"Visite {website}")

holaMundo3()
print(website) #Ojo con el orden de ejecución. holaMundo3() se ha de ejecutar necesariamente antes.


