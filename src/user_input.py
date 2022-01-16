import re


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
