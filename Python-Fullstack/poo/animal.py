class Animal:
    def __init__(self, nombre, especie, edad, color, sonido):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.color = color
        self.sonido = sonido

    def hacer_sonido(self):
        print(f"El {self.especie} llamado {self.nombre} hace un sonido de {self.sonido}.")