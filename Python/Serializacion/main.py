import pickle
class Vehiculo:
    marca = ''
    color = ''
    velocidad = 0.0

    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def __str__(self):
        return('Marca: ' + self.marca +
               '\nColor: ' + self.color +
                '\nVelocidad: ' + str(self.velocidad))

def main():

    coche = Vehiculo('BMW', 'Blanco', 250)
    fichero = open('vehiculo.bin', 'wb')
    pickle.dump(coche, fichero)
    fichero.close()

    fichero = open('vehiculo.bin', 'rb')
    miCocheGuardado = pickle.load(fichero)
    fichero.close()

    print(str(miCocheGuardado))

if __name__ == '__main__':
    main()

