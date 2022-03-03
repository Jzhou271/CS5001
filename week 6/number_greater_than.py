"""
CS5001
Lab 5
Jing Zhou
Question 2 Number greater than?
"""


def number_greater_than(float_list_1, float_list_2):
    '''
    This function returns a number by counting how many numbers in
    float_list_1 is greater than the corresponding number in float_list_2.
    :return: integer, the number of float numbers
    '''
    res = 0
    for i in range(len(float_list_1)):
        if float_list_1[i] > float_list_2[i]:
            res += 1
    return res


def number_greater_than_test():
    '''
    This is the fixed test to check if the expected output is the same as
    actual output
    '''
    float_list_1 = [12.3, 24.64, 34.3, 55.55, 63.22]
    float_list_2 = [10.4, 22.78, 36.9, 55.99, 56.8]
    expected = 3
    actual = number_greater_than(float_list_1, float_list_2)
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")

    float_list_1 = [-25, 0, 20, 59, 101]
    float_list_2 = [-67, 4, 10, 23, 38]
    expected = 4
    actual = number_greater_than(float_list_1, float_list_2)
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")


def main():
    number_greater_than_test()


if __name__ == "__main__":
    main()
