class Persona:
    raza = "Humano" # Atributo de clase, compartido por todas las instancias
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def cumpleanos(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tienes {self.edad} años.")
        
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
        
        
        
class Adulto(Persona):
   def __init__(self, nombre, edad, profesion):
       super().__init__(nombre, edad)
       self.profesion = profesion
  
   def mi_profesion(self):
       super().presentarse()
       print("Soy un adulto y mi profesión es", self.profesion)
       
# Crear una instancia de la clase Adulto
renato = Adulto("Renato", 18, "Astronauta")
renato.mi_profesion()
renato.cumpleanos()

juan = Persona("Juan", 17)
juan.presentarse()

