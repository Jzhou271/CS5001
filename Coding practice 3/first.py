"""
Coding practice -- Module 3
4. First
Write a function called first that receives two parameter values and returns
the one that comes first. In the case of two numeric values, it would return
the smaller of the two. In the case of two strings, it would return the one
that comes first lexicographically (e.g., first("cat", "dog") returns "cat")
"""


def first(parameter_1, parameter_2):
    if parameter_1 < parameter_2:
        return parameter_1
    else:
        return parameter_2

    for i in parameter_1:
        for j in parameter_2:
            if i < j:
                return parameter_1
            else:
                return parameter_2


def main():
    print(first(1, 2))
    print(first("cat", "dog"))
    print(first("maybe", "apple"))


if __name__ == "__main__":
    main()
