"""
Coding practice -- Module 6
6. Add 10
Write a function called add_ten that receives a list of integer values
and adds 10 to each element in the list. The list should then be returned.
"""


def add_ten(list_of_integer):
    for i in range(len(list_of_integer)):
        list_of_integer[i] += 10
    return list_of_integer


def main():
    print(add_ten([2, 7, 19, 24, 67]))


if __name__ == "__main__":
    main()
