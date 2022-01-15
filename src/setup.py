import os
import re
from src.classes.ships import *
from src.classes.player import Player, Computer
from src.classes.game import Game

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
        print('Name is longer than 16 characters.')
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


def random_placement(game):
    '''
    Loops through the list of ships and randomly place them on board
    '''
    ships = list_of_ships.copy()

    while ships:
        ship = ships.pop(0)
        game.player.board_obj.random_placement(ship)
        game.computer.board_obj.random_placement(ship)
    game.game_board()


def manual_placement(game):
    '''
    Loops through the list of ships
    and prompts the player to give coordinates to place them on board
    '''
    ships = list_of_ships.copy()

    while ships:
        ship = ships.pop(0)
        game.game_board()
        take_coords(
            f'Choose a coordinate for your {ship.name}: ',
            game.player.board_obj,
            ship)
        game.computer.board_obj.random_placement(ship)
    game.game_board()


def init_game():
    '''Game entry point'''
    os.system('cls||clear')

    player = Player(choose_name())
    player.add_new_board()

    computer = Computer()
    computer.add_new_board()

    print(f'Name is {player.name}')

    placement_type = choose_placement_type()

    game = Game(player, computer)

    # Placement loop
    if placement_type == 'random':
        random_placement(game)
    elif placement_type == 'manual':
        manual_placement(game)

    game.game_loop()
