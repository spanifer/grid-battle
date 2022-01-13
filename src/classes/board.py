import random


class Board:
    '''
    Creates an instance of a game board
    '''
    def __init__(self, owner):
        self.owner = owner
        self.board = self.__create_board()
        self.__width = len(self.board[0])
        self.__height = len(self.board)

    # Chars used on the board
    __charList = {
            'empty': '.',
            'part': '0',
            'damaged': 'X',
            'miss': 'm'
    }

    # Directions vector list in order as
    # UP, RIGHT, DOWN, LEFT
    __directions = [
        (0, -1),
        (1, 0),
        (0, 1),
        (-1, 0)
    ]

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def __create_board(self, x=12, y=12):
        '''
        Initializes the game board
        as a list of lists
        maximum 12 width
        '''
        board = []
        for _ in range(y):
            row = []
            for _ in range(x):
                row.append(self.__charList['empty'])
            board.append(row)

        return board

    def __rand_coord(self):
        return (random.randrange(self.width), random.randrange(self.height))

    def __rand_directions(self):
        '''
        Generator that gives a random direction
        Or raises StopIteration exception if list of directions got cleared
        '''
        directions = self.__directions.copy()
        while directions:
            yield directions.pop(random.randrange(len(directions)))

    def __validate_range(self, x, y):
        '''
        Checks if the vector is within the board range
        Returns False if it is not, otherwise True
        '''
        if x not in range(self.__width) or y not in range(self.__height):
            return False
        return True

    def __validate_shot(self, x, y):
        '''
        Checks if the coordinate have already received a shot
        Return False if it did, otherwise True
        '''
        if self.board[y][x] not in (self.__charList['damaged'],
                                    self.__charList['miss']):
            return False
        return True

    def __is_empty(self, x, y):
        '''
        Checks if the coordinate is empty
        Returns False if not, otherwise True
        '''
        if self.board[y][x] == self.__charList['empty']:
            return True
        return False

    def __find_ship_coords(self, ship, origin, direction):
        '''
        Checks if board is empty on given direction for given ship
        from the chosen origin
        Return a list of coords that the ship can be placed on
        '''
        length = ship.length - 1
        x, y = origin
        dx, dy = direction

        result = [origin]  # Add origin to the list

        while length:
            length -= 1
            nx, ny = (x+dx, y+dy)
            if self.__validate_range(nx, ny) and self.__is_empty(nx, ny):
                result.append((nx, ny))
                x, y = nx, ny
            else:
                return False

        return result

    def random_placement(self, ship):
        '''
        Place a ship on the board in a random position
        Will call itself recursively if unable to place ship and try again
        with another random position
        If finds a suitable position, place the value(s) on the board
        '''
        # Find a valid coordinate on the board
        x, y = self.__rand_coord()
        while not self.__is_empty(x, y):
            x, y = self.__rand_coord()

        # Call random directions iterator
        dirs = self.__rand_directions()
        direction = None
        found_coords = None

        while True:
            try:
                direction = next(dirs)
            except StopIteration:
                # If not valid in any direction
                return self.random_placement(ship)
            found_coords = self.__find_ship_coords(ship, (x, y), direction)
            if found_coords:
                # If ship can be placed on given direction break the loop
                break

        for (x, y) in found_coords:
            self.board[y][x] = self.__charList['part']

    def place_ship(self, ship, origin, direction):
        '''
        Place the ship on the grid
        The origin, and direction parameters are vectors
        '''
        pass

    def take_shot(self, x, y):
        '''
        Checks and modifies board for the given coordinates
        or return false if the shot is invalid
        '''
        pass
