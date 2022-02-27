
"""
CS5001
Jing Zhou
Coding practice -- Module 5
Read values
Write a function called read_values that returns a list of positive
integer values that are read from the keyboard one at a time. The values
should appear in the list in the order that they were entered.
Any non-positive integer value should stop adding elements to the list
"""


def read_values():
    # set up a empty list
    output = []
    while True:
        integer = int(input("Enter a number: "))
        if integer > 0:
            output.append(integer)
        else: # if integer < 0, quit the loop
            break
        print(output)
    return


def main():
    print(read_values())


if __name__ == "__main__":
    main()
