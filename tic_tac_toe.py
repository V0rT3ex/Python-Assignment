def check_row(row):
    """
    This function receives a list, denoted by row,
    and returns whether the all list contains the same
    number or not. if it does, it returns the number, otherwise
    it returns false.
    """

    element = row[0]
    # Looping through the rest of the row
    for i in range(1, 3):
        if i != element:
            return False
    else:
        return element


