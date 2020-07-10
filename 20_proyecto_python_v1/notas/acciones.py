import notas.nota as modelo

class Acciones:

    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!!. Vamos a crear una nota: ")

        titulo = input("Introduce el título de tu nota: ")
        descripcion = input("Mete el contenido de tu nota: ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()
        if guardar[0] >= 1:
            print(f"Perfecto!. Has guardado la nota {nota.titulo}")
        else:
            print(f"No se ha guardado la nota. Lo siento {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]}!!. Aqui tienes tus notas: ")
        nota = modelo.Nota(usuario[0])
        notas = nota.listar()
        #print(notas) #se muestra la lista
        for nota in notas:
            print("\n***********************************************")
            print(nota[2])
            print(nota[3])
            print("***********************************************")

    def borrar(self, usuario):
        print(f"\nOk {usuario[1]}. Vamos a borrar notas")
        titulo = input("Introduce el título de la nota a borrar: ")
        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("No se ha podido borrar la nota!")
