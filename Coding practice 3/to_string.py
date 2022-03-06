"""
Coding practice -- Module 3
8. To string
Write a function called to_string that takes any value as a parameter and
returns the string equivalent of that parameter.
"""


def to_string(string):
    return str(string)


def main():
    print(to_string(54))
    print(to_string(867.5309))
    print(to_string("Arthur, King of the Brits!"))
    print(to_string("None"))


if __name__ == "__main__":
    main()
