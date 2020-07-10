#manejo de múltiplies excepciones
try:
    numero = int(input("Dime un número para elevarlo al cuadrado: "))
    #genera un TypeError 
    print(f"El cuadrado del número es: {numero * numero}")
    #genera un ValueError si se introduce un string
except TypeError:
    print("Has de convertir tus cadenas a enteros")
#except ValueError:
#   print("Has de introducir un valor correcto")

#Se puede hacer de otra forma:
except Exception as e:
    print("Se ha producido un error: ",  type(e).__name__)