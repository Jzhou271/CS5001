"""
    Stacks and Queues -- Testcases
    Imports from word.py, and tests the Word class by creating objects,
    calling methods on those objects, and make sure the values of the attributes
    are what we expect.
"""
import unittest
from word import Word
import random


class WordTests(unittest.TestCase):
    """
    This is the unit test class, and it tests all the methods in
    Word class
    """
    def test_init(self):
        """
        This test is to check if the constructor works correctly
        """
        input_string = Word("abccba")
        self.assertEqual(input_string.input_word, "abccba")

    def test_str(self):
        """
        This test is to check if __str__() works correctly
        """
        word = Word("abcddcba")
        actual = word.__str__()
        expected = "abcddcba"
        self.assertEqual(actual, expected)
 

    def test_is_repeat_true(self):
        """
        This test generates repeated words, and tests is_repeat, always
        expecting a True answer
        :return: none
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for repeats in range(2, 11):
            for test in range(500):
                word_length = random.randint(4, 10)
                input_string = ""
            for letter in range(word_length):
                # random append alphabet string character into input_string
                input_string += random.choice(alphabet)

            # repeat input_string
            input_string = input_string * repeats
            word = Word(input_string)
            actual = word.is_repeat(repeats)
            self.assertTrue(actual, input_string)


    def test_is_repeat_false_odd_length(self):
        """
        This test generates repeated words, and tests is_repeat with odd
        characters, and always expecting a False answer
        :return: none
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for repeats in range(2, 11):
            for test in range(500):
                word_length = random.randint(4, 10)
                input_string = ""
            for letter in range(word_length):
                # random append alphabet string character into input_string
                input_string += random.choice(alphabet)

            # repeat input_string
            input_string = input_string * repeats
            input_string += random.choice(alphabet)
            word = Word(input_string)
            actual = word.is_repeat(repeats)
            self.assertFalse(actual, input_string)


    def test_is_repeat_false_even_length(self):
        """
        This test generates repeated words, and tests is_repeat with even
        characters, and always expecting a False answer
        :return: none
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for repeats in range(2, 11):
            for test in range(500):
                word_length = random.randint(4, 10)
                input_string = ""
            for letter in range(word_length):
                # random append alphabet string character into input_string
                input_string += random.choice(alphabet)

            # repeat input_string
            input_string = input_string * (repeats - 1)
            letter_to_add = random.choice(alphabet)
            input_string += letter_to_add * word_length
            word = Word(input_string)
            actual = word.is_repeat(repeats)
            self.assertFalse(actual, input_string)


    def test_is_palindrome_true_even(self):
        """
        This test generates palindrome words, and tests is_palindrome with even
        characters, always expecting a True answer
        :return: none
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for repeats in range(1, 11):
            for test in range(10):
                word_length = random.randint(2, 7)
                input_string = ""
                for letter in range(word_length):
                    # random append alphabet string character into input_string
                    input_string += random.choice(alphabet)

                # this is the palindrome word
                input_string = input_string + input_string[::-1]
                # palindrome repeats n times
                input_string = input_string * repeats
                word = Word(input_string)
                actual = word.is_repeat(repeats)
                self.assertTrue(actual, input_string)


    def test_is_palindrome_true_odd(self):
        """
        This test generates palindrome words, and tests is_palindrome with odd
        characters, always expecting a True answer
        :return: none
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for repeats in range(1, 7):
            for test in range(50):
                word_length = random.randint(1, 3)
                # word_length is odd
                if word_length % 2 != 0:
                    word_length = word_length
                else:
                    word_length = word_length - 1
                input_string = ""
                for letter in range(word_length):
                    # odd random words
                    input_string += random.choice(alphabet)
                # palindrome odd
                input_string = input_string + input_string[::-1]
                input_string = input_string * (2 * repeats + 1)
                word = Word(input_string)
                repeats = 1
                actual = word.is_palindrome(repeats)
                self.assertTrue(actual, input_string)


    def test_is_palindrome_false(self):
        """
        This test generates non-palindrome words, and tests is_palindrome,
        always expecting a False answer
        :return: none
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        for repeats in range(1, 11):
            for test in range(500):
                word_length = random.randint(2, 7)
                input_string = ""
                for letter in range(word_length):
                    input_string += random.choice(alphabet)

                input_string = input_string + "mn" + input_string[::-1]
                input_string = input_string * repeats
                word = Word(input_string)
                actual = word.is_palindrome(repeats)
                #print(actual)
                self.assertFalse(actual, input_string)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
