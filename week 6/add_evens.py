"""
Question 3 Adding Evens
"""
import random


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
        print("FAILED the test", list_num)
    else:
        print("PASSED the test")

    list_num = [33, 43, 64, 65, 100, 300]
    expected = 464
    actual = add_evens(list_num)
    if expected != actual:
        print("FAILED the test", list_num)
    else:
        print("PASSED the test")


def random_test():
    nums = []
    for i in range(10):
        nums.append(random.randint(0, 500))  
    res = add_evens(nums)
    test = 0
    for num in nums:
        if num % 2 == 0:
            test += num
    if test != res:
        print("RANDOM: FAILED the test")
    else:
        print("RANDOM: PASSED the test")


def main():
    add_evens_test()
    random_test()


if __name__ == "__main__":
    main()
