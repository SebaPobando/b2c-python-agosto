class Vehiculo:
    def __init__(self, marca, modelo, anio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def estado(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.anio}")
        
    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")
        
    def detener(self):
        print(f"El vehículo {self.marca} {self.modelo} se ha detenido.")
        
class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)
        self.puertas = puertas
    
    def descripcion(self):
        self.estado()
        print(f"Este auto tiene {self.puertas} puertas.")
        
        
auto1 = Auto("Subaru", "Impreza", 2007, 4)
auto1.descripcion()
auto1.arrancar()
auto1.detener()

auto2 = Auto("Toyota", "Celica", 1995, 2)
auto2.descripcion()
auto2.arrancar()
auto2.detener()

auto3 = Vehiculo("Ford", "Mustang", 2020, 2)
auto3.descripcion() # Esto generará un error porque Vehiculo no tiene el método descripcion

class Moto(Vehiculo):
    def __init__(self, marca, modelo, anio, tipo):
        super().__init__(marca, modelo, anio)
        self.tipo = tipo
    
    def descripcion(self):
        self.estado()
        print(f"Esta moto es de tipo {self.tipo}.")