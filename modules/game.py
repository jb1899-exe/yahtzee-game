from modules.die import Die
from modules.player import Player


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
    
    def roll_round(self, dice_result = None, to_roll = ["a", "b", "c", "d", "e"]):
        if dice_result is None:
            dice_result = {}
        for die_id in to_roll:
            die = Die()
            roll_result = die.get_value()
            dice_result.update({die_id: roll_result})
        return dice_result
    
    def reroll_round(self, initial_roll):
        id_reroll = []
        for id in ['a', 'b', 'c', 'd']:
            while True:
                id_reroll_input = input(f"Would you like to reroll '{id.upper()}'? (yes/no): ").lower()
                if id_reroll_input in ['yes', 'y']:
                    id_reroll.append(id)
                    break
                elif id_reroll_input in ['no', 'n']:
                    break
                else:
                    print("Please enter a valid response!")

        dice_result = self.roll_round(initial_roll, id_reroll)
        return dice_result
                
    def play_round(self, player = None):
        roll = self.roll_round(dice_result = {}) 
        for die, result in roll.items():
            print(f"Die {die.upper()} rolled {result}!")

        reroll_attempts = 0
        while True :
            reroll_input = input(f"\nWould you like to reroll? {reroll_attempts}/2 attempts (yes/no): ").lower()
            if reroll_input in ['yes', 'y'] and reroll_attempts < 2:
                reroll_attempts += 1
                roll = self.reroll_round(roll)
                print("\n")
                for die, result in roll.items():
                    print(f"Die {die.upper()} rolled {result}!")
            elif reroll_input in ['no', 'n']:
                break
            else:
                print("Please enter a valid response!")