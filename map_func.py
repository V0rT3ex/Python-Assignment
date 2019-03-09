def map_function(l, function):
    """
    This function receives a list - denoted by l,
    and a function as parameters and returns the list after
    each item of it has been modified by the function parameter.
    """

    l = [function(item) for item in l]
    return l


def func1(val):
    return val ** 2

def func2(val):
    return val + len('abc')