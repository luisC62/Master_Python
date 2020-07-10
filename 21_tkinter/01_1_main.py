#Importamos la clase Programa del módulo my_prog
from my_prog import Programa

#Creamos un programa instanciando a la clase Programa
prog = Programa()
prog.cargar()
prog.addTexto("Este es el texto de una etiqueta")
prog.addTexto("Este es el texto de otra etiqueta")
prog.mostrar()
prog.mostrar()


