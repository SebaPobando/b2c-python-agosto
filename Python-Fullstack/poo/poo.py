class Persona:
    
    raza = "Humano" # Atributo de clase, compartido por todas las instancias
    
    def __init__(self, nombre, apellido, edad, estatura):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.estatura = estatura

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} {self.apellido}, tengo {self.edad} años y mido {self.estatura} metros.")
        
    def cumpleanos(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños {self.nombre}! Ahora tienes {self.edad} años.")

# Crear una instancia de la clase Persona
sebastian = Persona("Sebastián", "Poblete", 26, 1.67)
renato = Persona("Renato", "Peters", 18, 1.75)

# print("La raza de Sebastián es:", sebastian.raza)

# sebastian.raza = "Extraterrestre"

# print("La raza de Sebastián ahora es:", sebastian.raza)

# Persona.raza = "Mutante"

# print("La raza de Renato ahora es:", renato.raza)

@classmethod
def cambiar_raza(cls, nueva_raza):
    cls.raza = nueva_raza

@staticmethod
def calcular_imc(peso, altura):
    return peso / (altura ** 2)


# sebastian.saludar()
# renato.cumpleanos()
# sebastian.cumpleanos()

# Print de un atributo de instancia
# print(sebastian.edad)

# Una clase se puede ver como un molde para crear objetos (instancias).
# Una instancia es un objeto creado a partir de una clase (molde).
# Una clase puede tener atributos (características) y métodos (funciones).
# Los atributos son variables que pertenecen a la clase y describen sus características.
# Los métodos son funciones que pertenecen a la clase y describen sus comportamientos.

# class Animal:
#     def __init__(self, especie, edad, color, patas, sonido):
#         self.especie = especie
#         self.edad = edad
#         self.color = color
#         self.patas = patas
#         self.sonido = sonido

#     def hacer_sonido(self):
#         print(f"El {self.especie} hace un sonido de {self.sonido}.")
        
# gato = Animal("gato", 2, "naranjo", 4, "miau")
# gato.hacer_sonido()
