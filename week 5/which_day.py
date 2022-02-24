"""
Days of the week
This is the file takes an integer between 1 and 7 and returns the corresponding weekday.
2/23/2022
"""


def which_day(number):
    """
    Takes an integer between 1 and 7 and returns the corresponding weekday.
    Start with Sunday, and end with Saturday.
    :param: an integer, between 1 and 7
    :return: string, weekday
    """
    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday",
                "Friday", "Saturday"]
    while number <= len(weekdays):
        return weekdays[number - 1]


def which_day_test_fixed():
    """
    This is the fixed method to test if the function is correct
    """
    actual = which_day(1)
    expected = "Sunday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 1 is", actual, "and expected is", expected)

    actual = which_day(2)
    expected = "Monday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 2 is", actual, "and expected is", expected)

    actual = which_day(3)
    expected = "Tuesday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 3 is", actual, "and expected is", expected)

    actual = which_day(4)
    expected = "Wednesday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 4 is", actual, "and expected is", expected)

    actual = which_day(5)
    expected = "Thursday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 5 is", actual, "and expected is", expected)

    actual = which_day(6)
    expected = "Friday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 6 is", actual, "and expected is", expected)

    actual = which_day(7)
    expected = "Saturday"
    if actual != expected:
        print("FAIL on the test")
    else:
        print("PASS the test")
        print("actual 7 is", actual, "and expected is", expected)


def main():
    which_day_test_fixed()


if __name__ == "__main__":
    main()
