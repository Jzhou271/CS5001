
"""
Coding practice -- Module 5
Convert to Numbers
Write a function called to_numbers that receives a list of string values
each of which represents a number and returns a list of floats.
"""


def to_numbers(string):
    index = 0
    while index < len(string):
        # convert string for float number
        string[index] = float(string[index])
        index += 1
    return string


def main():
    print(to_numbers([22, 564, 67]))


if __name__ == "__main__":
    main()
