from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, edad, color, sonido, raza):
        super().__init__(nombre, edad, color, sonido)
        self.raza = raza

    def descripcion(self):
        return f"{self.nombre} es un {self.raza} de color {self.color} y tiene {self.edad} años."

    def hacer_sonido(self):
        return f"{self.nombre} ladra: {self.sonido}."
    
perro1 = Perro("Rex", 5, "marrón", "Guau Guau", "Labrador")
print(perro1.descripcion())