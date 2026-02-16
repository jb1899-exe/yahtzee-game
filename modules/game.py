import time
from modules.die import Die
from collections import Counter
from modules.player import Player


class Game:
    '''Controls logic of Yahtzee game.'''

    def __init__(self):
        self.player_names: list[str] = []

    
    def update_player_names(self) -> None:
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
                 

    def get_player_names(self) -> list[str]:
        '''Retrurns names of all active players as entered in-game.'''

        return self.player_names
    
    
    # TODO: add type annotations here
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


    @staticmethod
    def contains_straight(roll_vals: set[int], type: str) -> bool:
        '''Returns True if straight present, depending on large or small argument.'''
        
        # roll_vals = set(roll_vals)
        if type.lower() == 'small':
            return (
                {1, 2, 3, 4}.issubset(roll_vals) or
                {2, 3, 4, 5}.issubset(roll_vals) or
                {3, 4, 5, 6}.issubset(roll_vals)
            )
        elif type.lower() == 'large':
            return (
                {1, 2, 3, 4, 5}.issubset(roll_vals) or
                {2, 3, 4, 5, 6}.issubset(roll_vals)
            )
        else:   
            return False
    
    
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

        die_roll_counts = {
            # key: die face value
            # value: count of face rolls
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0
        }
        for value in roll.values():
            if value in die_roll_counts.keys():
                die_roll_counts[value] += 1

        upper_scores = {
            key: key * value 
            for key, value 
            in die_roll_counts.items()
        }
        # TODO: implement iterable way of doing this
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

        valid_scores = {
            category: score 
            for category, score
            in player_scores.items()
            if not player.used_upper_categories.get(category, False)
        }
        player.add_scores(valid_scores, "upper")
        
        
    def play_lower(self, player: 'Player', roll: dict[str, int]) -> None:
        '''Scores roll with lower scoring rules and updates player scores.'''

        # TODO: make counter function?
        die_roll_counts = {
            # key: die face value
            # value: count of face rolls
            1: 0, 
            2: 0, 
            3: 0, 
            4: 0, 
            5: 0, 
            6: 0
        }
        for value in roll.values():
            if value in die_roll_counts.keys():
                die_roll_counts[value] += 1

        roll_counts = list(die_roll_counts.values())
        roll_values = list(roll.values())
        
        player_scores = {
            "three_of_a_kind": 0, 
            "four_of_a_kind": 0, 
            "full_house": 0,
            "small_straight": 0, 
            "large_straight": 0, 
            "yahtzee": 0, 
            "chance": sum(roll_values)
        }
        if len(set(roll_values)) == 1:
            player_scores['yahtzee'] = 50
        if set(Counter(roll_counts).values()) == [2, 3]:
            player_scores['full_house'] = 25
        if 3 in Counter(roll_counts).values():
            player_scores['three_of_a_kind'] = sum(roll_values)
        if 4 in Counter(roll_counts).values():
            player_scores['four_of_a_kind'] = sum(roll_values)
        if self.contains_straight(set(roll_values), type = 'small'):
            player_scores['small_straight'] = 30
        if self.contains_straight(set(roll_values), type = 'large'):
            player_scores['large_straight'] = 40
            
        valid_scores = {
            category: score 
            for category, score
            in player_scores.items()
            if not player.used_lower_categories.get(category, False)
        }
        player.add_scores(valid_scores, "lower")


    def play_round(self, player: 'Player') -> None:
        '''Contains functionality for player to play each round.'''

        roll = self.roll_round(dice_result = {}) 
        print(f"\nYour roll: {', '.join(f"{die_id.title()}: {die_val}" for die_id, die_val in roll.items())}")

        reroll_attempts = 0
        while True:
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
                self.upper_or_lower(player, roll)
                break    