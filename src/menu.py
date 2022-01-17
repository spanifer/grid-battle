import os
from src.classes.game import Game
from src.high_score import print_high_scores


def print_title():
    '''
    Displays the game title
    '''
    # Centered game title
    print(f'\n\n\n\n\n{" "*34}Grid Battle'
          f'\n{" "*30}(a battleships game)')


def print_options(invalid_str=None):
    '''
    Displays the options
    And prints optional message for invalid selected option
    '''
    print('\n\n\n Type one of the following option as its '
          'number and press Enter')
    print('\n 1: Start a new game')
    print(' 2: High scores')
    print(' 3: Game rules')

    if invalid_str is not None:
        print(f'\n  Invalid choice:\n  > {invalid_str}\n  '
              'Please type a number from 1 to 3')


def clear_run_input(func):
    '''Wraps the func between clear screen and input request'''
    os.system('cls||clear')
    func()
    input('Press Enter to return to menu...')


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
        Game()
    elif option == '2':
        clear_run_input(print_high_scores)
    elif option == '3':
        print('Rules')
        input('Press Enter to return to menu...')

    return menu()
