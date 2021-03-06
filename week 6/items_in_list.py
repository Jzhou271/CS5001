"""
Question 4 List containing values from another list
"""
import random


def items_in_list(integer_list_1, integer_list_2):
    """
    This function takes two lists and returns a third list. The third list
    contains only items that are in first_list but are also present in
    second_list
    :return: list, the values in both lists without repeating
    """
    res = []
    for i in integer_list_1:
        for j in integer_list_2:
            if i == j and i not in res:
                res.append(i)
    return res


def items_in_list_test():
    """
    This is the fixed test to check if the expected output is the same as
    actual output
    """
    integer_list_1 = [1, 2, 3, 4, 5, 6]
    integer_list_2 = [1, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 3, 4, 5, 6]
    actual = items_in_list(integer_list_1, integer_list_2)
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")

    integer_list_1 = [5, 7, 11, 34, 100]
    integer_list_2 = [4, 7, 45, 55, 100, 7, 7, 35, 64]
    expected = [7, 100]
    actual = items_in_list(integer_list_1, integer_list_2)
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")


def items_in_list_random():
    """
    This is random test to check if the expected output is the same as
    actual output
    """
    for test in range(5000):
        length_of_first = random.randint(1, 7)
        additional_length_of_second = random.randint(1, 5)
        integer_list_1 = []
        for index in range(length_of_first):
            integer_list_1.append(random.randint(0, 500))
        integer_list_2 = integer_list_1
        for index in range(additional_length_of_second):
            integer_list_2.append(random.randint(0, 500))
        expected = integer_list_1
        actual = items_in_list(integer_list_1, integer_list_2)
        if expected.sort() != actual.sort():
            print("FAILED the test")
        else:
            print("PASSED the test")
            break


def main():
    items_in_list_test()
    items_in_list_random()


if __name__ == "__main__":
    main()

