'''
CS5001
Lab 4
Question 2 Fibonacci sequence
Jing Zhou

This is the code takes a number between 0 and 10000, to determines if it is
in the Fibonacci sequence.
'''


def is_fibonacci(number):
    '''
    Take a number, and creates a formula to calculate the sequence. The first
    two numbers of sequence are 0 and 1, later sum of the previous two.
    :param number: int, a number between 0 and 10000. 
    :return: boolean, True if function is Fibonacci sequence, False otherwise.
    '''
    number_1 = 0
    number_2 = 1
    sum_two_numbers = number_1 + number_2
    if number == 0:
        return True
    while sum_two_numbers < number:
        number_1 = number_2
        number_2 = sum_two_numbers
        sum_two_numbers = number_1 + number_2
    return number == sum_two_numbers


def test_is_fibonacci():
    '''
    A function for running tests of the is_fibonacci function
    :return:
    '''

    actual = is_fibonacci(3)
    expected = True
    if actual != expected:
        print("3 is FAILED on the test")
    else:
        print("PASSED the test!")
        print("ACTUAL: ", "3", "is", expected)

    actual = is_fibonacci(89)
    expected = True
    if actual != expected:
        print("89 is FAILED on the test")
    else:
        print("PASSED the test!")
        print("ACTUAL: ", "89", "is", expected)

    actual = is_fibonacci(666)
    expected = True
    if actual != expected:
        print("666 is FAILED on the test")
    else:
        print("PASSED the test!")
        print("ACTUAL: ", "666", "is", expected)


def main():
    test_is_fibonacci()


if __name__ == "__main__":
    main()
