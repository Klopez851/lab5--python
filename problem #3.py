############################################
# Author: Keidy lopez
# Filename: problem #3.py
# Description: program that gives factorial of an entered number
############################################

def main():
    # main variables
    num = int(input("What number would you like to factor: "))
    factorial = 1

    # for loop that calculates and prints factorial if number is not negative
    if num > 0:
        for i in range(num, 1, -1):
            if i != 0:
                factorial *= i
        print("factorial of " + str(num) + " is " + str(factorial))
    elif num < 0:
        print("please enter a positive integer!")


if __name__ == "__main__":
    main()
