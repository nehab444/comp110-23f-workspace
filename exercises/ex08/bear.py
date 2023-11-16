"""File to define Bear class."""


class Bear:
    """This is the bear class."""
    
    age: int
    hunger_score: int

    def __init__(self, inp_age=0, inp_hunger_score=0):
        """This is a starter function."""
        self.age = inp_age
        self.hunger_score = inp_hunger_score
    
    def one_day(self):
        """This function updates the day-to-day bear population."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """This function shows how much fish the bear eats."""
        self.hunger_score += num_fish