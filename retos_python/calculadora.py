def calcular(operador_1, operacion, operador_2):
    resultado = {'tipo_operacion': '', 'resultado_operacion': 0}

    if operacion == '+':
        resultado['tipo_operacion'] = 'Suma'
        resultado['resultado_operacion'] = operador_1 + operador_2
    elif operacion == '-':
        resultado['tipo_operacion'] = 'Resta'
        resultado['resultado_operacion'] = operador_1 - operador_2
    elif operacion == '*':
        resultado['tipo_operacion'] = 'Multiplicacion'
        resultado['resultado_operacion'] = operador_1 * operador_2
    elif operacion == '/':
        resultado['tipo_operacion'] = 'Division'
        resultado['resultado_operacion'] = operador_1 / operador_2

    return resultado


def run():
    operador_1 = float(input('Dame el primer operador: '))
    operacion = input("""Dame la operacion que vas a realizar:
Suma: ' + ' 
Resta: ' - '
Multiplicacion: ' * '
Division: ' / '
: """)
    while operacion != '+' and operacion != '-' and operacion != '*' and operacion != '/':
        print('Selecciona una opcion correcta por favor: ')
        operacion = input("""
Suma: ' + ' 
Resta: ' - '
Multiplicacion: ' * '
Division: ' / '
: """)
    operador_2 = float(input('Dame el segundo operador: '))

    resultado = calcular(operador_1, operacion, operador_2)
    print('El Resultado de tu '  + resultado['tipo_operacion'] + ' es: ' + str(resultado['resultado_operacion']))

if __name__ == '__main__':
    run()