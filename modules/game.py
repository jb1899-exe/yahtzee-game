import time
from modules.die import Die
from modules.player import Player


class Game:
    '''Controls logic of Yahtzee game.'''

    def __init__(self):
        self.player_names: list = []

    
    def update_player_names(self):
        '''Updates list of player names as inputted in-game by players.'''

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
        '''Retrurns names of all active players as entered in-game.'''

        return self.player_names
    
    
    def roll_round(self, dice_result = None, to_roll = ["a", "b", "c", "d", "e"]):
        ''''''

        if dice_result is None:
            dice_result = {}
        for die_id in to_roll:
            die = Die()
            roll_result = die.get_value()
            dice_result.update({die_id: roll_result})
        return dice_result
    
    
    def reroll_round(self, initial_roll: dict[str, int]) -> dict[str, int]:
        ''''''

        id_reroll = []
        for id in ['a', 'b', 'c', 'd', 'e']:
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
    
    
    def upper_or_lower(self, player: 'Player', roll: dict[str, int]) -> None:
        '''Contains functionality for allowing player to select upper or lower scoring rules.'''

        while True:
            upper_lower_input = input("\nWould you like to score upper or lower? (upper/lower): ").lower()
            if upper_lower_input in ['upper', 'u']:
                self.play_upper(player, roll)
                break
            elif upper_lower_input in ['lower', 'l']:
                self.play_lower(player, roll)
                break
            else:
                print("\nPlease enter a valid response!")

                
    def play_upper(self, player: 'Player', roll: dict[str, int]) -> None:
        '''Scores roll with upper scoring rules and updates player scores.'''

        die_roll_values = {
            # key: die face value
            # value: count of face rolls
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0
        }
        # TODO: find iterable way of doing this
        for value in roll.values():
            if value == 1:
                die_roll_values[1] += 1
            elif value == 2:
                die_roll_values[2] += 1
            elif value == 3:
                die_roll_values[3] += 1
            elif value == 4:
                die_roll_values[4] += 1
            elif value == 5:
                die_roll_values[5] += 1
            elif value == 6:
                die_roll_values[6] += 1

        upper_scores = {key: key * value for key, value in die_roll_values.items()}

        player_scores = {}
        for key, value in upper_scores.items():
            if key == 1:
                player_scores['ones'] = value
            elif key == 2:
                player_scores['twos'] = value
            elif key == 3:
                player_scores['threes'] = value
            elif key == 4:
                player_scores['fours'] = value
            elif key == 5:
                player_scores['fives'] = value
            elif key == 6:
                player_scores['sixes'] = value

        # TODO: Find more efficient way of only showing availible categories.
        # Only calculate score for unused categories.

        for key, value in player.used_upper_categories.items():
            if value is True:
                del player_scores[key]

        player.add_upper_scores(player_scores)
            
        
    def play_lower(self, player: 'Player', roll: dict[str, int]) -> None:
        '''Scores roll with lower scoring rules and updates player scores.'''

        # TODO: rework lower scoring
        pass
    
        # die_roll_values = {
        #     # key: die face value
        #     # value: count of face rolls
        #     1: 0, 
        #     2: 0, 
        #     3: 0, 
        #     4: 0, 
        #     5: 0, 
        #     6: 0
        # }
        # for value in roll.values():
        #     if value == 1:
        #         die_roll_values[1] += 1
        #     elif value == 2:
        #         die_roll_values[2] += 1
        #     elif value == 3:
        #         die_roll_values[3] += 1
        #     elif value == 4:
        #         die_roll_values[4] += 1
        #     elif value == 5:
        #         die_roll_values[5] += 1
        #     elif value == 6:
        #         die_roll_values[6] += 1
        
        # if len(set(die_roll_values.values())) == 1:
        #     # yahtzee
        #     print("\nYou scored a Yahtzee!")
        # elif (1, 2, 3, 4) or (2, 3, 4, 5) or (3, 4, 5, 6) in list(die_roll_values.values()):
        #     # small straight
        #     print("\nYou scored a small straight!")
        # elif (1, 2, 3, 4, 5) or (2, 3, 4, 5, 6) in list(die_roll_values.values()):
        #     # large straight
        #     print("\nYou scored a large straight!")
        # else:
        #     # chance
        #     sum(die_roll_values.values())
        #     print("\nYou scored a chance!")


    def play_round(self, player: 'Player') -> None:
        '''Contains functionality for player to play each round.'''

        roll = self.roll_round(dice_result = {}) 
        print(f"\nYour roll: {', '.join(f"{die_id.title()}: {die_val}" for die_id, die_val in roll.items())}")

        reroll_attempts = 0
        while True :
            if reroll_attempts < 2:
                reroll_input = input(f"\nWould you like to reroll? {reroll_attempts}/2 attempts (yes/no): ").lower()
                if reroll_input in ['yes', 'y']:
                    reroll_attempts += 1
                    roll = self.reroll_round(roll)
                    print(f"\nYour roll: {', '.join(f"{die_id.title()}: {die_val}" for die_id, die_val in roll.items())}")
                elif reroll_input in ['no', 'n']:
                    self.upper_or_lower(player, roll)
                    break
                else:
                    print("Please enter a valid response!")
            else:
                print("\nYou have used all your rerolls!")
                break
                
    