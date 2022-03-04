"""
CS5001
Jing Zhou
Coding practice -- Module 2
Clamping
Write a program that reads in a number from the keyboard. Your program
should ensure that the value entered is between 1 and 100 by clamping it
and then print it to the screen. Clamping a number means that any value
less than the lowest value is set to the lowest value and that any value
larger than the largest value is set to the largest value.
"""


def main():
    num = int(input("Enter value: "))
    if 1 <= num <= 100:
        print(num)
    elif num > 100:
        print("Too big, clamping required")
        print("Value is 100")
    elif num < 1:
        print("Too small, clamping required")
        print("Value is 1")


if __name__ == "__main__":
    main()
