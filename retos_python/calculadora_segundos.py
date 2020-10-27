def run():
    def convertir_a_seguntos(horas, minutos):
        horas = (horas * 60) * 60
        minutos = (minutos * 60)
        segundos = horas + minutos
        return segundos

    horas = int(input('Dame el numero de horas: '))
    minutos = int(input('Dame el numero de minutos: '))
    segundos = convertir_a_seguntos(horas, minutos)

    print(f'{horas} horas y {minutos} minutos equivale a {segundos}')

if __name__ == '__main__':
    run()