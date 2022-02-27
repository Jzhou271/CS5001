"""
CS5001
Jing Zhou
Coding practice -- Module 5
Add spaces
Write a function called add_spaces that takes a string as input and
uses a loop to add 3 spaces between each letter of the specified string.
"""


def add_spaces(string):
    if not string:
        return ""
    output = ""
    index = 0
    while index < len(string) - 1:
        # output.append(string[index] + "   ")
        # (NOTE: use append() for [] instead)
        output += string[index] + "   "
        index += 1
    # output += string[index]
    output += string[index]
    return output


def main():
    print(add_spaces("Computer"))


if __name__ == "__main__":
    main()
