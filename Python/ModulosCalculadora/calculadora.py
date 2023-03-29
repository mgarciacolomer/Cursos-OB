"""Realiza las operaciones una por una en toda la tupla de argumentos
SUMA = a + b + c -...
RESTA = a - b - c - ...
MULTIPLICACIÓN = a * b * c
DIVISIÓN = ( ... (a / b) / c ) / ... )
"""
def sumar(*args):
    resultado = 0
    for item in args:
        resultado += item
    return resultado

def restar(*args):
    resultado = args[0]
    for i in range(len(args)):
        if i != 0:
            resultado -= args[i]
    return resultado

def multiplicar(*args):
    resultado = 1
    for item in args:
        resultado *= item
    return resultado

def dividir(*args):
    resultado = args[0]
    for i in range(len(args)):
        if i != 0:
            resultado /= args[i]
    return resultado