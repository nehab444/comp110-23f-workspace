"""File to define River class."""

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

__author__: str = "730645945"

day = int
bears = list[Bear]
fish = list[Fish]


class River:
    """This class describes the whole River ecosystem."""
    
    def __init__(self, num_fish: int, num_bears: int): 
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """This checks the ages of the fish in the ecosystem."""
        new_fish = []
        for fish in self.fish:
            if fish.age <= 3:
                new_fish.append(fish)
        self.fish = new_fish

        new_bears = []
        for bear in self.bears:
            if bear.age <= 5:
                new_bears.append(bear)
        self.bears = new_bears

    def bears_eating(self):
        """For each Bear, if there are at least 5 Fish, the Bear will eat 3 Fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)  # Remove 3 Fish
                bear.eat(3)  # Bear eats 3 Fish
    
    def check_hunger(self):
        """Remove bears from the river if their hunger_score is less than 0."""
        new_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                new_bears.append(bear)
        self.bears = new_bears
        
    def repopulate_fish(self):
        """Each pair of fish will produce 4 offspring."""
        new_fish = len(self.fish) // 2
        for _ in range(new_fish * 4):
            self.fish.append(Fish())  # Append new Fish instances, not the Fish class itself

    def repopulate_bears(self):
        """Each pair of bears will produce 1 offspring."""
        new_bears = len(self.bears) // 2
        for _ in range(new_bears):
            self.bears.append(Bear())  # Append new Bear instances, not the count of new bears

    def remove_fish(self, amount: int):
        """Remove amount many Fish from the river."""
        for number in range(amount):
            if self.fish:
                self.fish.pop(0)
            else:
                print("Not enough fish in the river")
                break

    def view_river(self):
        """See how the river ecosystem is doing."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()
            
    def one_river_week(self):
        """Shows the river in a week."""
        for blank in range(7):
            self.one_river_day()