class Player:
    '''
    Creates an instance for the human or the computer player
    '''
    def __init__(self, name):
        self.__name = name

    __shot_count = 0

    @property
    def name(self):
        return self.__name

    def add_shot(self):
        '''Increment the shot counter by one'''
        self.__shot_count += 1
