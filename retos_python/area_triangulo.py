import math

def area_triangulo_equilatero(lado_1, lado_2, lado_3):
    area = ( math.sqrt(3) / 4) * lado_1**2

    return area

def area_triangulo_escaleno(lado_1, lado_2, lado_3):
    if lado_1 > lado_2 and lado_1 > lado_3:
        base = lado_1
        altura = (lado_2 * lado_3) / base
    elif lado_2 > lado_3:
        base = lado_2
        altura = (lado_1 * lado_3) / base
    else:
        base = lado_3
        altura = (lado_1 * lado_2) / base

    area = (base * altura) / 2

    return area

def area_triangulo_isosceles(lado_1, lado_2, lado_3):
    if lado_1 == lado_2:
        base = lado_3
        lados_iguales = lado_1
    elif lado_2 == lado_3:
        base = lado_2
        lados_iguales = lado_1
    else:
        base = lado_1
        lados_iguales = lado_3
    
    area = (base * (math.sqrt((lados_iguales**2) - (base**2) / 4))) / 2

    return area


def run():
    lado_1 = float(input('Dame el primer lado del triangulo: '))
    lado_2 = float(input('Dame el segundo lado del triangulo: '))
    lado_3 = float(input('Dame el tercer lado del triangulo: '))

    if lado_1 == lado_2 and lado_2 == lado_3 and lado_3 == lado_1:
        resultado = area_triangulo_equilatero(lado_1, lado_2, lado_3)
        tipo_triangulo = 'Equilatero'
    elif (lado_1 == lado_2 and lado_3 != lado_1) or (lado_2 == lado_3 and lado_2 != lado_1) or (lado_1 == lado_3 and lado_1 != lado_2):
        tipo_triangulo = 'Isosceles'
        resultado = area_triangulo_isosceles(lado_1, lado_2, lado_3)
    else:
        tipo_triangulo = 'Escaleno'
        resultado = area_triangulo_escaleno(lado_1, lado_2, lado_3)

    print(f'El Area de tu Triangulo {tipo_triangulo} es {resultado}')

if __name__ == '__main__':
    run()