import os
import re
from src.classes.ships import *
from src.classes.player import Player

# The defined game rule requires the following number of ships
list_of_ships = [
    AircraftCarrier(),
    Battleship(),
    Cruiser(),
    Destroyer(),
    Destroyer(),
    Submarine(),
    Submarine()
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
    elif len(name) < 3:
        print('Name should be at least 3 characters.')
        return choose_name()

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
    and indexed rows and columns

    '''
    board_width = len(player.board[0])
    board_height = len(player.board)

    os.system('cls||clear')
    print(f'\n {player.name}{" "*(41 - len(player.name) + 1)}{computer.name}')

    def create_vertical_indexes():
        # creates a string with the column indexes (the x axis)
        row = '  '  # leave space for horizontal indexes
        for column_i in range(1, board_width+1):
            # Add two spaces for a single digit, and one space for two digits
            row += f" {column_i}" if column_i // 10 else f" {column_i} "

        return row

    vertical_indexes = create_vertical_indexes()
    vertical_indexes += ' '*(42-len(vertical_indexes)) 
    vertical_indexes += create_vertical_indexes()
    print(vertical_indexes)

    for row_i in range(1, board_height+1):
        row = ''
        ind = f"{'' if row_i // 10 else ' '}{row_i}"
        row += ind
        for col_i in range(board_width):
            row += f' {player.board[row_i-1][col_i]} '

        row += ' '*4
        row += ' '*(40-len(row))
        row += ind
        for col_i in range(board_width):
            row += f' {computer.board[row_i-1][col_i]} '  # ❗ Change to mask

        print(row)


def take_coords(prompt_msg, board_obj):
    '''
    Prompts the player to enter x, y coords
    separated by a space or a comma using a RegEx
    Validate cords in board range
    Returns the coords as a tuple(x, y)
    or 'err_msg'
    '''
    coords = input(prompt_msg)

    # Ignores trailing whitespaces, requires 2 digits
    # separated by a space or comma
    # Captures digits in group
    regex = re.compile(r'^ *(\d+)[ ,](\d+) *$').match(coords)
    if regex:
        x, y = int(regex.group(1)), int(regex.group(2))
        # Visual gameboard is indexed from 1 so substract 1
        if board_obj.validate_range(x-1, y-1):
            # This syntax returns a tuple, not required to specify it
            # like (x, y)
            return x, y
        else:
            raise ValueError('Coordinates out of range.')
    else:
        raise ValueError('Could\'t find coordinates in your input.')

def placement_loop(p_type, player, computer):
    # random
    ships = list_of_ships.copy()

    if p_type == 'random':
        while ships:
            ship = ships.pop(0)
            player.board_obj.random_placement(ship)
            computer.board_obj.random_placement(ship)
    elif p_type == 'manual':
        while ships:
            ship = ships.pop(0)
            try:
                x, y = take_coords(f'Choose a coordinate for your {ship.name}: ',
                                   player.board_obj)
            except ValueError as err_msg:
                # NOTE: if an edge case raises the value error
                # the meassage isn't user friendly
                print(err_msg)
                ships.insert(0, ship)
                break


def start_game():
    '''Game entry point'''
    os.system('cls||clear')

    player = Player(choose_name())
    player.add_new_board()

    computer = Player('Computer')
    computer.add_new_board()

    print(f'Name is {player.name}')

    placement_type = choose_placement_type()

    placement_loop(placement_type, player, computer)

    game_board(player, computer)
