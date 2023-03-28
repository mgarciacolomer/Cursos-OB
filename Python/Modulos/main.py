import sys
import pprint
import operaciones as oper

# PAQUETE
import matematicas.suma

def main():
    print('Hola en main()')
    resSuma = oper.suma(2, 2)
    resResta = oper.resta(5, 3)
    print(resSuma)
    print(resResta)
    print(oper.comoMeLlamo())
    o = oper.Operador()
    print(o.multiplicacion(4,2))
    print(oper.PI)
    pprint.pprint(sys.path)

    res = matematicas.suma.suma(3, 4)
    print(res)

# CONVENCION PARA EL MAIN
if __name__ == '__main__':
    main()