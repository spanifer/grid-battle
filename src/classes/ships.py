class Ship:
    '''
    Creates an instance of the main ship class
    '''
    def __init__(self, length, name):
        self.__length = length
        self.__name = name
        self.positions = set()

    @property
    def name(self):
        return self.__name

    @property
    def length(self):
        return self.__length

    def add_pos(self, coord):
        self.positions.add(coord)
        return self

    def check_pos(self, coord):
        return True if coord in self.positions else False

    def take_hit(self, coord):
        '''
        Checks if the ship is on the given coordinate
        Returns:
            - False if it is not
            - True if ship got a hit
            - self if ship sank
        '''
        try:
            self.positions.remove(coord)
        except KeyError:
            return False
        if not len(self.positions):
            return self
        return True


# The following subclasses are specific ships with properties

class AircraftCarrier(Ship):
    '''
    Creates Aircraft Carrier subclass
    with specific properties
    '''
    def __init__(self):
        Ship.__init__(self, 5, 'Aircraft Carrier')


class Battleship(Ship):
    '''
    Creates Battleship subclass
    with specific properties
    '''
    def __init__(self):
        Ship.__init__(self, 4, 'Battleship')


class Cruiser(Ship):
    '''
    Creates Cruiser subclass
    with specific properties
    '''
    def __init__(self):
        Ship.__init__(self, 3, 'Cruiser')


class Destroyer(Ship):
    '''
    Creates Destroyer subclass
    with specific properties
    '''
    def __init__(self):
        Ship.__init__(self, 2, 'Destroyer')


class Submarine(Ship):
    '''
    Creates Submarine subclass
    with specific properties
    '''
    def __init__(self):
        Ship.__init__(self, 1, 'Submarine')
