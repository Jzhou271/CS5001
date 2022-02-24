'''
The first function is called biggest. This function should take to numbers 
as parameters. It should compare the two numbers and return the biggest. 

The second function is called biggest_of_four. This function should take 
four parameters, each is a number. It should return the largest of the 
four numbers. It should not make any comparisons inside this function and
instead should make use of your other function, biggest. 

'''


def biggest(num_1, num_2):
    '''
    compare the two numbers and return the bigger one
    :param num_1: a float or an int number to compare to num_2
    :param num_2: a float or an int number to compare to num_1
    :return: a float or an int number is the biggest in num_1 and num_2
    '''
    if num_1 > num_2:
        return num_1
    else:
        return num_2


def biggest_of_four(num_a, num_b, num_c, num_d):
    '''
    comparison in four numbers and return the biggest one
    :param num_a: a float or an int number to compare to num_b, num_c,
    and num_d
    :param num_b: a float or an int number to compare to num_a, num_c,
    and num_d
    :param num_c: a float or an int number to compare to num_a, num_b,
    and num_d
    :param num_d: a float or an int number to compare to num_a, num_b,
    and num_c
    :return: a float or an int number is the biggest among num_a, num_b,
    num_c, and num_d
    '''

    return max(num_a, num_b, num_c, num_d)


def test_biggest(num1, num2, expected):
    '''
    testing the biggest number in two numbers
    '''
    actual = biggest(num1, num2)
    if actual == expected:
        print("PASSED:", actual, "is the biggest")
    else:
        print("FAILED:", expected, "is not the biggest,", actual,
              "is the biggest")


def test_biggest_of_four(num_a, num_b, num_c, num_d, expected):
    '''
    testing the biggest number in four numbers
    '''
    actual = biggest_of_four(num_a, num_b, num_c, num_d)
    if actual == expected:
        print("PASSED:", actual, "is the biggest")
    else:
        print("FAILED", expected, "is not the biggest,", actual,
              "is the biggest")


def main():
    test_biggest(77, 99, 77)
    test_biggest(101111, 2343, 101111)
    test_biggest(0.24354, 0.1, 0.24354)
    test_biggest_of_four(0.322, 0.65, 0.002, 0.46436, 0.65)
    test_biggest_of_four(-3696, -4359, -1633, -1750, -1633)
    test_biggest_of_four(-2948, -3875, -5905, -1402, -1402)


if __name__ == "__main__":
    main()
