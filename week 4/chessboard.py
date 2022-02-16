'''
CS5001
Lab 4
Question 1 Chessboard
Jing Zhou

This code designs for the function chessboard which creates a
chessboard, and for the functions to check that it is working
properly
'''


def chessboard(width, height):
    '''
    Takes a width and a height, and creates a string that
    represents a chessboard. The chessboard is made of alternating
    squres, that are either black (B), or white (W).
    The top leftmost square is B.

    :param width: int, the number of columns in the chessboard(横)
    :param height: int, the number of rows in the chessboard(竖)
    :return: str, a ASCII representation of a chessboard
    '''
    ans = ""
    if width == 1 and height == 1:
        return "B\n"
    elif width % 2 == 0:
        odd_line = width // 2 * "BW"
        even_line = width // 2 * "WB"
    else:
        odd_line = width // 2 * "BW" + "B"
        even_line = width // 2 * "WB" + "W"
    i = 1  # i represents height of row, starts from first row
    while i <= height:
        if i % 2 != 0:
            ans += odd_line + "\n"
        else:
            ans += even_line + "\n"
        i += 1
    return ans


def test_chessboard():
    '''
    A function for running several fixed tests of the chessboard function
    :return:
    '''

    actual = chessboard(2, 3)
    expected = "BW\nWB\nBW\n"
    if actual != expected:
        print("FAILED on input 2, 3")
    else:
        print("PASSED on input 2, 3")
        print("ACTUAL: ", "\n" + actual)
        print("EXPECTED: ", "\n" + expected)

    actual = chessboard(4, 2)
    expected = "BWBW\nWBWB\n"
    if actual != expected:
        print("FAILED on input 4, 2")
    else:
        print("PASSED on input 4, 2")
        print("ACTUAL: ", "\n" + actual)
        print("EXPECTED: ", "\n" + expected)

    actual = chessboard(6, 3)
    expected = "BWBWBW\nWBWBWB\nBWBWBW\n"
    if actual != expected:
        print("FAILED on input 6, 3")
    else:
        print("PASSED on input 6, 3")
        print("ACTUAL: ", "\n" + actual)
        print("EXPECTED: ", "\n" + expected)


def main():
    test_chessboard()


if __name__ == "__main__":
    main()
