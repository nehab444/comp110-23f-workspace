def value_exists(value1: dict[str, int], val: int) -> bool:
    """Return true if value exists"""
    for elem in value1:
        if value1[elem] == val:
            return True
    return False 