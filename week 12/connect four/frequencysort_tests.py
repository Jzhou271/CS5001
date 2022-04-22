import frequencysort
import unittest


def test_value_pair():
    """
    This is the test function to test value_pair() in file frequencysort.py.
    """
    abc = [0, -1]
    expected = [0, -1]
    actual = frequencysort.value_pair()
    if actual != expected:
        print("FAILED ON THE TEST")
    else:
        print("PASSED ON THE TEST")


def test_sort():
    """
    This is the test function to test sort() in file frequencysort.py.
    it takes a list of string of numbers as input test parameter, defined as
    the variable "mylist", get output of a new list that more frequency goes
    first, followed by the one that appeared first in the original list should
    come first.
    """
    list_of_number = [3, 3, 1, 1, 1, 8, 3, 6, 8, 7, 8]
    expected = [3, 3, 3, 1, 1, 1, 8, 8, 8, 6, 7]
    actual = frequencysort.sort(list_of_number)
    if actual != expected:
        print("FAILED ON THE TEST")
    else:
        print("PASSED ON THE TEST")

    list_of_number = [-1, -4, -2, -1, -5, 0, 0, -1]
    expected = [-1, -1, -1, 0, 0, -4, -2, -5]
    actual = frequencysort.sort(list_of_number)
    if actual != expected:
        print("FAILED ON THE TEST")
    else:
        print("PASSED ON THE TEST")

    list_of_number = [20, 20, 20, 30, 100, 30, 1, 0, 2, 2, 2]
    expected = [20, 20, 20, 2, 2, 2, 30, 30, 100, 1, 0]
    actual = frequencysort.sort(list_of_number)
    if actual != expected:
        print("FAILED ON THE TEST")
    else:
        print("PASSED ON THE TEST")


def main():
    # unittest.main()
    test_value_pair()
    test_sort()


if __name__ == '__main__':
    main()
