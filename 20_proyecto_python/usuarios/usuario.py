import datetime
import hashlib
import usuarios.conexion as conexion

#Establecemos la conexión con la base de datos
connect = conexion.conectar()
database = connect[0]
cursor = connect[1]

class Usuario:
    def __init__(self, nombre, apellidos, email, password):
        self.nombre =  nombre
        self.apellidos = apellidos
        self.email = email
        self.password = password

    def registrar(self):
        fecha = datetime.datetime.now()
        #Cifrado de la contaraseña
        cifrado = hashlib.sha256()  #Elección del método de cifrado
        cifrado.update(self.password.encode('utf8')) #Contraseña cifrada
        sql = "INSERT INTO usuarios VALUES(null, %s, %s, %s, %s, %s)"
        usuario = (self.nombre, self.apellidos, self.email, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            print("Se ha producido un error")
            result = [0, self]
        
        return result



    def identificar(self):
        #Consulta para comrobar si existe
        sql ="SELECT * FROM usuarios WHERE email = %s AND password = %s"
        #Cifrado de la contaraseña
        cifrado = hashlib.sha256()  #Elección del método de cifrado
        cifrado.update(self.password.encode('utf8')) #Contraseña cifrada
        usuario = (self.email, cifrado.hexdigest())
        #Ejecución de la consulta
        cursor.execute(sql, usuario)
        #No hace falta el commit proque no estamos actualizando la base de datos
        result = cursor.fetchone()

        return result
