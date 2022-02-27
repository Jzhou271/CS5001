"""
Coding practice -- Module 5
diagonal string
Write a function called diagonal_string that takes a string as a parameter
and returns each letter diagonally on a new line
"""


def diagonal_string(string):
    if not string:
        return ""
    index = 0
    output = ""
    while index < len(string) - 1:
        # " " * index represents add a whitespace for each row starts
        output += " " * index + string[index] + "\n"
        index += 1
    output += " " * index + string[index]
    return output


def main():
    print(diagonal_string("northeastern"))
    print(diagonal_string(""))


if __name__ == "__main__":
    main()
