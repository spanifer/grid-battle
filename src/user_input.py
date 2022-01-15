import re


def take_shot_inp(prompt_msg, board_obj):
    '''
    Prompts the player to enter x, y coords
    separated by a space or a comma
    Using a RegEx validate coords in board range
    Returns the coords as a tuple first element,
    The second element is the return value from take_dir
    '''
    coords = input(prompt_msg)

    regex = re.compile(r'^ *(\d+)[ ,](\d+) *$').match(coords)

    if regex:
        # Visual gameboard is indexed from 1 so substract 1
        x, y = int(regex.group(1))-1, int(regex.group(2))-1
        range_is_valid = board_obj.validate_range(x, y)

        if not range_is_valid:
            print('Coordinate out of range.')
            return take_shot_inp(prompt_msg, board_obj)

        already_shot = board_obj.shot_taken(x, y)
        if already_shot:
            print('You have already shot there.')
            return take_shot_inp(prompt_msg, board_obj)

        return board_obj.take_shot(x, y)
    else:
        print('Could\'t find a coordinate in your input.')
        return take_shot_inp(prompt_msg, board_obj)
