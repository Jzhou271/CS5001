'''
Average grade
The file contains a function and tests for average_grade, which takes
a list and compute average of the list
2/23/2022
'''
import random


def average_grade(grade_list):
    '''
    Take a list of grades and return the average value of the list
    :param grade_list: list of float numbers, the value of this list should
    between 0 and 100
    :return: a float number, average of grade_list
    '''
    count = 0
    total_sum = 0
    while count < len(grade_list):
        total_sum += grade_list[count]
        count += 1
    return total_sum / count


def test_average_grade_fixed():
    input_grades = [4, 7, 10]
    actual = average_grade(input_grades)
    expected = 7.0
    if actual != expected:
        print("FAIL on input:", input_grades)
        print("ACTUAL AVERAGE is", actual)
        print("However, EXPECTED AVERAGE is", expected)
    else:
        print("PASS on input: ", input_grades)
        print("ACTUAL AVERAGE is ", actual)
        print("EXPECTED AVERAGE is", expected)

    input_grades = [24, 57, 60, 99]
    actual = average_grade(input_grades)
    expected = 60.0
    if actual != expected:
        print("FAIL on input:", input_grades)
        print("ACTUAL AVERAGE is", actual)
        print("However, EXPECTED AVERAGE is", expected)
    else:
        print("PASS on input: ", input_grades)
        print("ACTUAL AVERAGE is ", actual)
        print("EXPECTED AVERAGE is", expected)

    input_grades = [-45, -35, -15, 6, 65]
    actual = average_grade(input_grades)
    expected = -4.8
    if actual != expected:
        print("FAIL on input:", input_grades)
        print("ACTUAL AVERAGE is", actual)
        print("However, EXPECTED AVERAGE is", expected)
    else:
        print("PASS on input: ", input_grades)
        print("ACTUAL AVERAGE is ", actual)
        print("EXPECTED AVERAGE is", expected)


def test_average_grade_random():
    input_grades = []
    grade_index = 0
    while grade_index < 10:
        input_grades.append(random.random() * 100)
        grade_index += 1
    actual = average_grade(input_grades)
    expected = sum(input_grades) / len(input_grades)
    if actual != expected:
        print("FAIL on input:", input_grades)
        print("ACTUAL AVERAGE is", actual)
        print("However, EXPECTED AVERAGE is", expected)
    else:
        print("PASS on input: ", input_grades)
        print("ACTUAL AVERAGE is ", actual)
        print("EXPECTED AVERAGE is", expected)
        return
    test += 1


def main():
    test_average_grade_fixed()
    test_average_grade_random()


if __name__ == "__main__":
    main()
