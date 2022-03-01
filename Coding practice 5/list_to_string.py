"""
Coding practice -- Module 5
List to string
Write a function called list_to_string, that takes a list as a parameter
and returns a string with each element of the list on its own line.
"""


def list_to_string(string):
    if not string:
        return ""
    output = ""
    index = 0
    while index < len(string):
        output += str(string[index]) + "\n"
        index += 1
    return output.strip()


def main():
    print(list_to_string(["khoury", "college", "align", "masters"]))


if __name__ == "__main__":
    main()
