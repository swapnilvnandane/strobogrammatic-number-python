from com.app import StrobogrammaticNumber

"""
Main function to run the program
"""


def main():
    # Read input from the user
    user_input = input("Enter a value: ")

    if StrobogrammaticNumber.check(user_input):
        print("The number is strobogrammatic.")
    else:
        print("The number is not strobogrammatic.")


"""
Run main function
"""
if __name__ == "__main__":
    main()

"""
Main class to run the program
"""


class Main:
    pass
