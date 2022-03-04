"""
CS5001
Jing Zhou
Coding practice -- Module 2
Both sides
Write a program that prompts with "Enter value: " and reads in an integer
value from the keyboard and prints the appropriate message depending upon
the value of that input according to the following table.
Even or odd	Value	        Message
Even	        negative	"even negative number"
Even (and 0)	positive	"even positive number"
Odd	        negative	"odd negative number"
Odd	        positive	"odd positive number"
"""


def main():
    num = int(input("Enter value: "))
    if num % 2 == 0:
        if num < 0:
            print("even negative number")
        else:
            print("even positive number")
    else:
        if num < 0:
            print("odd negative number")
        else:
            print("odd positive number")


if __name__ == "__main__":
    main()
