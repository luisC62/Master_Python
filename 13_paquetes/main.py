"""
Un paquete es un conjunto de módulos
Para crear un paquete, hay que crear un subdirectorio con el nombre del paquete,
y dentro un fichero que se ha de llamar __ini__.py (en este caso vacío).
En este directorio también pondremos los módulos que formarán parte del paquete
(en nuestro caso: pruebas.py y herramientas.py)
"""
print("PROBANDO PAQUETES")

#from nombredelpaquete import modulo
from mipaquete import pruebas
from mipaquete import herramientas

pruebas.probando()
herramientas.nombreCompleto("Luis", "Cárceles")

"""
Para instalar paquetes vamos a la web pypi.org (python package index)
"""
