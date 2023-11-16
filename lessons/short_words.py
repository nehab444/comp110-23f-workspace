"""A function that gets rid of long elements in list."""

__author__: str = "730645945"


def short_words(list1: list[str]) -> list[str]:
    """Filter out the shorter words."""
    new_list: list[str] = []

    for x in list1:
        if len(x) < 5:
            new_list.append(x)
        else:
            print(f"{x} is too long!")
    return new_list
