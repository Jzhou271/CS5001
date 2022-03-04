"""
CS5001
Jing Zhou
Coding practice -- Module 2
Pairs
Write a program that reads four integers from the keyboard and prints
"two pairs" if the input consists of two matching pairs (in some order)
and "not two pairs" otherwise.
1 2 2 1   two pairs
1 2 2 3   not two pairs
2 2 2 2   two pairs
"""


def main():
    num_1 = int(input("Enter num_1: "))
    num_2 = int(input("Enter num_2: "))
    num_3 = int(input("Enter num_3: "))
    num_4 = int(input("Enter num_4: "))
    if num_1 == num_2 == num_3 == num_4:
        print(num_1, num_2, num_3, num_4, "two pairs")
    elif num_1 == num_2 or num_1 == num_3 or num_1 == num_4 \
            and num_2 == num_3 or num_2 == num_4:
        print(num_1, num_2, num_3, num_4, "two pairs")
    else:
        print(num_1, num_2, num_3, num_4, "not two pairs")


if __name__ == "__main__":
    main()
