# Import functions and games
from games import *
from func import *

# Welcome message
print_info('=== Добро пожаловать! ===')

# Total money
money = 100

# Main
while True:
    # Start choosing
    choose = ChooseGame()
    if choose == 1: # Cards
        # Explain the game's rules or not
        explain = input('Вам нужно объяснить правила игры (y/n): ')
        if explain.lower() == 'y': Cards_info()
        elif explain.lower() == 'n': pass
        # Only 'y' or 'n'
        else:
            print_info('Нужно ввести y или n.')
            explain = input('Вам нужно объяснить правила игры (y/n): ')

        # Want to play or not
        continueGame = input('Вы хотите продолжить? (y/n): ')
        if continueGame.lower() == 'y':
            # Start Cards
            money -= 10
            Cards()
            if Cards: money += 30 # Win or lose
        elif continueGame.lower() == 'n': pass # Change mind
        # Only 'y' or 'n'
        else:
            print_info('Нужно ввести y или n.')
            continueGame = input('Вы хотите продолжить? (y/n): ')

    # Close the program
    else:
        exit()