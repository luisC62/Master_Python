import clases

persona = clases.Persona() #Creo un objeto del tipo persona
persona.setNombre("Victor")
persona.setApellido("Robles")
persona.setAltura(1.7)
persona.setEdad(37)
print("\n-----------------------------------------")
print(f"La persona es {persona.getNombre()} {persona.getApellido()}")
print(persona.hablar())

informatico = clases.Informatico() #Creamos el objeto informatico definido en la 'librería' clases
informatico.setNombre("Luis")
informatico.setApellido("Cárceles")
print("\n-----------------------------------------")
print(f"El informático es {informatico.getNombre()} {informatico.getApellido()}") #Métodos heredados de la clase persona
print(informatico.getLenguajes())
print(informatico.caminar())
informatico.aprendeLenguaje("Python")
print(informatico.getLenguajes())
print("\n-----------------------------------------")
tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes)
print(tecnico.getLenguajes()) #Ojo! ya que hemos hecho super().__init__() y ejecutamos el construtor del padre también