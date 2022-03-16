"""
CS5001
Lab 7
Jing Zhou
3. Filter list
"""
import random


def filter_list(list_of_number, threshold):
    """
    The filter_list takes a list of number as first parameter, and set a value
    as the second parameter, to compare all numbers in the list which are
    larger than the threshold, then return the new list
    :param: list, list of numbers, include integer and float
    :param: integer/float, any number set as threshold, to compared with
    numbers in the list
    :return: list, numbers are greater than threshold
    """
    new_list = filter(lambda res: res > threshold, list_of_number)
    res = list(new_list)
    return res


def filter_list_fixed_test():
    """
    Fixed method to test if the expected output is the same as actual output
    :return: None
    """
    test_list = [3, 4, 6, 7, 8, 20, 30]
    test_threshold = 5
    actual = filter_list(test_list, test_threshold)
    expected = [6, 7, 8, 20, 30]
    if actual != expected:
        print("Failed on the test")
    else:
        print("Passed on the test")
        print("Actual output is", actual)
        print("Expected output is", expected)

    test_list = [-6, -2, 3, 0, 15, -26, 63]
    test_threshold = 0
    actual = filter_list(test_list, test_threshold)
    expected = [3, 15, 63]
    if actual != expected:
        print("Failed on the test")
    else:
        print("Passed on the test")
        print("Actual output is", actual)
        print("Expected output is", expected)


def filter_list_random_test():
    """
    Random test of filter_list to check if the expected output is the same as
    actual output
    :return: None
    """
    test_list = []
    for i in range(10):
        test_list.append((random.random() - 0.5) * 200)
    test_threshold = (random.random() - 0.5) * 200
    expected = []
    for i in test_list:
        if i > test_threshold:
            expected.append(i)
        actual = filter_list(test_list, test_threshold)
    if actual != expected:
        print("Failed on the test")
    else:
        print("Passed on the test")
        print("Actual output is", actual)
        print("Expected output is", expected)


def main():
    filter_list_fixed_test()
    filter_list_random_test()


if __name__ == "__main__":
    main()
