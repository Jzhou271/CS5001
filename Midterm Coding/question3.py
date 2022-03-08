"""
CS5001
Jing Zhou
Midterm Coding Portion
3. Testing
write test for the following function declaration by random inputs.
name test function what the test is actually tested
"""
import random


def find_smallest(list_of_numbers):
    """
    find_smallest takes a list of numbers
    and returns the smallest value in the list
    :param: list_of_numbers: A list of any numbers, of any size
    :return: the smallest value in list_of_numbers
    """
    return min(list_of_numbers)


def find_smallest_random():
    """
    This is the random method to test if the expected output is the same as
    actual output
    :return: None
    """
    nums = []
    for i in range(10):
        nums.append(random.randint(-100, 100))
        nums.sort()
    print("random list:", nums)
    expected = nums[0]
    actual = find_smallest(nums)
    if actual != expected:
        print("TEST FAILED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)
    else:
        print("TEST PASSED")
        print("EXPECTED = ", expected)
        print("ACTUAL = ", actual)


def main():
    print(find_smallest([1, 2, 4, 5, 43, 3, 22]))
    find_smallest_random()


if __name__ == "__main__":
    main()
