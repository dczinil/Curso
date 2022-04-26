    # * numero
    # * su raiz cuadrada
    # * saber los números primos hasta la llegar raiz cuadrada
    # * saber si es divisible hasta el ultimo primo
    
#TODO Funcion Raiz cuadrada babilonica
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


def run():
    numero = int(input('Escribe un número: '))
    print(raiz_cuadrada_babilonico(numero))
    

if __name__ == '__main__':
    run()