import sys


def main():
    """
    This function returns whether an ID inputted
    is valid or not.
    """

    Id = input("Enter the id you would like to check:\t")
    sum = 0

    # Iterating over each element of the Id except for the last one
    for i in range(len(Id) - 1):
        if i % 2 == 0:
            sum += int(Id[i])
        else:
            sum += int(Id[i]) * 2 // 10 + int(Id[i]) * 2 % 10

    tens = 10
    # Looping until the tens is greater or equal to sum
    while True:
        if tens >= sum:
            break
        tens += 10

    if tens - sum == int(Id[len(Id) - 1]):
        print("The ID you have entered is valid")
        sys.exit()
    print("The ID you have entered is not valid")


if __name__ == '__main__':
    main()

