"""
CS5001
Jing Zhou
Homework 4 Rocket Ship
2/25/2022
This is the file to draw a rocket ship. The program should use for a
size 3 or greater
"""


def rocket(size_n):
    if size_n < 3:
        print("Rocket sizes must be at least 3")
    else:
        rocket_top_and_bottom(size_n)
        devi_line(size_n)
        rocket_body_1(size_n)
        rocket_body_2(size_n)


def rocket_top_and_bottom(size_n):
    slash = "/"
    back_slash = "\\"
    space = " "
    stars = "**"
    row = 1
    space_count = size_n * 2 - 1
    while row <= (2 * size_n - 1):
        slash_count = row
        back_slash_count = row
        print(space * space_count + slash * row + stars + back_slash * row)
        row += 1
        space_count -= 1


def devi_line(size_n):
    plus_sign = "+"
    devi_line = "=*"
    count = 2 * size_n
    row = 1
    count = 2 * size_n
    while row < (2 * size_n):
        print(plus_sign + devi_line * count + plus_sign)
        break


def rocket_body_1(size_n):
    row = 0
    n = size_n
    vertical_bar = "|"
    slash = "/"
    backslash = "\\"
    dot = "."

    while row < size_n + n:
        print(
            vertical_bar + dot * row + (backslash + slash) * size_n
              + dot * row + dot * row + (backslash + slash) * size_n
              + dot * row + vertical_bar
            )
        row += 1
        size_n -= 1


def rocket_body_2(size_n):
    i = 1
    dot_count = size_n - 1
    vertical_bar = "|"
    slash = "/"
    backslash = "\\"
    dot = "."
    while i < size_n + 1:
        print(
            vertical_bar + dot * dot_count + (slash + backslash) * i +
              2 * dot * dot_count + (slash + backslash) * i + dot * dot_count
              + vertical_bar
            )
        i += 1
        dot_count -= 1


def main():
    size_n = int(input("Enter size_n: "))
    rocket_top_and_bottom(size_n)
    devi_line(size_n)
    rocket_body_1(size_n)
    rocket_body_2(size_n)
    devi_line(size_n)
    rocket_body_2(size_n)
    rocket_body_1(size_n)
    devi_line(size_n)
    rocket_body_1(size_n)
    rocket_body_2(size_n)
    devi_line(size_n)
    rocket_top_and_bottom(size_n)


if __name__ == "__main__":
    main()
