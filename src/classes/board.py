class Board:
    '''
    Creates an instance of a game board
    '''
    def __init__(self, owner = 'npc'):
        self.owner = owner
        self.board = self.__create_board()

    # Chars used on the board
    __charList = {
            'empty':'.',
            'part':'0',
            'damaged':'X',
            'miss': 'm'
    }

    # Directions vector list in order as
    # UP, RIGHT, DOWN, LEFT
    __directions = [
        [0,1],
        [1,0],
        [0,-1],
        [-1,0]
    ]


    def __create_board(self, x = 13,y = 13):
        '''
        Initializes the game board
        as a list of lists
        '''
        board = []
        for i in range(y):
            row = []
            for j in range(x):
                row.append(self.__charList['empty'])
            board.append(row)
        
        return board

    def place_ship(self, origin, direction):
        '''
        Place the ship on the grid
        The origin, and direction parameters are vectors
        '''
        pass

    def __validate_vector(self, x, y):
        '''
        Checks if the vector is within the board range
        and if the coordinate have already received a shot
        '''
        pass

    def take_shot(self, x, y):
        '''
        Checks and modifies board for the given coordinates
        or return false if the shot is invalid
        '''
        pass
