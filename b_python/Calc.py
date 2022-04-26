a = int(input("Introduce el primer número; "))
b = int(input("Introduce el segundo número; "))


menu = """

Calculadora

1.- Suma
2.- Resta
3.- División
4.- Multiplicación

Elige una opción """

opcion = int(input(menu))

if opcion == 1:
    suma = a + b
    print ("La suma es; ",suma)
elif opcion == 2:
    resta = a - b
    print ("La resta es; ",resta)
elif opcion == 3:
    division = a / b
    print ("La division es; ",division)
elif opcion == 4:
    multiplicacion = a * b
    print("La multiplicacion es;",multiplicacion)
else:
    print("Ingresa una opción correcta por favor")
