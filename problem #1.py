############################################
# Author: Keidy lopez
# Filename: problem#1.py
# Description: program that counts down starting at 10
############################################

def main():
    # announcing countdown
    print("countdown\n")

    # for loop for countdown
    for i in range(10, 0, -1):
        print(i, end="\n")
        if i == 1:
            break

    # prints blastoff
    print("\nBlastoff!!!!")


if __name__=="__main__":
    main()
