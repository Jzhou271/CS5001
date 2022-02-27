
"""
CS5001
Jing Zhou
Coding practice -- Module 5
Name Number
Numerologists claim to be able to determine a person's character
traits based on the "numeric value" of a name. The value of a name
is determined by summing up the values of the letters of the name
where "a" is 1, "b" is 2, "c" is 3, etc., up to "z" being 26.
For example, the name "Jump" would have the value 10 + 21 + 13 + 16 = 60
Write a function called name_number that returns the numeric value of a
single named provided to it.
"""


def name_number(name):
    # lowercase for name
    name = name.lower()
    index = 0
    # output starts from 0 (0 + 10 + 10 + 10..)
    ans = 0
    while index < len(name):
        # ord("a") = 97
        ans += ord(name[index]) + ord("a") - 193
        index += 1
    return ans


def main():
    print(name_number("ttttt"))


if __name__ == "__main__":
    main()
