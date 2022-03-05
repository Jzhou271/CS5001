"""
Coding practice -- Module 6
7. Filter evens
Write a function called filter_evens that receives a list of integer values
and returns a new list that contains only the even elements of the argument.
"""


def filter_evens(list_of_integer):
    res = []
    for i in range(len(list_of_integer)):
        if list_of_integer[i] % 2 == 0:
            res.append(list_of_integer[i])
    return res


def main():
    print(filter_evens([12, 35, 54, 67, 100]))


if __name__ == "__main__":
    main()
