class Game:
    '''
    Game class
    '''
    def __init__(self, player=None, computer=None):
        self.player = player
        self.computer = computer

        self.game_loop()

    def game_loop(self):
        '''Initiates the game loop'''
