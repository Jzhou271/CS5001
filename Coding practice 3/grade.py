"""
Coding practice -- Module 3
7. Grade
Using the grade scale for this class (that you can find on the syllabus),
write a function called grade that receives a score and returns the letter
grade for that score.
"""


def grade(points):
    if 93.00 <= points <= 100.00:
        return "A"
    elif 90.00 <= points <= 92.99:
        return "A-"
    elif 86.00 <= points <= 89.99:
        return "B+"
    elif 82.00 <= points <= 85.99:
        return "B"
    elif 77.00 <= points <= 81.99:
        return "B-"
    elif 73.00 <= points <= 76.99:
        return "C+"
    elif 69.00 <= points <= 72.99:
        return "C"
    elif 65.00 <= points <= 68.99:
        return "C-"
    else:
        return "F"


def main():
    print(grade(100))
    print(grade(70))
    print(grade(64.99))


if __name__ == "__main__":
    main()
