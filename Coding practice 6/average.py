"""
Coding practice -- Module 6
4. Calculate average
Write a function called calculate_average that receives a list of integer
values and calculates the average of the values in the list. Your function
should return 0 if there are no elements in the list.
"""


def calculate_average(list_of_integer):
    sum_num = 0
    avg = 0
    for i in list_of_integer:
        sum_num = sum_num + i
    avg = sum_num / len(list_of_integer)
    return avg


def main():
    print(calculate_average([1, 2, 3, 4, 5]))


if __name__ == "__main__":
    main()
