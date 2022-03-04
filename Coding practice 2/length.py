"""
CS5001
Jing Zhou
Coding practice -- Module 2
Length
Write a program that reads a measurement in meters and the converts
it to inches, feet, and miles. There are 39.3701 inches in a meter
"""


def main():
    length_meter = float(input("Enter length: "))
    inches = length_meter * 39.3701
    feet = length_meter * 3.2808411
    miles = length_meter * 0.000621371
    print("The length in inches is", inches)
    print("The length in feet is", feet)
    print("The length in miles is", miles)


if __name__ == "__main__":
    main()
