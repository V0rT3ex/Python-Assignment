import sys


# The secret code is set to be 12345 in default
secret_code = "12345"


def check_password():
    """
    This function checks whether a password inserted
    by a user is valid or not.
    """
    password = input("Please enter your account's password:\t")
    while True:
        if password == secret_code:
            break
        print("You have inserted an invalid password!")
        # Reinputing the password
        password = input("Please enter your account's password again:\t")
    print("You have successfully entered to your account!")


def main():
    """
    Main function of the ATM's operation.
    """

    # Setting the amount of money var to be 1000 in default
    amount_of_money = 1000

    # Calling check_password function
    check_password()

    print("Enter 1 - to see your account's status, 2 - to withdraw money, 3 - to change your password and 4 - to exit")
    option = int(input("choice:\t"))

    # Ensuring the input is valid
    while True:
        if option > 1 or option < 4:
            break
        option = int(input("Enter a valid choice!\t"))

    # Looping until the user chooses 4
    while True:
        if option == 4:
            break
        elif option == 1:
            print("The amount of money in your bank is :\t{}".format(amount_of_money))
        elif option == 2:
            withdrawal = int(input("Enter the amount of money to withdraw: 20, 50 or any other amount:\t"))
            # If the user entered a negative value, he will be stuck in a loop until he inserts a valid value.
            while True:
                if withdrawal > 0:
                    break
                withdrawal = int(input("Please enter a positive value!"))
            amount_of_money -= withdrawal
        else:
            # Allowing a change in the global variable - secret_code
            global secret_code
            secret_code = input("Enter your new secret code:\t")
        check_password()
        print(
            "Enter 1 - to see your account's status, 2 - to withdraw money, 3 - to change your password and 4 - to exit")
        option = int(input("choice:\t"))
    sys.exit()


if __name__ == '__main__':
    main()
