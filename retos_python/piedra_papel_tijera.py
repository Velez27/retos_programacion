def piedra_papel_tijeras(jugador_1, jugador_2):
    ganador = ''
    if jugador_1 == jugador_2:
        ganador = 'Empate'
    elif (jugador_1 == 'piedra'  and jugador_2 == 'tijeras') or (jugador_1 == 'papel' and jugador_2 == 'piedra') or (jugador_1 == 'tijeras' and jugador_2 == 'papel'):
        ganador = 'Jugador 1'
    elif (jugador_2 == 'piedra'  and jugador_1 == 'tijeras') or (jugador_2 == 'papel' and jugador_1 == 'piedra') or (jugador_2 == 'tijeras' and jugador_1 == 'papel'):
        ganador = 'Jugador 2'
    
    return ganador


def run():
    contador = 0
    victorias_jugador_1 = 0
    victorias_jugador_2 = 0

    while contador < 3:
        jugador_1 = input('Selecciona una opcion de: Piedra, Papel o Tijeras?: ')
        jugador_1 = jugador_1.lower()
        while jugador_1.lower() != 'piedra'  and jugador_1.lower() != 'papel' and jugador_1.lower() != 'tijeras':
            jugador_1 = input('Selecciona una opcion valida de: Piedra, Papel o Tijeras?: ')
        jugador_2 = input('Selecciona una opcion de: Piedra, Papel o Tijeras? : ')
        jugador_2 = jugador_2.lower()
        while jugador_2.lower() != 'piedra'  and jugador_2.lower() != 'papel' and jugador_2.lower() != 'tijeras':
            jugador_2 = input('Selecciona una opcion valida de: Piedra, Papel o Tijeras?: ')
        
        ganador = piedra_papel_tijeras(jugador_1, jugador_2)
        print(f'El ganador de esta Ronda es: {ganador}')

        if ganador == 'Jugador 1':
            victorias_jugador_1 += 1
            if victorias_jugador_1 == 2:
                break
        elif ganador == 'Jugador 2':
            victorias_jugador_2 += 1
            if victorias_jugador_2 == 2:
                break

        contador += 1
    
    if victorias_jugador_1 == victorias_jugador_2:
        print('Jugadores empatados')
    elif victorias_jugador_1 > victorias_jugador_2:
        print('El Ganador es el Jugador 1')
    else:
        print('El Ganador es el Jugador 2')

if __name__ == '__main__':
    run()