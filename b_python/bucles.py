# contador = 0
# print("2 elevado a " + str(contador) + " es igual a " + str(2**contador))

# contador = 1
# print("2 elevado a " + str(contador) + " es igual a " + str(2**contador))

# contador = 2
# print("2 elevado a " + str(contador) + " es igual a " + str(2**contador))

# contador = 3
# print("2 elevado a " + str(contador) + " es igual a " + str(2**contador))

# contador = 4
# print("2 elevado a " + str(contador) + " es igual a " + str(2**contador))

# contador = 5
# print("2 elevado a " + str(contador) + " es igual a " + str(2**contador))


def run():
#TODO constante
    LIMITE = 1000000
    
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
#TODO Para no tener que colocar "srt" hay que colocar f antes de >>""<< y las variables entre {}
#   print("2 elevado a " + str(contador) + " es igual a " + potencia_2)
        print(f"2 elevado a {contador} es igual a {potencia_2}")
        contador = contador + 1
        potencia_2 = 2**contador

if __name__ == "__main__":
    run()