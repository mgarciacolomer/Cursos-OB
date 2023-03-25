peso = float(input('Introduzca su peso en kg: '))
estatura = float(input('Introduzca su estatura en m: '))

IMC = peso / (estatura ** 2)

print('Tu indice de masa corporal es: ' + str(round(IMC,2)))
