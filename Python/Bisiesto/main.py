"""
Si no es divisible entre 4 -> No es bisiesto
Si es divisible entre 4 y no es divisible entre 100 -> Es bisiesto
Si es divisible entre 4, entre 100 y no es divisible entre 400 -> No es bisiesto
Si no es divisible entre 4, 100, pero si entre 400 -> Es bisiesto

"""


def anyoBisiesto(anyo):
    if anyo % 4:
        return False
    elif anyo % 100:
        return True
    elif anyo % 400:
        return False
    else:
        return True


anyo = int(input('Introduzca el año: '))

if anyoBisiesto(anyo):
    print('El año', anyo, 'es bisiesto')
else:
    print('El año', anyo, 'no es bisiesto')
