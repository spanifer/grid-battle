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

    def add_shot(self):
        '''Increment the shot counter by one'''
        self.__shot_count += 1

    def add_new_board(self):
        '''A Board instance can be added later if none defined at init'''
        self.__board = Board(self.__name)
        self.board = self.__board.board
