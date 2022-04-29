'''
Jing Zhou
CS5001 Final --- recursion question
Write a recursive version of list_of_strings_loop
Write a useful comment for your function
'''
import random


def list_of_strings_loop(number_of_strings):
    """
    This function takes a integer represents number of strings(length) in the
    list. The process randomly take strings from recursion function and return
    a list of strings
    :param: int | number of strings (length) in the return list
    :return: list of string | list of string by input number of strings
    """
    if int(number_of_strings) < 0:
        raise ValueError("Invalid length of string list, number_of_strings"
                         "must greater than 0")
    if type(number_of_strings) != int:
        raise ValueError("Invalid number of strings in the list, "
                         "number_of_strings must be an integer")
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    list_of_strings = []
    for word in range(number_of_strings):
        string_length = random.randint(1, 5)
        this_word = ""

        # for character in range(string_length):
        #     this_word += random.choice(alphabet)

        # take strings from recursion function
        this_word = recursive(string_length, this_word, alphabet)
        # append each word from recursion function to the empty list
        list_of_strings.append(this_word)
    return list_of_strings


def recursive(number_of_times, this_word, alphabet):
    """
    This function takes three parameters for the for loop by making a recursive
    process that randomly choose alphabet character into string words by given
    length, and iterate string length and return   
    :param: int | count how many times to iterate alphabet
    :param: string | every iterate add a character from alphabet
    :param: string | character a-z
    :return: none | function return back to list_of_strings_loop()
    """
    if int(number_of_times) < 0:
        raise ValueError("Invalid repetition, number_of_times must "
                         "greater and equal to 0")

    # base case when no iteration takes place
    if number_of_times == 0:
        return this_word
    # every iterate add a character from alphabet to the word
    this_word += random.choice(alphabet)
    return recursive(number_of_times - 1, this_word, alphabet)


def main():
    print(list_of_strings_loop(4))


if __name__ == "__main__":
    main()
