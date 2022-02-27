"""
Rocket Ship
This is the file to draw a rocket ship. The program should use for a
size 3 or greater
2/25/2022
"""


def rocket_top_and_bottom(size_n):
    '''
    rocket_top_and_bottom() designed for the top and bottom piece of
    the rocket
    :param: integer, the size of rocket
    :return: string, representing the rocket top and bottom
    '''
    slash = "/"
    back_slash = "\\"
    space = " "
    stars = "**"
    row = 1
    space_count = size_n * 2 - 1
    res = ''
    while row <= (2 * size_n - 1):
        slash_count = row
        back_slash_count = row
        res += space * space_count + slash * row \
            + stars + back_slash * row + "\n"
        row += 1
        space_count -= 1
    return res 


def devi_line(size_n):
    '''
    devi_line() designed for a divider line to connect each function
    :param: integer, the size of rocket
    :return: string
    '''
    plus_sign = "+"
    devi_line = "=*"
    count = 2 * size_n
    row = 1
    count = 2 * size_n
    return plus_sign + devi_line * count + plus_sign + "\n"


def rocket_body_1(size_n):
    '''
    rocket_body_1() designed for the first piece of rocket body, displayed as
    two standing congruent trangles
    :param: integer, the size of rocket
    :return: string, representing two standing trangles in rocket body
    '''
    row = 0
    n = size_n
    vertical_bar = "|"
    slash = "/"
    backslash = "\\"
    dot = "."
    res = ""
    while row < size_n + n:
        res = res + vertical_bar + dot * row + (backslash + slash) * size_n \
              + dot * row + dot * row + (backslash + slash) * size_n \
              + dot * row + vertical_bar + "\n"
        row += 1
        size_n -= 1
    return res


def rocket_body_2(size_n):
    '''
    rocket_body_2() designed for the second piece of rocket body, displayed as
    two inverted congruent trangles
    :param: integer, the size of rocket
    :return: string, representing two inverted trangles in rocket body
    '''
    i = 1
    dot_count = size_n - 1
    vertical_bar = "|"
    slash = "/"
    backslash = "\\"
    dot = "."
    res = ""
    while i < size_n + 1:
        res += vertical_bar + dot * dot_count + (slash + backslash) * i \
               + 2 * dot * dot_count + (slash + backslash) * i \
               + dot * dot_count + vertical_bar + "\n" 
        i += 1
        dot_count -= 1
    return res


def rocket(size_n):
    '''
    rocket() is the combinating function gather all subset function to call
    and return the final output
    :param: integer, the size of rocket
    :return: string, gather all string from subset functions
    '''
    res = ""
    res += rocket_top_and_bottom(size_n)
    res += devi_line(size_n)
    res += rocket_body_1(size_n)
    res += rocket_body_2(size_n)
    res += devi_line(size_n)
    res += rocket_body_2(size_n)
    res += rocket_body_1(size_n)
    res += devi_line(size_n)
    res += rocket_body_1(size_n)
    res += rocket_body_2(size_n)
    res += devi_line(size_n)
    res += rocket_top_and_bottom(size_n)
    return res


def rocket_test_fixed():
    """
    This is the fixed method to test if the output is correct
    """
    res = rocket(3)
    print(res)


def rocket_test_loop():
    """
    This is the loop method of size range to test if the output is correct
    """
    n = 3
    while n < 6:
        print(n)
        res = rocket(n)
        n += 1
        print(res, '\n')


def main():
    rocket_test_fixed()
    rocket_test_loop()


if __name__ == "__main__":
    main()
