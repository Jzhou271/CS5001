"""
Palindrome
This is the function for checking if on input string is a palindrome, also to
test of this function correctness
"""
import random


def is_palindrome(word):
    """
    Takes a string as input and return True if that string is a palindrome (the
    same forward and backward). Otherwise, it returns False
    :param word: string, The string to test
    :return: True if word is palindrome
    """
    count = 0
    while count < len(word):
        if word[count] != word[-1 - count]:
            return False
        count += 1
    return True


def is_palindrome_test_fixed():
    """
    This is the fixed method to test if the input string is palindrome
    """
    input_word = 'fihwh'
    actual = is_palindrome(input_word)
    expected = True
    if actual != expected:
        print("FAIL on the test: ", input_word, "is not palindrome")
    else:
        print("PASS the test:", input_word, "is palindrome")

    input_word = 'racecar'
    actual = is_palindrome(input_word)
    expected = True
    if actual != expected:
        print("FAIL on the test: ", input_word, "is not palindrome")
    else:
        print("PASS the test:", input_word, "is palindrome")


def is_palindrome_test_random():
    """
    This is the random method to test if the input string is palindrome
    """
    input_word = ""
    count = 0
    word_length = random.random() * 15
    while count < word_length:
        input_word += str(int(random.random() * 10))
        count += 1
    input_word += input_word[::-1]
    actual = is_palindrome(input_word)
    expected = True
    if actual != expected:
        print("FAIL on the test: ", input_word, "is not palindrome")
    else:
        print("PASS the test:", input_word, "is palindrome")


def main():
    is_palindrome_test_fixed()
    is_palindrome_test_random()


if __name__ == "__main__":
    main()
