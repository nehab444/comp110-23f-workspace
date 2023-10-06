"""EX04- Practice in implementing algorithms to gain knowledge on computational thinking!"""

__author__ = "730645945"

def all(input: list[int], chosen_int) -> int:

    if len(list) == 0:
        return False
    
    expected_length = len(list)

    while len(list) > 0:

        num = list.pop()

        if num != chosen_int:
            return False
        

    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    maximum = list.pop()
    
    # Iterate through the list
    while len(list) > 0:
        # Pop the last element from the list
        num = list.pop()
        
        # Update the maximum value if a larger number is found
        if num > maximum:
            maximum = num
    
    return maximum

def is_equal(input: list[int], input1: list[int]) -> int:

    if len(input) != len(input1):
        return False

    while len(input) > 0:

        num1 = input.pop() 
        num2 = input1.pop()

        if num1 != num2:
            return False
        
    return True
    