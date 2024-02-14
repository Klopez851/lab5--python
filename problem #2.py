############################################
# Author: Keidy lopez
# Filename: problem #2.py
# Description: prints out odd integers between a two numbers
############################################

def main():
    # announces action
    print("The odd integers between 1 and 99 are:\n")

    # for loop that prints odd integers
    for i in range(1,100,2):
        print(i, end=", ")


if __name__ == "__main__":
    main()