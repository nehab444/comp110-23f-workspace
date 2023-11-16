"""Calling river methods and instantiating them."""

from exercises.ex08.river import River

my_river: River = River(10, 2)
print(my_river)

my_river.view_river()

my_river.one_river_week()

my_river.repopulate_bears()