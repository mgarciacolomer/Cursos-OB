class Vehiculo:
    color = ''
    ruedas = 0
    puertas = 0
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas
        print('Vehiculo construido')

class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self, velocidad, cilindrada, color, puertas):
        super().__init__(color, 4, puertas) # Se entiende que un coche tiene 4 ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        print('Coche construido')

# CREAMOS UN OBJETO DE CLASE COCHE

miCoche = Coche(160, 1400, 'Azul', 5)

print('Caracteristicas del coche creado:')
print('El color del coche es:', miCoche.color)
print('Tiene', miCoche.ruedas, 'ruedas')
print('Tiene', miCoche.puertas, 'puertas')
print('Alcanza una velocidad de:', miCoche.velocidad, 'km/h')
print('Tiene una cilindrada de:', miCoche.cilindrada, 'cc')



