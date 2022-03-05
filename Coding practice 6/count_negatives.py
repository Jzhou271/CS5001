"""
Coding practice -- Module 6
5. Count negatives
Write a function called count_negatives that receives a list of integer
values and returns how many of the values in the list are negative. Your
function should return 0 if there are no elements in the list.
"""


def count_negatives(list_of_integer):
    negative_num = 0
    for i in list_of_integer:
        if i < 0:
            negative_num += 1
    return negative_num


def main():
    print(count_negatives([-10, -4, -2, 10, 23, 34, 56]))


if __name__ == "__main__":
    main()
