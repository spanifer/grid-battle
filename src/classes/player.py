from src.classes.board import Board


class Player:
    '''
    Creates an instance for the human or the computer player
    '''
    def __init__(self, name, board=None):
        self.__name = name
        self.board = board

    __shot_count = 0

    @property
    def name(self):
        return self.__name

    @property
    def shots(self):
        return self.__shot_count

    @property
    def ships(self):
        return self.board.ships

    def add_shot(self):
        '''Increment the shot counter by one'''
        self.__shot_count += 1

    def add_new_board(self):
        '''A Board instance can be added later if none defined at init'''
        self.board = Board(self.__name)


class Computer(Player):
    '''
    Creates a computer specific player instance
    '''
    def __init__(self, player_name, board=None):
        npc_name = 'Computer'
        self.__normal_difficulty = True
        if player_name.lower() == npc_name.lower():
            npc_name = 'Quantum Computer'  # 😂
            self.__normal_difficulty = False
        Player.__init__(self, npc_name, board)

    def guess(self, player_board):
        '''Returns the computer random guess'''
        if self.__normal_difficulty:
            return player_board.rand_coord()
        # Easter egg
        try:  # Test just in case
            ship = player_board.ships.pop()
        except KeyError:
            self.__normal_difficulty = True
            return self.guess(player_board)

        player_board.ships.add(ship)

        return ship.get_a_pos()
