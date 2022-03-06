"""
Coding practice -- Module 3
3. Equal
Write a function called is_equal that receives two parameter values and
returns true if they are equal to one another, and false otherwise.
"""


def is_equal(num_1, num_2):
    if num_1 == num_2:
        return True
    else:
        return False


def main():
    print(is_equal(2, 2))
    print(is_equal(2, 5))


if __name__ == "__main__":
    main()
