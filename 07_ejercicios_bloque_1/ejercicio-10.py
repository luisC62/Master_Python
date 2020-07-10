"""
Ejercicio 10
El programa tiene que pedir la nota de 15 alumnos y
tiene que decir cuantos han aprobado y cuantos han suspendido
"""

calificaciones =[4, 4, 6, 5, 3, 4, 4, 6, 5, 3, 4, 4, 6, 5, 3]
aprobados = 0
suspendidos = 0
for nota in calificaciones:
    if nota >=  5:
        aprobados += 1
    else: 
        suspendidos += 1

print(f"Han aprobado {aprobados} alumnos, y han suspendido {suspendidos} alumnos")