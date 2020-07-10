mi_texto = "Master"
mi_texto2 = "en Python"

texto_unido = mi_texto + " " + mi_texto2
print(texto_unido)

#Para mostrar un texto entrecomillado, se utiliza \" (escapa de la funcionalidad original de las comillas)
texto_unido2 = "\"" + mi_texto + "\"" + " " + mi_texto2
print(texto_unido2)

#Otra solución es utilizar comillas simples en lugar de dobles
mi_texto3 ="'Master'"
texto_unido3 = mi_texto3 + " " + mi_texto2
print(texto_unido3)

#Caracteres especiales
texto_unido4=mi_texto + "\n" + mi_texto2 #Salto de línea
print(texto_unido4)

texto_unido5=mi_texto + "\t" + mi_texto2 #Tabulación
print(texto_unido5)

texto_unido6=mi_texto + "\r" + mi_texto2 #Retroceso
print(texto_unido6)