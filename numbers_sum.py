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


