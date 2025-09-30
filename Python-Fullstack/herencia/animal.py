class Animal:
    def __init__(self, nombre, edad, color, sonido):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        self.sonido = sonido

    def descripcion(self):
        return f"{self.nombre} es de color {self.color} y tiene {self.edad} años."

    def hacer_sonido(self):
        return f"{self.nombre} hace un sonido de {self.sonido}."