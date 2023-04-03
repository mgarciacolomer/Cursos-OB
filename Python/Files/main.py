def main():
    fichero = open('fichero.txt', 'w')
    fichero.write('Hola soy un fichero escrito desde Python\n')
    fichero.close()

    fichero = open('fichero.txt', 'a+')
    fichero.write('Soy una nueva linea\n')

    datos = fichero.read()

    print(datos)
    fichero.close()

if __name__ == '__main__':
    main()