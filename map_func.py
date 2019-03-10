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


if __name__ == '__main__':
    l = [1, 3, 8]
    print(l)
    l = map_function(l, func1)
    print(l)
    l = map_function(l, func2)
    print(l)


