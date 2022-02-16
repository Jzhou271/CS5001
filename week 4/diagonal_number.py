'''
CS5001
Lab 4
Question 3 Diagonal Number
Jing Zhou

This is while loop function diagonal_number() designs for Diagonal
number which takes a single parameter as an int.
'''


def diagonal_number(line_number):
    '''
    Takes a single integer to build the while loop. indicate that the
    string has n lines with n number in the end of the first line, follow
    by lines decrase with n-1 number until n = line = number = 1.
    :param: int, the number of lines in a string
    :return: str, diagonal numbers with number of lines
    '''
    ans = ""
    while line_number > 0:
        count = 1
        while count <= line_number:
            ans += str(count) + " "
            count += 1
        ans += "\n"
        line_number -= 1
    return ans


def test_diagonal_number():
    '''
    A function for running tests of the diagonal_number function to check
    wether atucal output is the same as expected
    :return: None
    '''
    actual = diagonal_number(1)
    expected = "1 \n"
    if actual != expected:
        print("FAILED on input 1")
    else:
        print("PASSED on input 1")
        print("ACTUAL:", "output is \n" + actual)
        print("EXPECTED:", "output is \n" + expected)

    actual = diagonal_number(2)
    expected = "1 2 \n1 \n"
    if actual != expected:
        print("FAILED on input 1")
    else:
        print("PASSED on input 1")
        print("ACTUAL:", "output is \n" + actual)
        print("EXPECTED:", "output is \n" + expected)

    actual = diagonal_number(3)
    expected = "1 2 3 \n1 2 \n1 \n"
    if actual != expected:
        print("FAILED on input 1")
    else:
        print("PASSED on input 1")
        print("ACTUAL:", "output is \n" + actual)
        print("EXPECTED:", "output is \n" + expected)


def main():
    test_diagonal_number()


if __name__ == "__main__":
    main()
