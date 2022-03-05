"""
Coding practice -- Module 6
8. Compare lists
Write a function called compare_lists that receives two lists of integer
values. The function should return true if all of the elements in the first
list are contained in the second list (but not necessarily in the same order)
"""


def compare_lists(list_1, list_2):
    if(all(i in list_2 for i in list_1)):
        return True
    else:
        return False


def main():
    print(compare_lists([1, 2, 4, 5, 7], [1, 5, 7, 2, 4, 9, 10]))
    print(compare_lists([1, 2, 4, 5, 8], [1, 6, 7, 2, 4]))
    print(compare_lists([99, 100], [1, 6, 7, 2, 4]))


if __name__ == "__main__":
    main()
