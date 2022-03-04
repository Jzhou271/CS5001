"""
Question 1 Days of the week returns
"""

import which_day


def get_day_string():
    '''
    This function returns a string that has every day, starting from Sunday,
    separated by a space. No space at the end of the string
    :return: str, all the day names in order, with a space between them
    '''
    days = [which_day.which_day(1), which_day.which_day(2),
            which_day.which_day(3), which_day.which_day(4),
            which_day.which_day(5), which_day.which_day(6),
            which_day.which_day(7)]
    string = ""
    for i in range(len(days)):
        string += days[i] + " "
        string += ""
    return string.strip()


def get_day_string_test():
    '''
    This is the fixed test to check if the expected output is the same as
    actual output
    '''
    expected = "Sunday Monday Tuesday Wednesday Thursday Friday Saturday"
    actual = get_day_string()
    if expected != actual:
        print("FAILED the test")
    else:
        print("PASSED the test")


def main():
    print(get_day_string())
    get_day_string_test()


if __name__ == "__main__":
    main()
