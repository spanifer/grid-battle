import os
from src.user_input import take_shot_inp


class Game:
    '''
    Game class, main game course
    '''
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.__is_player_turn = False

    def game_loop(self):
        '''Initiates the game loop'''
        while self.__check_win():
            self.__is_player_turn = not self.__is_player_turn
            if self.__is_player_turn:
                self.__player_turn()
            else:
                self.__computer_turn()

    def __player_turn(self):
        '''Player turn'''
        is_hit = take_shot_inp(
            'Take a guess as the number of '
            'the column and row like: X,Y or X Y'
            '\n Your guess is: ',
            self.computer.board_obj)

        self.player.add_shot()
        self.game_board()

        if is_hit:
            print('Hit!')
        else:
            print('Miss...')

    def __computer_turn(self):
        '''Computer turn'''
        is_hit = take_shot_inp(prompt_msg, board_obj)

    def __check_win(self):
        '''Checks if one of the players lost all of their ships'''
        if (len(self.player.ships_pos) and
                len(self.computer.ships_pos)):
            return True
        return False

    def game_board(self):
        '''
        Prints the game area with the player and computer boards,
        shot count and player info
        Each column of the board row have 3 char length
        and indexed rows and columns

        '''
        player = self.player
        computer = self.computer

        board_width = len(player.board[0])
        board_height = len(player.board)

        os.system('cls||clear')
        print(f'\n {player.name}'
              f'{" "*(41 - len(player.name) + 1)}{computer.name}')

        def create_vertical_indexes():
            # creates a string with the column indexes (the x axis)
            row = '  '  # leave space for horizontal indexes
            for column_i in range(1, board_width+1):
                # Add two spaces for a single digit, one space for two digits
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
