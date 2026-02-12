class Player:
    '''Controls player scoring logic.'''

    def __init__(self, name):
        self.name = name
        self.upper_scores = {
            "ones": 0, 
            "twos": 0, 
            "threes": 0, 
            "fours": 0, 
            "fives": 0, 
            "sixes": 0
        }
        self.lower_scores = {
            "three_of_a_kind": 0, 
            "four_of_a_kind": 0, 
            "full_house": 0,
            "small_straight": 0, 
            "large_straight": 0, 
            "yahtzee": 0, 
            "chance": 0
        }
        self.used_upper_categories = {
            "ones": False, 
            "twos": False, 
            "threes": False, 
            "fours": False, 
            "fives": False, 
            "sixes": False
        }
        self.used_lower_categories = {
            "three_of_a_kind": False, 
            "four_of_a_kind": False, 
            "full_house": False,
            "small_straight": False, 
            "large_straight": False, 
            "yahtzee": False, 
            "chance": False
        }


    def get_availible_upper_categories(self):
        '''Returns scoring categories that have no yet been used in-game by player.'''
        
        # TODO: Make this work for upper/lower
        availible_categories = {key: value for key, value in self.used_upper_categories.items() if value is False}
        return availible_categories
    

    def get_scored_categories(self, new_scores):
        '''Returns categories scored by player in a round.'''

        scored_categories = {key: value for key, value in new_scores.items() if value != 0}
        return scored_categories


    def add_upper_scores(self, new_scores):
        '''Updates player upper scores with new scores.'''

        unused_categories = set(self.get_availible_upper_categories().keys())
        scored_categories = set(self.get_scored_categories(new_scores).keys())
        availible_categories = list()
        for category in unused_categories:
            if category in scored_categories.intersection(unused_categories):
                availible_categories.append(category)

        print("\nYou may score:")
        for key, value in new_scores.items():
            if value != 0 and key in availible_categories:
                print(f"{key.title()}: {value}")
       
        while True:
            upper_category_input = (input(f"\nPlease select a score category! ({', '.join(f"{item.title()}" for item in availible_categories)}): ").lower())
                        
            if upper_category_input in availible_categories:
                print(f"\nYou selected {upper_category_input.title()}")
                self.upper_scores[upper_category_input] = new_scores[upper_category_input]
                print(f"\nYou scored {self.upper_scores[upper_category_input]} points!")
                self.used_upper_categories[upper_category_input] = True
                break
            else:
                print("\nPlease enter a valid response!")