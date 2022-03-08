"""
CS5001
Jing Zhou
Midterm Coding Portion
List of Multiples of 3
write code that takes an integer as input, and returns a list containing all
multiples of 3 in ascending order. test code on several hand created examples
for expected results. 
"""


def multiples_of_three(integer):
    """
    The function takes an integer as input, and returns a list containing
    all multiples of 3 that are less than or equal to the integer that was
    entered
    :param integer: an integer
    :return: a list, starts from 0 and the multiples of 3 that are less than
    or equal to the integer
    """
    res = []
    for i in range(0, integer + 1, 3):
        res.append(i)
    return res


def multiples_of_three_fixed_test():
    """
    This is the fixed method to test if the expected output is the same as
    actual output
    :return: None
    """
    actual = multiples_of_three(21)
    expected = [0, 3, 6, 9, 12, 15, 18, 21]
    if actual != expected:
        print("TEST FAILED")
        print("actual output is", actual)
        print("expected output is", expected)
    else:
        print("TEST PASSED")
        print("actual output is", actual)
        print("expected output is", expected)

    actual = multiples_of_three(17)
    expected = [0, 3, 6, 9, 12, 15]
    if actual != expected:
        print("TEST FAILED")
        print("actual output is", actual)
        print("expected output is", expected)
    else:
        print("TEST PASSED")
        print("actual output is", actual)
        print("expected output is", expected)


def main():
    multiples_of_three_fixed_test()


if __name__ == "__main__":
    main()
