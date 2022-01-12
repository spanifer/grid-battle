import os
from src.classes.ships import *
from src.classes.player import Player
from src.classes.board import Board

# The defined game rule requires the following number of ships
list_of_ships = [
    [1, AircraftCarrier()],
    [1, Battleship()],
    [1, Cruiser()],
    [2, Destroyer()],
    [2, Submarine()]
]


def choose_name():
    '''
    Request the user for a character name and confirms the te selected name
    '''
    print('\nChoose a name for your captain (maximum 16 character)')
    name = input('Name: ')

    def agree_on_name():
        nonlocal name

        print(f'Your captains name will be: {name}')
        agreement = input('Is this ok? (y)es/(n)o ').lower()
        if agreement in ('n', 'no'):
            return choose_name()
        elif agreement in ('y', 'yes'):
            return name
        else:
            print(f'Invalid answer:\n> {agreement}\n')
            return agree_on_name()

    if len(name) > 16:
        name = name[:16]

    return agree_on_name()


def choose_placement_type():
    '''
    Allows the user to choose from random or manual ship placement
    '''
    print('Do you want to place your ships on the grid or want it'
          'randomly placed?')
    placement_type = input('Type (R)andom or (M)anual: ').lower()

    if placement_type in ('r', 'random'):
        return 'random'
    elif placement_type in ('m', 'manual'):
        return 'manual'
    else:
        print(f'Invalid answer:\n> {placement_type}\n')
        return choose_placement_type()


def start_game():
    '''Game entry point'''
    os.system('cls||clear')

    player = Player(choose_name())

    print(f'Name is {player.name}')

    placement = choose_placement_type()

    print(f'You chose {placement} placement')
