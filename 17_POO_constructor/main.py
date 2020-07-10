from coche import Coche #Hay que importar la clase

carro = Coche("Amarillo", "Renault", "Clio", 110, 70, 4)
print(carro.getInfo())

carro1 = Coche("Verde", "Seat", "Panda", 100, 50, 4)
carro2 = Coche("Azul", "Citroen", "Xara", 100, 110, 4)
carro3 = Coche("Rojo", "Mercedes", "Case A", 220, 180, 4)

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())

carro4 = "No soy un coche"

#Detección del tipo de objeto
if type(carro4) == Coche:
    print("Es un objeto correcto!!!")
else:
    print("El objeto no es de la clase 'Coche'")
#visibilidad
print(carro.soy_publico)
print(carro.getPrivado()) #Sólo se puede acceder con un getter