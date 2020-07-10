#Definición de la clase coche
class Coche:
    #Atributos o propiedades
    #Características del coche
    color = "Rojo" #Con los valores de la propiedad por defecto
    marca = "Ferrari"
    modelo = "Aventator"
    velocidad = 360
    caballaje = 500
    plazas = 2

    soy_publico = "Hola, soy un atributo público"
    #El nombre de los atributos privados empieza con '__'
    __soy_privado = "Hola, soy un atributo privado"

    #Constructor de la clase: Es lo primero que se ejecuta cuando creamos un objeto
    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.caballaje = caballaje
        self.plazas = plazas

    #Métodos: Acciones que hace el ojeto (funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo
    
    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self): #Hay que hacer referencia al propio objeto con la palabra reservada self
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def getInfo(self):
        info = "--------Información del coche:----------"
        info += "\n Color: " + self.getColor()
        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Velocidad: " + str(self.getVelocidad())
        return info
    def getPrivado(self):
        #Esta es la única manera de acceder a los atributos privados
        return self.__soy_privado
#Fin de la definición de la clase