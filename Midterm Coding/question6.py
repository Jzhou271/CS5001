"""
CS5001
Jing Zhou
Midterm Coding Portion
6. Months and Days
"""


def months_and_days(integer):
    """
    this function take an integer from 1 to 12, and return a string that has
    the name of the corresponding month, followed by a comma, a space, the
    number of days in that month, end with a "\n"
    :param: integer, between 1 and 12 (inclusive)
    :return: string, the name of month
    """
    integer <= 12
    if integer == 1:
        return "January, 31\n"
    elif integer == 2:
        return "February, 28\n"
    elif integer == 3:
        return "March, 31\n"
    elif integer == 4:
        return "April, 30\n"        
    elif integer == 5:
        return "May, 31\n"        
    elif integer == 6:
        return "June, 30\n"
    elif integer == 7:
        return "July, 31\n"
    elif integer == 8:
        return "August, 31\n"
    elif integer == 9:
        return "September, 30\n"
    elif integer == 10:
        return "October, 31\n"
    elif integer == 11:
        return "November, 30\n"
    else:
        return "December, 31\n"


def months_and_days_fixed_test():
    """
    This is the fixed method to test if the expected output is the same as
    actual output
    :return: None
    """
    actual = months_and_days(1)
    expected = "January, 31\n"
    if actual != expected:
        print("TEST FAILED on January")
    else:
        print("TEST PASSED on January")

    actual = months_and_days(2)
    expected = "February, 28\n"
    if actual != expected:
        print("TEST FAILED on February")
    else:
        print("TEST PASSED on February")

    actual = months_and_days(3)
    expected = "March, 31\n"
    if actual != expected:
        print("TEST FAILED on March")
    else:
        print("TEST PASSED on March")

    actual = months_and_days(4)
    expected = "April, 30\n"
    if actual != expected:
        print("TEST FAILED on April")
    else:
        print("TEST PASSED on April")

    actual = months_and_days(5)
    expected = "May, 31\n"
    if actual != expected:
        print("TEST FAILED on May")
    else:
        print("TEST PASSED on May")

    actual = months_and_days(6)
    expected = "June, 30\n"
    if actual != expected:
        print("TEST FAILED on June")
    else:
        print("TEST PASSED on June")

    actual = months_and_days(7)
    expected = "July, 31\n"
    if actual != expected:
        print("TEST FAILED on July")
    else:
        print("TEST PASSED on July")

    actual = months_and_days(8)
    expected = "August, 31\n"
    if actual != expected:
        print("TEST FAILED on August")
    else:
        print("TEST PASSED on August")

    actual = months_and_days(9)
    expected = "September, 30\n"
    if actual != expected:
        print("TEST FAILED on September")
    else:
        print("TEST PASSED on September")

    actual = months_and_days(10)
    expected = "October, 31\n"
    if actual != expected:
        print("TEST FAILED on October")
    else:
        print("TEST PASSED on October")

    actual = months_and_days(11)
    expected = "November, 30\n"
    if actual != expected:
        print("TEST FAILED on November")
    else:
        print("TEST PASSED on November")

    actual = months_and_days(12)
    expected = "December, 31\n"
    if actual != expected:
        print("TEST FAILED on December")
    else:
        print("TEST PASSED on December")


def main():
    months_and_days_fixed_test()


if __name__ == "__main__":
    main()
