def repite(palabra, num_repetir):
    if num_repetir == 1:
        return print(f'{palabra}')
    
    print(f'{palabra}')
    return repite(palabra, num_repetir - 1)

def run():
    repite('Jesus', 8)


if __name__ == '__main__':
    run()