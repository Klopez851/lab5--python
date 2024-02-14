############################################
# Author: Keidy lopez
# Filename: problem #9.py
# Description: program that generates a pattern
############################################

def main():

    # for loop that generates pattern
    for i in range(1,3):
        for j in range(1,11):
            print('*', end='')
        print()
        for l in range(1, 11):
            print('=', end='')
        print()


if __name__ == "__main__":
    main()