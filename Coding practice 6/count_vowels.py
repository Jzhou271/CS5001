"""
Coding practice -- Module 6
3. Count vowels
Write a function called count_vowels that takes a string as an input and
returns the number of vowels (a, e, i, o, u) that are found in the sentence.
"""


def count_vowels(string):
    vowels = ("aeiouAEIOU")
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count


def main():
    print(count_vowels("this is a sentence"))


if __name__ == "__main__":
    main()
