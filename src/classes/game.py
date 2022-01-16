import os
from src.classes.player import Player, Computer
from src.classes.ships import Ship
from src.data import list_of_ships
from src.user_input import (choose_name, choose_placement_type,
                            take_coords, take_shot_inp)


class Game:
    '''
    Game class, main game course
    '''
    def __init__(self):
        self.player = None
        self.computer = None
        self.__is_player_turn = False
        self.__init_game()

    def __init_game(self):
        '''Game entry point'''
        os.system('cls||clear')

        self.player = Player(choose_name())
        self.player.add_new_board()

        self.computer = Computer(self.player.name)
        self.computer.add_new_board()

        print(f'Name is {self.player.name}')

        placement_type = choose_placement_type()

        # Placement loop
        if placement_type == 'random':
            self.__random_placement()
        elif placement_type == 'manual':
            self.__manual_placement()

        self.__game_loop()

    def __random_placement(self):
        '''
        Loops through the list of ships and randomly place them on board
        '''
        ships = list_of_ships.copy()

        while ships:
            ship = ships.pop(0)
            self.player.board.random_placement(ship())
            self.computer.board.random_placement(ship(), hide=True)
        self.__print_game_board()

    def __manual_placement(self):
        '''
        Loops through the list of ships
        and prompts the player to give coordinates to place them on board
        '''
        ships = list_of_ships.copy()

        while ships:
            ship = ships.pop(0)
            self.__print_game_board()
            take_coords(
                f'Choose a coordinate for your {ship().name}: ',
                self.player.board,
                ship())
            self.computer.board.random_placement(ship(), hide=True)
        self.__print_game_board()

    def __game_loop(self):
        '''
        Initiates the game loop
        Alternating between the player and computer turn
        '''
        while self.__check_win():
            self.__is_player_turn = not self.__is_player_turn
            if self.__is_player_turn:
                self.__player_turn()
            else:
                self.__computer_turn()

    def __player_turn(self):
        '''Player turn'''
        hit = take_shot_inp(
            'Take a guess as the number of '
            'the column and row like: X,Y or X Y'
            '\n Your guess is: ',
            self.computer.board)

        self.player.add_shot()
        self.__print_game_board()

        if not hit:
            print('Miss...')
        else:
            print('Hit!')
            if isinstance(hit, Ship):
                print(f'{hit.name} sank.')

        input('Press Enter to continue...')

    def __computer_turn(self):
        '''Computer turn'''
        comp_guess = self.computer.guess(self.player.board)
        hit = self.player.board.take_shot(*comp_guess)
        self.__print_game_board()

        if not hit:
            print(f'{self.computer.name} missed the shot.')
        else:
            print('You received a hit.')
            if isinstance(hit, Ship):
                print(f'{self.computer.name} sank your {hit.name}.')

    def __check_win(self):
        '''Checks if one of the players lost all of their ships'''
        return (len(self.player.ships) and
                len(self.computer.ships))

    def __print_game_board(self):
        '''
        Prints the game area with the player and computer boards, and names
        Each column of the board row have 3 char length
        and indexed rows and columns
        '''
        player_board = self.player.board.get_printable_board()
        computer_board = self.computer.board.get_printable_board()

        os.system('cls||clear')
        print(f'\n {self.player.name}'
              f'{" "*(41 - len(self.player.name) + 1)}{self.computer.name}')

        game_board = zip(player_board, computer_board)

        for row in game_board:
            print(''.join(row))
