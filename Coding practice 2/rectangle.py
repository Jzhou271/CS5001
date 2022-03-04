
"""
CS5001
Jing Zhou
Coding practice -- Module 2
Rectangle
Write a program that reads the length of a rectangle's sides and then prints
the area and perimeter of the rectangle the length of the diagonal
(use the Pythagorean theorem)
"""


def main():
    width = float(input("Enter width:"))
    height = float(input("Enter height:"))
    area_rectangle = float(width * height)
    perimeter_rectangle = float(2 * (width + height))
    diagonal = float((width ** 2 + height ** 2) ** 0.5)
    print("The area of the rectangle is", area_rectangle)
    print("The perimeter of the rectangle is", perimeter_rectangle)
    print("The diagonal of the rectangle is", diagonal)


if __name__ == "__main__":
    main()
