# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if (isinstance(x, int) and isinstance(y, int)) and x,y in range(101):
        return x+y
    return '{} and {} must be integers in the range 1-100'.format(x, y)
    raise NotImplementedError()


