class Alumno:
    nombre = ''
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print('Alumno creado')

    def mostrarAtributos(self):
        print('El alumno se llama:', self.nombre)
        print('Su nota es:', self.nota)

    def haAprobado(self):
        if self.nota < 5:
            print('El alumno ha suspendido')
        else:
            print('El alumno ha aprobado')

# INICIALIZAMOS CON EL CONSTRUCTOR
a1 = Alumno('Jaime', 3.5)
a2 = Alumno('Marta', 7.5)
a3 = Alumno('Javier', 5)

a1.mostrarAtributos()
a1.haAprobado()

a2.mostrarAtributos()
a2.haAprobado()

a3.mostrarAtributos()
a3.haAprobado()
