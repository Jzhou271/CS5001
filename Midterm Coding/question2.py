"""
CS5001
Jing Zhou
Midterm Coding Portion
2. Correct this code 
To find the bug in this code and correct it, so that the functionality
matches the description
"""


def find_median(input_list):
    '''
    find_median takes a list of numbers as input and finds the median value
    in the list. The median value is defined as the value for which half the
    items are larger and half the items are smaller. For a list of length 5,
    this means 2 values are larger and 2 values are larger. So for an odd
    length list there are an equal number of bigger items, and equal number
    of smaller items. For a list of length 6, there are 2 values larger, and
    two values smaller. But this leaves two middle values. In this case we
    take the average of the two: (middle1 + middle2) / 2
    So for an even length list, there are equal number smaller and larger, but
    then we always have two values left, and must take their average (mean).
    :param input_list: A list of numbers
    :return: The median value of the list
    '''
    median = 0
    sorted_list = sorted(input_list)
    for i in range(len(sorted_list)):
        if len(input_list) % 2 != 0:
            median = int((len(sorted_list) + 1) / 2 - 1)
            return input_list[median]
        else:
            middle1 = int(len(input_list) / 2 - 1)
            middle2 = int(len(input_list) / 2)
            return (sorted_list[middle1] + sorted_list[middle2]) / 2


def find_median_fix_test():
    """
    This is the fixed method to test if the expected output is the same as
    actual output
    :return: None
    """
    my_list = list(range(0, 6))
    expected = 2.5
    actual = find_median(my_list)
    if actual != expected:
        print("FAILED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)
    else:
        print("PASSED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)

    my_list = list(range(0, 5))
    expected = 2
    actual = find_median(my_list)
    if actual != expected:
        print("FAILED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)
    else:
        print("PASSED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)


def main():
    print(find_median([2, 4, 6, 7, 6, 9, 10]))
    print(find_median([-2, 7, 6, 4, 8, 3, 6]))
    find_median_fix_test()


if __name__ == "__main__":
    main()
