def main():
    string = input("Enter a sequence of character:\t")
    if string != "":

        char = string[0]
        temp = ""

        # Initializing the counter to be 1
        counter = 1

        # Iterating over the other characters
        for i in range(1, len(string)):
            if string[i] == char:
                counter += 1
            else:
                temp += str(char) + str(counter)
                counter = 1
                char = string[i]
        temp += str(char) + str(counter)
        print(temp)
    else:
        print("You have entered an empty string!")


if __name__ == '__main__':
    main()

