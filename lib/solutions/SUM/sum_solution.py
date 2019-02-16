def compute(x, y):
    if isinstance(x, int) and isinstance(y, int):
        return x+y
    return '{} and {} must be integers in the range 1-100'.format(x, y)




