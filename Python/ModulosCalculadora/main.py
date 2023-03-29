import calculadora as calc

def main():
    a = float(input('Introduzca el valor de a: '))
    b = float(input('Introduzca el valor de b: '))
    c = float(input('Introduzca el valor de c: '))

    print('La suma es: ', calc.sumar(a, b, c))
    print('La resta es: ', calc.restar(a, b, c))
    print('La multiplicación es: ', calc.multiplicar(a, b, c))
    print('La división es: ', calc.dividir(a, b, c))


if __name__ == '__main__':
    main()