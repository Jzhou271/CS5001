'''
Sort 3 numbers input by a user. Do not use arrays or any built in python 
sorting method. You must sort them on your own using conditionals. 
1/22/2022
'''


def main():
    first_num = float(input("Input first number: "))
    second_num = float(input("Input second number: "))
    third_num = float(input("Input third number: "))
    if first_num > second_num:
        if first_num > third_num:
            if second_num > third_num:
                print("{}, {}, {}".format(third_num, second_num, first_num))
            else:
                print("{}, {}, {}".format(second_num, third_num, first_num))
        else:
            print("{}, {}, {}".format(second_num, first_num, third_num))
    else:
        if second_num > third_num:
            if first_num > third_num:
                print("{}, {}, {}".format(third_num, first_num, second_num))
            else:
                print("{}, {}, {}".format(first_num, third_num, second_num))
        else:
            print("{}, {}, {}".format(first_num, second_num, third_num))


if __name__ == "__main__":
    main()
