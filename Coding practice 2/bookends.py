"""
CS5001
Jing Zhou
Coding practice -- Module 2
Numeric Bookends
Write a program that reads a 4-digit number from the keyboard and prints
the first and last digits of the number
"""


def main():
    book_num = str(input("Enter number: "))
    abc_1 = book_num[0]
    abc_2 = book_num[3]
    print("The first number is", abc_1)
    print("The last number is", abc_2)


if __name__ == "__main__":
    main()
