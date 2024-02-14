############################################
# Author: Keidy lopez
# Filename: problem #8.py
# Description: program that finds the nth number of the fibonacci sequence
############################################

def main():
    # main variables
    n = int(input('please enter the sequence position for which you would like to find the corresponding fibonacci number: '))
    num1 = 1
    num2 = 0
    num3 = 0

    # for loop that calculates nth number
    for i in range(1, n+1):
        num3 = num1 + num2
        num1 = num2
        num2 = num3

    # prints out nth number
    print(num3)

if __name__ == "__main__":
    main()