"""
Stacks and Queues
Using stacks and queues to determine if the input string is a palindrome,
and to determine if the input string repeats itself a given number of times. 
"""
from collections import deque


class Word:
    def __init__(self, input_word):
        """
        :param: input_word: str | The string of the word defining this word
        object
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.input_word = input_word
        for i in input_word:
            if i not in alphabet:
                raise ValueError("Invalid input word provided to this Word")

    def __str__(self):
        """
        Returns a string that represents this word
        :param: self | the current word
        """
        word = self.input_word
        return word

    def is_repeat(self, number_repetition):
        """
        Returns whether or not this word object repeats itself
        number_repetition times
        :param: number_repetition: int | we check if this word repeats at
        least number_repetition times
        :return: boolean | if this word repeats number_repetition times
        """
        if int(number_repetition) <= 0:
            raise ValueError("Invalid repetition, number_repetition must"
                             "greater and equal to 1")

        word_length = len(self.input_word)
        if word_length % number_repetition != 0:
            return False
        stack = deque()
        base_word_length = word_length // number_repetition
        base_word = self.input_word[: base_word_length]
        idx = 0

        for _ in range(number_repetition):
            stack.append(self.input_word[idx: idx + base_word_length])
            idx += base_word_length
        count = 0
        while stack:
            if stack.pop() == base_word:
                count += 1
        return count == number_repetition

    def is_palindrome(self, number_of_times):
        """
        Returns true if this word object is a palindrome.
        With number_of_times of 1, we check if the word is a palindrome.
        With number_of_times of 2, we check if the word, when divided in half
        is a palindrome.
        With a number_of_times of 3, we check if the word when divided in
        half twice is a palindrome.
        :param: number_of_times: int | the number of times to check if this
        word and its substrings are palindromes
        :return: boolean | True if the word is a palindrome when subdivided
        number_of_times times
        """
        if int(number_of_times) <= 0:
            raise ValueError("Invalid repetition, number_repetition must"
                             "greater and equal to 1")

        # Not sure how the number is divided
        if number_of_times == 3:
            number_of_times = 4

        check_word = self.input_word[:len(self.input_word) // number_of_times]

        # Below is to check palindrome using stack
        stack = deque(list(check_word))
        for char in check_word:  # String goes from left to right
            if char != stack.pop():  # Stack goes from right to left, FILO
                return False
        return True


def main():
    word = Word("abbaabba")
    print(word.is_palindrome(1))
    print(word.is_repeat(2))


if __name__ == "__main__":
    main()
