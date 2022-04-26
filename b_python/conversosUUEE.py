dollar = input("¿Cuántos dolares EEUU tienes?: ")   
dollar = float(dollar)
valor_peso = .049
peso = dollar / valor_peso
peso = round(peso, 2)
peso = str(peso)
print("Tienes $" + peso + " dollar")