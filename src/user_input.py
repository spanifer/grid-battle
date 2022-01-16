import re


def choose_name():
    '''
    Request the user for a character name and confirms the te selected name
    '''
    print('\nChoose a name for your captain (min 3 maximum 16 character)')
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


def take_dir(msg, board, ship, origin):
    '''
    Take user input for a choice of direction
    as defined in Board w,a,s,d for up,left,down,right
    Returns Board.place_ship() return value
    Alternatively recursively calls itself
    '''
    print(msg)

    dir_list = board.find_valid_dirs(ship, origin)
    valid_dir_list = [char.upper() for char, _ in dir_list]
    dir_input = input(f'Valid directions are: {", ".join(valid_dir_list) } > ')

    # Case insensitive match
    matched = re.compile(f'^[{"".join(valid_dir_list)}]',
                         re.I).match(dir_input)
    if not matched:
        print('No such direction.')
        return take_dir(msg, board, ship, origin)

    direction = matched.group()
    ship_placed = board.place_ship(ship, origin, direction)
    if ship_placed:
        return ship_placed


def take_coords(prompt_msg, board, ship):
    '''
    Using a RegEx validate coords
    Prompts the player to enter x, y coords
    separated by a space or a comma
    validated in board range
    Returns the coords as a tuple first element,
    The second element is the return value from take_dir
    '''
    coords = input(prompt_msg)

    # Ignores trailing whitespaces, requires 2 digits
    # separated by a space or comma
    # Captures digits in group
    matched = re.compile(r'^ *(\d+)[ ,](\d+) *$').match(coords)

    if not matched:
        print('Could\'t find a coordinate in your input.')
        return take_coords(prompt_msg, board, ship)

    # Visual gameboard is indexed from 1 so substract 1
    x, y = int(matched.group(1))-1, int(matched.group(2))-1
    range_is_valid = board.validate_range(x, y)

    # Submarine case 👇
    available_dirs = None
    if ship.length > 1:
        available_dirs = board.find_valid_dirs(ship, x, y)

    if not range_is_valid:
        print('Coordinates out of range.')
        return take_coords(prompt_msg, board, ship)

    coord_is_empty = board.is_empty(x, y)
    if not coord_is_empty:
        print('That space is already occupied.')
        return take_coords(prompt_msg, board, ship)

    if available_dirs:
        return ((x, y),
                take_dir('Choose the direction your ship lays.',
                         board, ship, (x, y)))
    elif available_dirs is None:
        board = board.place_ship(ship, (x, y), None)
        return ((x, y), )
    # available_dirs is an empty list here
    else:
        print('Your ship will not fit there.')
        return take_coords(prompt_msg, board, ship)


def take_shot_inp(prompt_msg, board):
    '''
    Prompts the player to enter x, y coords
    separated by a space or a comma
    Using a RegEx validate coords in board range
    Returns the coords as a tuple first element,
    The second element is the return value from take_dir
    '''
    coords = input(prompt_msg)

    matched = re.compile(r'^ *(\d+)[ ,](\d+) *$').match(coords)

    if not matched:
        print('Could\'t find a coordinate in your input.')
        return take_shot_inp(prompt_msg, board)

    # Visual gameboard is indexed from 1 so substract 1
    x, y = int(matched.group(1))-1, int(matched.group(2))-1
    range_is_valid = board.validate_range(x, y)

    if not range_is_valid:
        print('Coordinate out of range.')
        return take_shot_inp(prompt_msg, board)

    new_shot = board.validate_shot(x, y)
    if not new_shot:
        print('You have already shot there.')
        return take_shot_inp(prompt_msg, board)

    return board.take_shot(x, y)
