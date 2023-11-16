"""Combining two lists into a dictionary."""
__author__: str = "730645945"


def zip(list1: list[str], list2: list[int]) -> dict[str, int]:
    """The function name is zip and The function should produce a dictionary where the keys are the items of the first list and the values are the corresponding items at the same index of the second list.
    
    Args:
    list1: list[str] is our first list
    list2: list[str] is our second list
    Returns:
    The function should return a dict[str,int] where the keys are the items of the first list and the values are the corresponding items at the same index of the second list.
    
    """
    if len(list1) != len(list2):
        return {}
    
    zipped_dict = {}
    for i in range(len(list1)):
        zipped_dict[list1[i]] = list2[i]

    return zipped_dict