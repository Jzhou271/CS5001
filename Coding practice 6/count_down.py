"""
Coding practice -- Module 6
2. Count down
Write a function called count_down that uses a for loop to print the
count down from 100 to 0 (inclusive) by 5s. Instead of printing 0,
your code should print Blastoff!
"""


def count_down():
    start = 100
    end = 0
    down = -5
    for i in range(100, 0, -5):
        print(i)
            

def main():
    count_down()


if __name__ == "__main__":
    main()
