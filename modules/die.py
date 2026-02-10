import random

class Die:
    def __init__(self):
        '''Initialises random value for die.'''
        self.value = random.randint(1, 6)

    def roll(self):
        '''Generates a new random value for die.'''
        self.value = random.randint(1, 6)

    def get_value(self):
        '''Returns value of die.'''
        return self.value