'''
program should have the user input a single integer value, and then should print out if that is an even or odd number.
'''


def main():
    num_aa = int(input("Input number: "))
    if num_aa % 2 == 0:
        print(num_aa, "is even")
    else:
        print(num_aa, "is odd")


if __name__ == "__main__":
    main()
