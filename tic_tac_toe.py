import sys


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
        if row[i] != element:
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


def check_diagonals(matrix):
    """
     This function receives the matrix and returns whether
     one of the diagonals contains the same number or not.
     If one does, it returns the number, otherwise it returns false.
    """

    # Initializing the rows of the matrix
    row1, row2, row3 = matrix[0], matrix[1], matrix[2]

    if row1[0] == row2[1] and row2[1] == row3[2]:
        return row1[0]
    elif row1[2] == row2[1] and row2[1] == row3[0]:
        return row1[2]
    return False


def board_input():
    """
    This function asks the user to fill in
    the board of the game and returns a matrix which represents
    the board.
    """

    matrix = []

    # Creating each row in the board
    for i in range(1, 4):
        print("Insert the numbers in row {}:".format(i))
        temp = input()
        temp = temp.split(',')
        temp = [int(element) for element in temp]
        matrix.append(temp)

    return matrix


def main():
    game = board_input()
    for row in game:
        temp = check_row(row)
        if temp:
            print("The winner is player {}".format(temp))
            sys.exit()

    temp = check_cols(game)
    if temp:
        print("The winner is player {}".format(temp))
        sys.exit()

    temp = check_diagonals(game)
    if temp:
        print("The winner is player {}".format(temp))
        sys.exit()

    print("Draw!")


if __name__ == '__main__':
    main()

