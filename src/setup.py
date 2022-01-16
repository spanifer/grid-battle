import os
from src.data import list_of_ships
from src.user_input import choose_name, choose_placement_type, take_coords
from src.classes.game import Game
from src.classes.player import Player, Computer


def random_placement(game):
    '''
    Loops through the list of ships and randomly place them on board
    '''
    ships = list_of_ships.copy()

    while ships:
        ship = ships.pop(0)
        game.player.board.random_placement(ship())
        game.computer.board.random_placement(ship(), hide=True)
    game.print_game_board()


def manual_placement(game):
    '''
    Loops through the list of ships
    and prompts the player to give coordinates to place them on board
    '''
    ships = list_of_ships.copy()

    while ships:
        ship = ships.pop(0)
        game.print_game_board()
        take_coords(
            f'Choose a coordinate for your {ship().name}: ',
            game.player.board,
            ship())
        game.computer.board.random_placement(ship(), hide=True)
    game.print_game_board()


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
