"""
Coding practice -- Module 3
6. Area of Triangle
Write a function called area_triangle that returns the area of a triangle
given the length of its three sides as parameters.
"""
import math


def area_triangle(side1, side2, side3):
    s_value = (side1 + side2 + side3) / 2
    res = s_value * (s_value - side1) * (s_value - side2) * (s_value - side3)
    return math.sqrt(res)


def main():
    print(area_triangle(5, 4, 3))


if __name__ == "__main__":
    main()
