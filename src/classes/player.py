from src.classes.board import Board


class Player:
    '''
    Creates an instance for the human or the computer player
    '''
    def __init__(self, name, board=None):
        self.__name = name
        self.__board = board
        self.board = None if not board else board.board

    __shot_count = 0

    @property
    def name(self):
        return self.__name

    @property
    def shots(self):
        return self.__shot_count

    @property
    def board_obj(self):
        return self.__board

    @property
    def ships_pos(self):
        return self.__board.ships_pos

    def add_shot(self):
        '''Increment the shot counter by one'''
        self.__shot_count += 1

    def add_new_board(self):
        '''A Board instance can be added later if none defined at init'''
        self.__board = Board(self.__name)
        self.board = self.__board.board


class Computer(Player):
    '''
    Creates a computer specific player instance
    '''
    def __init__(self, board=None):
        Player.__init__(self, self.__random_name(), board)

    def __random_name(self):
        return 'Computer'
