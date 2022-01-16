from src.classes.ships import *


# The defined game rule requires the following number of ships
list_of_ships = [
    AircraftCarrier,
    Battleship,
    Cruiser,
    Destroyer,
    Destroyer,
    Submarine,
    Submarine
]


# Chars used on the board
char_list = {
    'empty': '.',
    'part': '0',
    'hit': 'X',
    'miss': 'm'
}


# Directions vector list in order as
# UP, RIGHT, DOWN, LEFT
DIRECTIONS = [
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]
