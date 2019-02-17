def compute(x, y):
    if (isinstance(x, int) and isinstance(y, int)) and (0 <= x and y <= 100):
        return x+y
    return 'inputs must be integers in the range 1-100'
