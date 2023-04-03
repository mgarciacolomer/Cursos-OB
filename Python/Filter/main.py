from functools import reduce
def main():
    lista = [1, 2, 4, 8, 9, 8, 77, 14, 65, 44, 79]

    filtrada = filter(lambda x: True if x % 2 else False, lista)
    listaFiltrada = list(filtrada)
    print(listaFiltrada)

    suma = reduce(lambda x,y: x + y, listaFiltrada)
    print(suma)
if __name__ == '__main__':
    main()

