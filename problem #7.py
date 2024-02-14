############################################
# Author: Keidy lopez
# Filename: problem #7.py
# Description: program that rolls dice 5 times, gives total and average roll; if dice is double 1 stops and calculates
# the dice total rolls up until then.
############################################
import random

def main():
    # input to start the rolls
    input('Let\'s roll some dice!\nPress enter to roll 5 times...')
    print()

    # for loop that rolls dice and gives total of rolls and average of roll
    die_total = 0
    for i in range(1, 6):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        die_total += (die2 + die1)
        if die1 == 1 and die2 == 1:  # if roll is snake eyes this will execute and break loop
            print('roll #'+str(i)+ ': ' + str(die1) + ', ' + str(die2) + ' snake eye!')
            average_roll = die_total / 5
            print('the total: ' + str(die_total), 'the average roll was: ' + str(average_roll))
            break
        elif die1 != 1 or die2 != 1:
            print('roll #' + str(i) + ': ' + str(die1) + ', ' + str(die2))
        if i == 5:
            average_roll = die_total/5
            print('the total: ' + str(die_total), 'the average roll was: ' + str(average_roll))


if __name__ == "__main__":
    main()