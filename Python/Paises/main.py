def main():
    datosIntroducidos = input('Introduzca la lista de países separados por comas: ')
    paises = datosIntroducidos.split(',')
    # Quitar posibles espacios en blanco al inicio y al final
    # ATENCIÓN: Únicamente al inicio y al final (espacios intermedios no se eliminan). Ejemplo: República Checa
    for i in range(len(paises)):
        paises[i] = paises[i].strip(' ')

    paises = set(paises)

    print(sorted(paises))

if __name__ == '__main__':
    main()
