#Herencia: Es la posibilidad de compartir atributos y métodos
#entre clases, y que diferentes clases hereden de otras

class Persona:
    """
    nombre
    apellido
    altura
    edad
    """

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido 

    def getAltura(self):
        return self.altura 
    
    def getEdad(self):
        return self.edad 

    def setNombre(self, nombre):
        self.nombre = nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setAltura(self, altura):
        self.altura = altura

    def setEdad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

#Construimos la clase 'Informatico' heredando la clase 'Persona'
class Informatico(Persona):
    """
    lenguajes
    experiencia
    """
    #Constructor
    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, PHP"
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprendeLenguaje(self, lenguaje):
        self.lenguajes = self.lenguajes + ", " + lenguaje
        return self.lenguajes

    def programar(self):
        return "Estoy programando"

    def repararPC(self):
        return "He reparado tu ordenador"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() #Se ejecutará el constructor del la clase padre
        self.auditarRedes = "Experto"
        self.experienciaRedes = 15

    def auditoria(self):
        return "Estoy auditando una red"
