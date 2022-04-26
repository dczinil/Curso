def raiz_cuadrada_babilonico(numero):
    braiz = numero / 2
    while True:
        if braiz * braiz == numero:
            return braiz
        else:
            cbraiz = braiz
            braiz = (braiz + (numero/braiz)) / 2
        if cbraiz == braiz:
            break
    return braiz

def es_primo(numero):
    if numero < 2:
        return False
    
    for i in range (2, numero):
        if numero % 1 == 0:
            return False
        return True

def run():
    numero = int(input('Escribe un número: '))
    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')
        
if __name__ == '__main__':
    run()