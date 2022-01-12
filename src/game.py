import os
from src.classes.ships import *
from src.classes.player import Player

# The defined game rule requires the following number of ships
list_of_ships = [
    [1, AircraftCarrier()],
    [1, Battleship()],
    [1, Cruiser()],
    [2, Destroyer()],
    [2, Submarine()]
]


def choose_name():
    print('\nChoose a name for your captain (maximum 16 character)')
    name = input('Name: ')

    if len(name) > 16:
        name = name[:16]

        def agree_on_name():
            print(f'Your name will be: {name}')
            agreement = input('Is this ok? (y)es/(n)o ').lower()
            if agreement in ('n','no'):
                return choose_name()
            elif agreement in ('y','yes'):
                return name
            else:
                print(f'Invalid answer:\n{agreement}')
                return agree_on_name()
        
        name = agree_on_name()

    return name


def chose_placement_type():
    '''
    Allows the user to chose from random or manual ship placement
    '''
    print('Do you want to place your ships on the grid or want it randomly placed?')
    print('Type (R)andom or (M)anual: ')


def start_game():
    '''Game entry point'''
    os.system('cls||clear')

    player = Player(choose_name())
    placement = chose_placement_type()
