from src.settings import list_of_ships, char_list as chrl
from src.classes.board import Board


def print_game_rules():
    '''Prints the game rules'''
    l = len(list_of_ships)
    b = Board(None)
    print(
        '\n Battleships game is a two player turn based game played on a grid'
        '\n\n The player who first destroy the enemy fleet will win the game\n'
        'and if you as the player achieve a highscore, it can be added on to\n'
        'the publicly available highscore ranking table.'
        '\n\n How to play:'
        f'\nBoth players own their own {b.width} by {b.height} grid.'
        f'\nEach player places {l} different length ships on their board. You '
        'can chose\nto place yours manually. This case, entering the column '
        'number separated by a \nspace or a comma followed by the row number, '
        'for example 4 5 or 4,5\nAfter that you need to choose the direction '
        'which the ship lays by entering\n one of W A S D as in the direction '
        'keys.\nAlternatively you can choose to get your ships placed randomly'
        '\nAfter placing the ships the battle begins and each player take a '
        'guess\non a position. If a ship gets a hit the part character'
        f' [ {chrl["part"]} ] change to [ {chrl["hit"]} ]'
        f'\nIf it is a miss you will see [ {chrl.get("miss")} ] character '
        f'replace the [ {chrl.get("empty")} ]'
        '\n\n Good luck, and make sure to choose a \'good\' name.'
        )
