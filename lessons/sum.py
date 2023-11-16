"""Summing the elements of a list using different loops."""

__author__: str = "730645945"


def w_sum(vals: list[float]) -> float:
    """Calculates the sum of all element using a while loop!

    Args:
    vals: list[float]: List of float values.

    Returns:
    float: The sum of all the elements in the list.
    """
    total = 0.0  

    index = 0  

    while index < len(vals):
        total += vals[index]
        index += 1
    
    return total


def f_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements using a for in loop.

    Args:
    vals: list[float]: List of float values.

    Returns:
    float: The sum of all the elements in the list.
    """
    # Initialize the sum to 0.0
    total = 0.0
    
    # Use a for...in loop to iterate through the list directly
    for val in vals:
        total += val

    return total


def f_range_sum(vals: list[float]) -> float:
    """Calculates the sum of all elements using a for in range loop.

    Args:
    vals: list[float]: List of float values.

    Returns:
    float: The sum of all the elements in the list.
    """
    # Initialize the sum to 0.0
    total = 0.0
    
    # Use a for...in range loop to iterate through the list
    for i in range(len(vals)):
        total += vals[i]

    return total

# Test the function with the examples


result = f_range_sum([1.1, 0.9, 1.0])
print(result)  # Should print 3.0


result = f_range_sum([])
print(result)  # Should print 0.0


# Test the function with examples
result = f_sum([1.1, 0.9, 1.0])
print(result)  # Should print 3.0


result = f_sum([])
print(result)  # Should print 0.0


result = w_sum([1.1, 0.9, 1.0])
print(result)  # Should print 3.0


result = w_sum([])
print(result)