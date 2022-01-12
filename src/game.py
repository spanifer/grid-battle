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


def game_board(player, computer):
    '''
    Prints the game area with the player and computer boards,
    shot count and player info
    Each column of the board row have 3 char length

    '''
    board_width = len(player.board[0])
    board_height = len(player.board)

    os.system('cls||clear')
    print(f'\n {player.name}{" "*17}{computer.name}')
    print(f'{board_width} {board_height}')


def start_game():
    '''Game entry point'''
    os.system('cls||clear')

    player = Player(choose_name())
    player.add_new_board()

    computer = Player('Computer')
    computer.add_new_board()

    print(f'Name is {player.name}')

    placement = choose_placement_type()

    game_board(player, computer)

    if placement == 'random':
        # player.board.randomly_place_ships
        # invoke placement loop randomly
        pass
    else:
        # invoke placement loop manualy
        pass
