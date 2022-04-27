"""
2. Count by 5s again
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


def count_by_fives_recursive_two(counter, ending_value):
    """
    This is the recursive function to count by 5s, starts at 0 and adds all
    values, in ascending order that are multiples of 5, but less than the
    ending_value.
    :param counter: int, the first call this should start at 0, and it
    increments by five each time
    :param ending_value: any number, represents the stopping criteria
    :return: list of int, the list starts from 0, 5, 10, 15, up to the ending
    value
    """
    if counter > ending_value:
        return []
    five_list = count_by_fives_recursive_two(counter + 5, ending_value)
    return [counter] + five_list


def count_by_fives_recursive_two_test():
    """
    Run many tests of count_by_fives_recursive_two
    :return: None
    """
    for test in range(4975):
        actual = count_by_fives_recursive_two(0, test)
        expected = count_by_fives(test)
        if expected != actual:
            print("Failed on the test")
        else:
            print("Passed the test")
            print("Actual: \n", actual)
            print("Expected: \n", expected)
            return


def main():
    print(count_by_fives_recursive_two(0, 88))
    count_by_fives_recursive_two_test()


if __name__ == "__main__":
    main()
