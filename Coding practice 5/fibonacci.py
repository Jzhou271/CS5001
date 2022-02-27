
"""
CS5001
Jing Zhou
Coding practice -- Module 5
Fibonacci list
Write a function called fibonacci that takes a single positive integer
value and returns a list that contains the first n Fibonacci numbers.
The Fibonacci sequences starts 1, 1, 2, 3, 5, 8, ...
"""


def fibonacci(integer):
    # assume [0] = 1
    if integer == 1:
        return [1]
    # assume [0] = 0
    # then there is no value for the list, so it's an empty list
    if integer == 0:
        return []
    # given [0] = 1, then [1] = 1
    ans = [1, 1]
    # index starts from 2
    index = 2
    while index < integer:
        # set the formula for [0] + [1] = [2]
        ans.append(ans[index - 1] + ans[index - 2])
        index += 1
    return ans


def main():
    print(fibonacci(10))


if __name__ == "__main__":
    main()
