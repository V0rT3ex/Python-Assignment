def seif_alef():
    """
    This function inputs numbers from the user
    until he inserts stop.
    It prints the sum of the numbers he has inserted.
    """

    # Initializing the sum.
    sum = 0

    # Looping until the user inserts stop
    while True:
        number = input("Enter a number. Enter stop to stop.\t")
        if number == 'stop':
            break
        sum += int(number)
    print("The sum of the numbers you have inserted:\t{}".format(sum))


def seif_bet():
    """
    This function inputs a list of number
    from the user and prints the sum of them.
    """

    # Initializing the sum.
    sum = 0
    numbers = input("Enter a list of numbers:\t")
    numbers = numbers.split(',')

    # Iterating over each number and summing.
    for number in numbers:
        sum += int(number)
    print("The sum of the numbers you have inserted:\t{}".format(sum))

