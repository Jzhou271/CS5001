
"""
Coding practice -- Module 5
Square each
Write a function called square_each that receives a list as a parameter
and returns the same list that has been modified so that all the elements
are squared.
"""


def square_each(string):
    index = 0
    while index < len(string):
        # set the formual as a = a^2
        string[index] = string[index] * string[index]
        index += 1
    return string


def main():
    print(square_each([11, 20]))


if __name__ == "__main__":
    main()
