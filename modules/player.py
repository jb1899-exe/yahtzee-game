class Player:
    def __init__(self, name, score_categories):
        self.name = name
        self.scorecard = {
            category: None 
            for category 
            in score_categories
        }