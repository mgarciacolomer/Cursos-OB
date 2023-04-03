def main():
    datosIntroducidos = input('Introduzca la lista de países separados por comas: ')
    paises = datosIntroducidos.split(',')
    # Quitar posibles espacios en blanco al inicio y al final
    # ATENCIÓN: Únicamente al inicio y al final (espacios intermedios no se eliminan). Ejemplo: República Checa
    for i in range(len(paises)):
        paises[i] = paises[i].strip(' ')

    # Convertimos en un set para eliminar elementos repetidos
    paises = set(paises)
    # Ordenamos
    paises = sorted(paises)

    # Arreglamos la cadena a mostrar
    mostrar = ''
    for pais in paises:
        mostrar += pais + ', '

    print(mostrar.strip(' ,')) # Quitamos última coma

if __name__ == '__main__':
    main()
