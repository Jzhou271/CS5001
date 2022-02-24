'''
Write a function called float_is_equal that takes three parameters. The first
two parameters are the numbers to compare. The third parameter is a value to 
use as a threshold. 
use the fabs function in the math module if you need. It takes a parameter and
returns the absolute value of the parameter.
'''
import math


def float_is_equal(number_1, number_2, threshold):
    '''
    This compares number_1 and number_2 to see if they are within threshold of
    each other
    :param number_1: a float or an integer to compare to number_2
    :param number_2: a float or an integer to compare to number_1
    :param threshold: a float, if number_1 and number_2 have a difference that
    less than threshold, we consider them equal
    :return: boolean, true if the numbers are approximately equaled
    '''
    return math.fabs(number_1 - number_2) < threshold


def test_float_is_equal(number_1, number_2, threshold, expected):
    actual = float_is_equal(number_1, number_2, threshold)
    if actual == expected:
        print("PASS", "on input:", number_1, number_2, threshold)
        print("EXPECTED:", expected)
        print("ACTUAL:", actual)
    else:
        print("FAIL", "on input:", number_1, number_2, threshold)
        print("EXPECTED:", expected)
        print("ACTUAL:", actual)


def main():
    test_float_is_equal(10.57, 3.57159, 0.001, False)
    test_float_is_equal(443.433, 443.674, 0.001, False)
    test_float_is_equal(88.5673002, 88.77456384792, 0.1, False)
    test_float_is_equal(11.11111, 11.111, 0.1, True)


if __name__ == "__main__":
    main()
