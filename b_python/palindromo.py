#TODO Funsión para validar si la palaba es palindromo
def palindromo(palabra):
#TODO Borrar los espacio
    palabra = palabra.replace(" ","")
#TODO Convertir en minusculas todas las palabras (al igual se pueden convertir todas en mayusculas).
    palabra = palabra.lower()
#TODO Leer la palabra de forma invertida
    palabra_invertida = palabra [::-1]
#TODO Si es igual a la forma invertida debuelve True o de lo contrario False
    if palabra == palabra_invertida:
        return True
    else:
        return False


#TODO funsión que valida  palindromo si es correcta o no
def run():
    palabra = input("Escribe una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print("Es palindromo")
    else:
        print("No es palindromo")

#TODO desde aqui empieza a correr el programa
if __name__ == "__main__":
    run()