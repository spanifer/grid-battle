import os
from src.classes.ships import *


# The defined game rule requires the following number of ships
no_of_ships = [
    [1, AircraftCarrier()],
    [1, Battleship()],
    [1, Cruiser()],
    [2, Destroyer()],
    [2, Submarine()]
]

def start_game():
    '''Game entry point'''
    os.system('cls||clear')

    print('Game')
    for ships in no_of_ships:
        print(ships[0], ships[1].name)