#Ejemplo 7 (Funciones Lambda)
"""
-Son funciones anónimas (no tienen nombre)
-No hace falta definirlas (utilizando def)
-Se programan en una sola línea de  código
-Sirven para ejecutar tareas muy simples, pero muy repetitivas.
"""
print("############## EJEMPLO 7 #################")
dime_el_year = lambda year: f"El año es {year}" #year: parámetro, el texto es lo que devuelve a la variable

print(dime_el_year(1998))