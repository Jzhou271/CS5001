"""
Coding practice -- Module 6
1. Print multiples of 5
Write a program that reads in a positive integer value from the
keyboard and uses a for loop to print the multiples of 5 that are
less than or equal to the number that was entered.

Enter a positive integer: 42
5
10
15
20
25
30
35
40

"""


def main():
    num = int(input("Enter a positive integer: "))
    for i in range(5, num + 1, 5):
        print(i)


if __name__ == "__main__":
    main()
