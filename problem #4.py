############################################
# Author: Keidy lopez
# Filename: problem #4.py
# Description: program that calculates running sum of a given number
############################################

def main():
    # main variables
    num = int(input("Please enter and integer and I will sum all the numbers from 1 up to your integer: "))
    total_sum = 0

    # for loop that determines whether number is positive and prints answer
    if num > 0:
        for i in range(1, num+1):
            total_sum += i
        print("The sum of all the numbers from 1 to " + str(num) + " is " + str(total_sum))
    else:
        print("Please enter a positive number!")


if __name__ == "__main__":
    main()