import os
from src.game import start_game


def print_title():
    '''
    Displays the game title
    '''
    # Centered game title
    print('\n\n\n\n\n                                  Grid Battle')
    print('                              (a battleships game)')


def print_options(invalid_str=None):
    '''
    Displays the options
    And prints optional message for invalid selected option
    '''
    print('\n\n\n Type one of the following option as its number and press Enter')
    print('\n 1: Start a new game')
    print(' 2: High scores')
    print(' 3: Game rules')

    if invalid_str is not None:
        print(f'\n  Invalid choice:\n  > {invalid_str}\n  Please type a number from 1 to 3')


def menu(option=None):
    '''
    (Re)displays the menu
    '''
    # Clear screen
    os.system('cls||clear')

    print_title()
    print_options(option)

    # Take user input
    option = input('\n ')

    if option == '1':
        start_game()
    elif option == '2':
        print('High scores')
    elif option == '3':
        print('Rules')
    else:
        menu(option)
