"""
CS5001
Jing Zhou
Coding practice -- Module 5
Tuple to list
Write a function called convert_tuple that takes a tuple as a parameter
and returns a list that contains all of the same elements in the same order.
"""


def convert_tuple(string):
    # set a tuple empty list
    output = []
    i = 0
    while i < len(string):
        # add [1], [2], [3].. to the list
        output.append(string[i])
        i += 1
    return output


def main():
    print(convert_tuple([1, 2, 3, 4, 5, 6, 7]))


if __name__ == "__main__":
    main()
