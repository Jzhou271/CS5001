"""
CS5001
Jing Zhou
Midterm Coding Portion
5.Coding from a flowchart
Write a function, called flowchart_function, not getting input from a user
using input()
"""
import random
import string


def flowchart_function(input_list):
    """
    This function follows the algorithm described the flowchart. takes a input
    list and return the item at position n, repeated n + 1 times by new row
    end by a "\n"
    :param: list, string
    :return: string, list each string in new row, repeated n + 1 times
    """
    res = ""
    n = 0
    while n < len(input_list):
        res += str(input_list[n]) * (n + 1) + "\n"
        n += 1
    return res


def flowchart_function_fixed_test():
    """
    This is the fixed method to test if the expected output is the same as
    actual output
    :return: None
    """
    actual = flowchart_function(["happy", "birthday", "to", "you", "!"])
    expected = """happy
birthdaybirthday
tototo
youyouyouyou
!!!!!
"""
    if actual != expected:
        print("FIXED TEST FAILED")
    else:
        print("FIXED TEST PASSED")

    actual = flowchart_function(["I", "am", "really", "into", "dance"])
    expected = """I
amam
reallyreallyreally
intointointointo
dancedancedancedancedance
"""
    if actual != expected:
        print("FIXED TEST FAILED")
    else:
        print("FIXED TEST PASSED")

    actual = flowchart_function(["2", "3", "9", "35", "100"])
    expected = """2
33
999
35353535
100100100100100
"""
    if actual != expected:
        print("FIXED TEST FAILED")
    else:
        print("FIXED TEST PASSED")


def flowchart_function_random():
    """
    This is the random method to test if the expected output is the same as
    actual output
    :return: None
    """
    test_list = []
    expected = ""
    for i in range(10):
        test_list.append(random.choice(string.ascii_letters))
        expected += test_list[i] * (i + 1) + "\n"
    actual = flowchart_function(test_list)
    if actual != expected:
        print("RANDOM TEST FAILED")
    else:
        print("RANDOM TEST PASSED")


def main():
    flowchart_function_fixed_test()
    flowchart_function_random()


if __name__ == "__main__":
    main()
