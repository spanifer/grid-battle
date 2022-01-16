import random


class Board:
    '''
    Creates an instance of a game board
    '''
    def __init__(self, owner):
        self.__width = 12
        self.__height = 12
        self.owner = owner
        self.board = self.__create_board()
        self.ships = set()  # list of ships

        # list of all available position that can take a shot
        # the computer will only call random once on self.fog length
        self.fog = [(x, y) for x in range(self.width)
                    for y in range(self.height)]

    # Chars used on the board
    __charList = {
            'empty': '.',
            'part': '0',
            'hit': 'X',
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
    def get_dirs(self):
        return zip(('w', 'd', 's', 'a'), self.__directions)

    def __dir_from_char(self, inp_char):
        for char, vector in self.get_dirs:
            if char == inp_char.lower():
                return vector

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    def get_occupied_coords(self):
        '''Returns the ships positions in one set'''
        return {coord for ship in self.ships for coord in ship.positions}

    def __create_board(self):
        '''
        Initializes the game board
        as a list of lists
        maximum 12 width
        '''
        board = []
        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(self.__charList['empty'])
            board.append(row)

        return board

    def rand_coord(self):
        '''Returns a random coord from self.fog'''
        return self.fog[random.randrange(len(self.fog))]

    def __rand_directions(self):
        '''
        Generator that gives a random direction
        Or raises StopIteration exception if list of directions got cleared
        '''
        directions = self.__directions.copy()
        while directions:
            yield directions.pop(random.randrange(len(directions)))

    def validate_range(self, x, y):
        '''
        Checks if the vector is within the board range
        Returns False if it is not, otherwise True
        '''
        if x not in range(self.__width) or y not in range(self.__height):
            return False
        return True

    def validate_shot(self, x, y):
        '''
        Checks if the coordinate have already received a shot
        Return False if it did, otherwise True
        '''
        return (x, y) in self.fog

    def is_empty(self, x, y):
        '''
        Checks if the coordinate is empty
        Returns False if not, otherwise True
        '''
        if (x, y) in self.get_occupied_coords():
            return False
        return True

    def __find_ship_coord(self, ship, origin, direction):
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
            if self.validate_range(nx, ny) and self.is_empty(nx, ny):
                result.append((nx, ny))
                x, y = nx, ny
            else:
                return False

        return result

    def find_valid_dirs(self, ship, origin):
        '''
        Finds available directions
        Returns the found directions in a list of character values
                                    and coresponding vector values
        Otherwise returns an empty list
        '''
        found_directions = []
        for (char, direct) in self.get_dirs:
            if self.__find_ship_coord(ship, origin, direct):
                found_directions.append((char, direct))

        return tuple(found_directions)

    def random_placement(self, ship, hide=False):
        '''
        Place a ship on the board in a random position
        Will call itself recursively if unable to place ship and try again
        with another random position
        If finds a suitable position, place the value(s) on the board
        Also adds ship to the self.ships set and adds the Ship.positions
        '''
        # Find a valid coordinate on the board
        x, y = self.rand_coord()
        while not self.is_empty(x, y):
            x, y = self.rand_coord()

        # Create random directions iterator
        dirs = self.__rand_directions()
        direction = None
        found_coords = None

        while True:
            try:
                direction = next(dirs)
            except StopIteration:
                # If not valid in any direction
                return self.random_placement(ship)
            found_coords = self.__find_ship_coord(ship, (x, y), direction)
            if found_coords:
                # If ship can be placed on given direction break the loop
                break

        self.ships.add(ship)
        for (x, y) in found_coords:
            ship.add_pos((x, y))
            if not hide:
                self.board[y][x] = self.__charList['part']

    def place_ship(self, ship, origin, direction_inp, hide=False):
        '''
        Place the ship on the grid
        origin parameter is a vectors
        direction is a character
        Returns True if placement is successfull, otherwise False
        Also adds ship to the self.ships set and adds the Ship.positions
        '''
        if ship.length == 1:
            self.board[origin[1]][origin[0]] = self.__charList['part']
            self.ships.add(ship)
            ship.add_pos(origin)
            return True

        direction = self.__dir_from_char(direction_inp)
        found_ship_coords = self.__find_ship_coord(ship, origin, direction)
        if found_ship_coords:
            self.ships.add(ship)
            for x, y in found_ship_coords:
                ship.add_pos((x, y))
                if not hide:
                    self.board[y][x] = self.__charList['part']
            return True

        return False

    def take_shot(self, x, y):
        '''
        Checks and modifies board for the given coordinates
        Returns True if ship got hit, False for miss, or <ship> if sank
        '''
        # It's getting worse
        for ship in self.ships:
            hit = ship.take_hit((x, y))  # 'hit' can be the 'ship' if sank
            self.ships.discard(hit)  # removes from the 'ships' if it is

            if hit:
                self.board[y][x] = self.__charList['hit']
                self.fog.remove((x, y))
                return hit

        self.board[y][x] = self.__charList['miss']
        self.fog.remove((x, y))
        return False
