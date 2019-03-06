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


def check_cols(matrix):
    """
    This function receives the matrix and returns whether
    there is a sequence of the same number in a col of the matrix.
    If it does, it returns the number, otherwise it returns false.
    """

    # Initializing the rows of the matrix
    row1, row2, row3 = matrix[0], matrix[1], matrix[2]

    # Looping through each row
    for i in range(3):
        if row1[i] == row2[i] and row2[i] == row3[i]:
            return row1[i]
    return False
