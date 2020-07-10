#Programación orientada a objetos

#Definición de una clase (molde para crear objetos de ese tipo).

#(coche) con características similares.
class Coche:
    #Atributos o propiedades
    #Características del coche
    color = "Rojo" #Con los valores de la propiedad por defecto
    marca = "Ferrari"
    modelo = "Aventator"
    velocidad = 360
    caballaje = 500
    plazas = 2

    #Métodos: Acciones que hace el ojeto (funciones)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self): #Hay que hacer referencia al propio objeto con la palabra reservada self
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
#Fin de la definición de la clase

#Crear objetos ==> Instanciar la clase
coche = Coche() #De esta manera se crea un objeto de la clase Coche
coche.setColor("Amarillo")
coche.setModelo("Murcielago")
print(coche.marca, coche.color, coche.getModelo())
# print(f"Velocidad actual: {coche.getVelocidad()}")
# print("Acelerando")
coche.acelerar()
# print(f"Velocidad actual: {coche.getVelocidad()}")
# print("Frenando")
coche.frenar()
coche.frenar()
# print(f"Velocidad actual: {coche.getVelocidad()}")
coche2 = Coche()
print("El color del segundo coche es: ", coche2.getColor())
print(coche2.marca, coche2.getColor(), coche2.getModelo())