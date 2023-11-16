def w_sum(vals: list[float]) -> float:
    
    total = 0.0

    i = 0
    
    while i < len(vals):
        total += vals[i]
        i+=1

    return total

def f_sum(vals: list[float]) -> float:

    total = 0.0

    for val in vals:
        total+= val
    
    return total

def f_range_sum(vals: list[float]) -> float:

    total = 0.0
    for i in range(len(vals)):
        total += vals[i]

    return total


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