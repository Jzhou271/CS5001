"""
CS5001
Lab 7
Jing Zhou
1. Count by 5s
"""


def count_by_fives(ending_value):
    """
    This is the simple loop function for counting by 5s, given by an ending
    value that start counted from 0, and are multiples of 5, but less than
    itself.
    :param ending_value: any number, represents the stopping criteria
    :return: list of int, the list starts from 0, 5, 10, 15, up to the ending
    value
    """
    result = []
    count = 0
    while count <= ending_value:
        result.append(count)
        count += 5
    return result


def count_by_fives_recursive(ending_value):
    """
    This is the recursive function to count by 5s, starts at 0 and adds all
    values, in ascending order that are multiples of 5, but less than the
    ending_value.
    :param ending_value: any number, represents the stopping criteria
    :return: list of int, the list starts from 0, 5, 10, 15, up to the ending
    value
    """
    if ending_value < 0:
        return []
    ending_value = ending_value - (ending_value % 5)
    five_list = count_by_fives_recursive(ending_value - 5)
    return five_list + [ending_value]


def count_by_fives_recursive_test():
    """
    Run many tests of count_by_fives_recursive
    :return: None
    """
    for test in range(4975):
        actual = count_by_fives_recursive(test)
        expected = count_by_fives(test)
        if expected != actual:
            print("Failed on the test")
        else:
            print("Passed the test")
            print("Actual: \n", actual)
            print("Expected: \n", expected)
            return


def main():
    print(count_by_fives(56))
    print(count_by_fives_recursive(55))
    count_by_fives_recursive_test()


if __name__ == "__main__":
    main()
