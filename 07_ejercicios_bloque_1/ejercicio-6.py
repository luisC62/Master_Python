"""
Ejercicio 6.

Mostrar todas las tablas de multiplicar que hay del 1 al 10.
Mostrar el título de cada tabla
"""
for tabla in range(1, 11):
    print(f"#######Tabla de multiplicar del {tabla}########")
    for numero in range(1,11):
        print(f"{tabla} por {numero} = {tabla * numero}")
