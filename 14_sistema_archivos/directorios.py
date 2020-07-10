import os, shutil

#Crear carpeta
if not os.path.isdir("./mi_carpeta"): #Antes hay que comprobar que no existe
    os.mkdir("./mi_carpeta")
else:
    print("El directorio ya existe")

#Eliminar carpeta
#os.rmdir("./mi_carpeta")

#Copiar carpetas
# original = "./mi_carpeta"
# copia = "./mi_carpeta_copiada"
# shutil.copytree(original, copia)

#Listar archivos dentro de una carpeta
print("Contenido de mi carpeta")
contenido = os.listdir("./mi_carpeta")
print(contenido)
