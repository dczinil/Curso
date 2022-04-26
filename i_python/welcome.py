# TODO Solicitar nombre y saludar y regresar el numero de caracteres con el que cuena tu nombre
def run():
    hi = input('¿Cúal es tu nombre? ')
    welcom = (f'¡Mucho gusto {hi}!')
    print(welcom, f'La logingitu del saludo es; ', len(welcom), 'caracteres.')


if __name__ == '__main__':
    run()
