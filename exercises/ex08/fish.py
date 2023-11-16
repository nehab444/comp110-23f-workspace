"""File to define Fish class."""


class Fish:
    """This class shows Fish behavior and makes a Fish object."""
    
    age: int

    def __init__(self, inp1_age=0):
        """This is a starter fish function."""
        self.age = inp1_age
    
    def one_day(self):
        """This shows the lifespan of a fish."""
        self.age += 1