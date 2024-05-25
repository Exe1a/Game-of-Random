# Import libary for games
from func import *
from random import randint

# Cards
def Cards_info():
    print_info('=== Правила игры: ===')
    print_info('Выбираете число 0-36')
    print_info('Стоимость игры 10 монет')
    print_info('Угадали - +30 монет')
    print_info('Нет - ничего')

def Cards():
    card = randint(0,36)
    print_info('Загадываем карту...')
    answer = input('Выберите номер карты: ')
    if type(answer) != int:
        print_info('Вам нужно выбрать 0-36.')
        answer = input('Выберите номер карты: ')
    elif not(0 <= answer <= 36):
        print_info('Вам нужно выбрать число.')
        answer = input('Выберите номер карты: ')
    print_info('Итак...')
    sleep(3)
    if card == answer:
        print_info('Молодец! Вы угадали!')
        print_info('Вы получаете 30 монет!')
        return True
    else:
        print_info('Неудача! В следующий раз повезет.')
        return False