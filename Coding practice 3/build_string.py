"""
Coding practice -- Module 3
9. Building a string
Write a function called build_string that takes a string value, and three
integer values and returns a single string containing 3 lines. One each line,
the string value is repeated the specified number of times. For example,
if I were to call it with build_string("hi", 4, 2, 3) I would get the string:

hihihihi
hihi
hihihi

"""


def build_string(string, num1, num2, num3):
    line1 = string * num1
    line2 = string * num2
    line3 = string * num3
    return line1 + "\n" + line2 + "\n" + line3


def main():
    print(build_string("yes", 7, 3, 5))


if __name__ == "__main__":
    main()
