import mysql.connector

#Definimos la función para conectar a la base de datos
def conectar():
    #Creamos el objeto de base de datos
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "master_python",
        port = 3306
    )
    #Creamos el objeto cursor para ralizar múltiples consultas
    cursor = database.cursor(buffered = True)

    return [database, cursor]