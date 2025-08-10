# def add(a, b):
#     """Return the sum of a and b."""
#     return a + b

def add(a, b):
    """Return the sum of a and b."""
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be int or float")
    return a + b

def divide(a, b):
    """Return a divided by b."""
    return a / b

