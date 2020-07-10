'''
Proyecto Python y MySQL
- Abrir asistente
- Preguntar login ó registro
- Si elegimos registro, creará un usuario en la BBDD
- Si elegimos login, identifica al usuario y nos preguntará lo siguiente:
- Crear nota, mostrar nota, borrar nota/s.
'''

from usuarios import acciones

inicio = acciones.Acciones()
inicio.menuPrincipal()
# print('''
# Acciones disponibles:
#     - registro
#     - login
# ''')
# hazEl = acciones.Acciones() #Módulo.objeto
# accion = input("¿Que quieres hacer: ")

# if accion == "registro":
#     hazEl.registro()
# elif accion == "login":
#     hazEl.login()
# else: 
#     print(f"La opción {accion} no existe")