# TODO two users are asked their age and name, they are told who is older.
def run():
    name_1 = input('Whats is you name? ')
    age_1 = int(input('How old are you? '))
    name_2 = input('Whats is you name? ')
    age_2 = int(input('How old are you? '))
    if age_1 < age_2:
        print('you are older ', name_2)
    elif age_1 > age_2:
        print('you are older ', name_1)
    else:
        print(f'both are the same age ', name_1, ' and ', name_2)


if __name__ == '__main__':
    run()
