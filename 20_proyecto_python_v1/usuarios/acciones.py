import usuarios.usuario as modelo
import notas.acciones

class Acciones:
    def menuPrincipal(self):
        print("Menu Principal")
        print('''
        Acciones disponibles:
            - registro
            - login
        ''')
        accion = input("¿Que quieres hacer: ")
        if accion == "registro":
            self.registro()
        elif accion == "login":
            self.login()
        else: 
            print(f"La opción {accion} no existe")
            
    def registro(self):
        print("\nOk! vamos a registrarte en el sistema ....")

        nombre = input("¿Cual es tu nombre?: ")
        apellidos = input("¿Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1: #El usuario ha sido registrado con éxito (rowcount > 0)
            print(f"Ok {registro[1].nombre}. Te has registrado con el email {registro[1].email}.")
        else:
            print("No te has registrado correctamente.")


    def login(self):
        print("Vale!! Identifícate en el sistema.")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contraseña: ")

            usuario = modelo.Usuario('', '', email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado el {login[5]}")
                self.proximasAcciones(login)
        except Exception as e:
            #print(type(e))
            #print(type(e).__name__)
            print("Login incorrecto!!.")

    def proximasAcciones(self, usuario):
        print('''
        Acciones disponibles:
            - Crear nota (crear)
            - Mostrar tus notas (mostrar)
            - Eliminar nota (eliminar)
            - Salir (salir)
        ''')

        accion = input("¿Que quieres hacer?: ")
        hazEl = notas.acciones.Acciones() #Creamos el objeto notas.Acciones

        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Adios {usuario[1]}")
            exit()
        else:
            print(f"La acción {accion} no existe")
            self.proximasAcciones(usuario)

        return None



    