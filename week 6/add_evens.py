"""
CS5001
Lab 5
Jing Zhou
Question 3 Adding Evens
"""


def add_evens(list_num):
    '''
    This is the function takes a list of integers, and add all even values in
    the list and return the result
    :return: integer, adding by all even numbers in the list
    '''
    res = 0
    for i in range(len(list_num)):
        if list_num[i] % 2 == 0:
            res += list_num[i]
    return res


def add_evens_test():
    '''
    This is the fixed test to check if the expected output is the same as
    actual output
    '''
    list_num = [1, 2, 3, 4, 5]
    expected = 6
    actual = add_evens(list_num)
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")

    list_num = [33, 43, 64, 65, 100, 300]
    expected = 464
    actual = add_evens(list_num)
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")


def main():
    add_evens_test()


if __name__ == "__main__":
    main()
