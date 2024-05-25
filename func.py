# Import some libary
from time import sleep

# Print some message
def print_info(string):
    print(string)
    sleep(1)

# Choosing game
def ChooseGame():
    way = [-1,1]
    print_info('Доступные игры: ')
    print_info('1. Карты')
    print_info('-1. Завершить')
    while True:
        try:
            choose_game = int(input('Выберите игру: '))
            if choose_game not in way:
                print_info('Выберите из доступных вариантов.')
                choose_game = int(input('Выберите игру: '))
        except ValueError:
            print_info('Введите цифру.')
        else:
            return choose_game