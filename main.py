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


class Player:
    def __init__(self, name, score_categories):
        self.name = name
        self.scorecard = {
            category: None 
            for category 
            in score_categories
        }


class Game:
    def __init__(self):
        self.player_names = []
        self.score_categories = (
            "ones", 
            "twos", 
            "threes", 
            "fours", 
            "fives", 
            "sixes",
            "three_of_a_kind", 
            "four_of_a_kind", 
            "full_house",
            "small_straight", 
            "large_straight", 
            "yahtzee", 
            "chance"
        )

    def update_player_names(self):
        while True:
            new_player_response = input("Would you like to enter a player name (yes/no)?: ")
            if new_player_response.lower() in ['yes', 'y']:
                while True:
                    name_response = input("Please enter a player name: ")
                    self.player_names.append(name_response)
                    break
            elif new_player_response.lower() in ['no', 'n']:
                break
            else:
                print("Please enter a valid response!")

    def get_player_names(self):
        return self.player_names
    
    def play_round(self):
        pass


def main():
    
    game = Game()
    game.update_player_names()
    game.play_round()
    
    

if __name__ == "__main__":
    main()