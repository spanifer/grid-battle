class Ship:
    '''
    Creates an instance of the main ship class
    '''
    def __init__(self, length, name):
        self.__length = length
        self.__name = name


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
