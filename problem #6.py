############################################
# Author: Keidy lopez
# Filename: problem #6.py
# Description: program that prints out 10 dice rolls and announces if the roll is a double
############################################
import random

def main():
    # input to start the rolls
    input('Let\'s roll some dice!\nPress enter to roll 10 times...')
    print()

    # for loop that prints out 10 rolls and determines whether they are doubles
    for i in range(1,11):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 == die2:
            print('roll #' + str(i) + ': ' + str(die1) + ', ' + str(die2), 'Doubles!')
        else:
            print('roll #' + str(i) + ': ' +str(die1) + ', ' + str(die2))


if __name__ == "__main__":
    main()
