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
            if new_player_response.lower() in['yes', 'y']:
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
    
    def roll_round(self, dice_result = None, keep = ["a", "b", "c", "d", "e"]):
        if dice_result is None:
            dice_result = {}
        for die_id in keep:
            die = Die()
            roll_result = die.get_value()
            dice_result.update({die_id: roll_result})
        return dice_result
            


def main():
    
    game = Game()
    # game.update_player_names()
    for round in range(1, 14):

        print(f"Round {round}!\n")

        # play_round
        initial_roll = game.roll_round(dice_result = {}) 
        for die, result in initial_roll.items():
            print(f"Die {die.upper()} rolled {result}!")

        reroll_attempts = 0
        while True and reroll_attempts < 2:
            reroll_input = input("\nWould you like to reroll? (yes/no): ")
            if reroll_input.lower() in ['yes', 'y']:
                reroll_attempts += 1
                game.roll_round(initial_roll)
                for die, result in initial_roll.items():
                    print(f"Die {die.upper()} rolled {result}!")
            elif reroll_input.lower() in ['no', 'n']:
                break
            else:
                print("Please enter a valid response!")

        break # for testing
    
    

if __name__ == "__main__":
    main()