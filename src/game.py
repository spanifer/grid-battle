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


def take_dir(msg, board_obj, ship, origin):
    '''
    Take user input for a choice of direction
    as defined in Board w,a,s,d for up,left,down,right
    Returns Board.place_ship() return value
    Alternatively recursively calls itself
    '''
    print(msg)

    dir_list = board_obj.find_valid_dirs(ship, origin)
    valid_dir_list = [char.upper() for char, _ in dir_list]
    dir_input = input(f'Valid directions are: {", ".join(valid_dir_list) } > ')

    regex = re.compile(f'^[{"".join(valid_dir_list)}]', re.I).match(dir_input)
    if regex:
        direction = regex.group()
        ship_placed = board_obj.place_ship(ship, origin, direction)
        if ship_placed:
            return ship_placed
    else:
        print('No such direction.')
        return take_dir(msg, board_obj, ship, origin)


def take_coords(prompt_msg, board_obj, ship):
    '''
    Prompts the player to enter x, y coords
    separated by a space or a comma
    Using a RegEx validate coords in board range
    Returns the coords as a tuple first element,
    The second element is the return value from take_dir
    '''
    coords = input(prompt_msg)

    # Ignores trailing whitespaces, requires 2 digits
    # separated by a space or comma
    # Captures digits in group
    regex = re.compile(r'^ *(\d+)[ ,](\d+) *$').match(coords)

    if regex:
        # Visual gameboard is indexed from 1 so substract 1
        x, y = int(regex.group(1))-1, int(regex.group(2))-1
        range_is_valid = board_obj.validate_range(x, y)

        # Submarine case 👇
        available_dirs = None
        if ship.length > 1:
            available_dirs = board_obj.find_valid_dirs(ship, (x, y))

        if not range_is_valid:
            print('Coordinates out of range.')
            return take_coords(prompt_msg, board_obj, ship)

        coord_is_empty = board_obj.is_empty(x, y)
        if not coord_is_empty:
            print('That space is already occupied.')
            return take_coords(prompt_msg, board_obj, ship)

        if available_dirs:
            return ((x, y),
                    take_dir('Choose the direction your ship lays.',
                             board_obj, ship, (x, y)))
        elif available_dirs is None:
            board_obj = board_obj.place_ship(ship, (x, y), None)
            return ((x, y), )
        else:
            print('Your ship will not fit there.')
            return take_coords(prompt_msg, board_obj, ship)
    else:
        print('Could\'t find a coordinate in your input.')
        return take_coords(prompt_msg, board_obj, ship)


def placement_loop(p_type, player, computer):
    '''
    Loops through the list of ships for the given placement type
    '''
    ships = list_of_ships.copy()

    if p_type == 'random':
        while ships:
            ship = ships.pop(0)
            player.board_obj.random_placement(ship)
            computer.board_obj.random_placement(ship)
        game_board(player, computer)

    elif p_type == 'manual':
        while ships:
            ship = ships.pop(0)
            game_board(player, computer)
            take_coords(
                f'Choose a coordinate for your {ship.name}: ',
                player.board_obj,
                ship)
            computer.board_obj.random_placement(ship)
        game_board(player, computer)


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
