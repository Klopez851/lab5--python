############################################
# Author: Keidy lopez
# Filename: problem #5.py
# Description: program that gives the squared sum of a range of numbers
############################################


def main():
    # main accumulator variable and inputs
    lower_bound = int(input('Please enter the lower bound of a range: '))
    upper_bound = int(input('Please enter the upper bound of a range: '))
    range_total = 0

    # if statements that determone whether lower bound is smaller than upper bound and runs for loop to calculate
    # squared sum and prints total
    if lower_bound > upper_bound:
        print('Please enter a lower bound that is less than the upper bound.')
    elif lower_bound < upper_bound:
        for i in range(lower_bound, upper_bound + 1):
            square = (i**2)
            range_total += square
        print('The squared and summed total is:', range_total)


if __name__ == "__main__":
    main()
