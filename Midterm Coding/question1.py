"""
CS5001
Jing Zhou
Midterm Coding Portion
1. Correct Commenting
Properly comment the following function, and rename it with an appropriate
name. 
"""


def sort_list(input_list):
    """
    This is a function called sort_list that receives a list of string values
    and reorder that comes first and returns the new list. Strings are sorted
    alphabetically, and numbers are sorted numerically.
    :param: list of inputs, strings
    :return: list, sorted by ascending order
    """
    new_list = []
    for item in input_list:
        if len(new_list) == 0:
            new_list.append(item)
        else:
            index = 0
            while index < len(new_list):
                if item <= new_list[index]:
                    break
                index += 1
            new_list.insert(index, item)
    return new_list


def main():
    print(sort_list([0, 3, -5, 2, 0]))
    print(sort_list(["a", "baf", "caohi", "arh", "eio"]))


if __name__ == "__main__":
    main()
