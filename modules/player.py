class Player:
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
        # self.lower_scores = {
        #     "three_of_a_kind", 
        #     "four_of_a_kind", 
        #     "full_house",
        #     "small_straight", 
        #     "large_straight", 
        #     "yahtzee", 
        #     "chance"
        # }


    def add_upper_scores(self, new_scores):
        '''Updates player upper scores with new scores.'''
        
        for key in self.upper_scores:
            self.upper_scores[key] += new_scores.get(key, 0)
