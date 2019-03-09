import time

cache_dict = {}


def print_items(*args):
    temp_list = [str(item) for item in args]
    temp_list = str(temp_list)
    temp_list = temp_list[3:len(temp_list) - 3]
    return ''.join(temp_list)


def cache_decorator(*args):
    """
    This function receives a dynamic number of parameters - depending
    on the user's decision and prints the parameters passed, using the
    print_items function. This function uses a dictionary which operates as a
    cache for the calculations. If a "calculation" does not appear in the dictionary,
    it will calculate the function and insert it into the dictionary. Otherwise, it
    returns the value of the key that does appear in the dictionary.
    Note that this function will also use the time.sleep method to create an illusion
    as if the function were to be a massive one.
    """

    args_str = str(args)
    if args_str in cache_dict:
        print(cache_dict[args_str])
    else:
        print("Calculating your function...")

        # Arbitrary time to sleep
        time.sleep(5)

        cache_dict[args_str] = print_items(args)
        print(cache_dict[args_str])


