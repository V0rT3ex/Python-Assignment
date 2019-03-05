import sys


# The secret code is set to be 12345 in default
secret_code = "12345"


def check_password(password):
    """
    This function checks whether a password inserted
    by a user is valid or not.
    """

    while True:
        if password == secret_code:
            break
        print("You have inserted an invalid password!")
        # Reinputing the password
        password = input("Please enter your account's password again:\t")
    print("You have successfully entered to your account!")

