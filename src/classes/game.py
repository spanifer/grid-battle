class Game:
    '''
    Game class, main game course
    '''
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
        self.__is_player_turn = False

        self.game_loop()

    def game_loop(self):
        '''Initiates the game loop'''
        while self.__check_win():
            self.__is_player_turn = not self.__is_player_turn
            if self.__is_player_turn:
                self.__player_turn()
            else:
                self.__computer_turn()

    def __player_turn(self):
        '''Player actions'''
        input('Choose where you would like to shoot: ')

    def __computer_turn(self):
        '''Computer actions'''

    def __check_win(self):
        '''Checks if one of the players lost all of their ships'''
        if self.player.ships and self.computer.ships:
            return True
