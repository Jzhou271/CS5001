"""
CS5001
Jing Zhou
Lab 9
Test file for scrabble.py
"""
import scrabble


def test_store_words():
    """
    This is the test function to test store_words() in file scrabble.py.
    it takes a list of string of words as input test parameter, defined as the
    variable "abc", get words output of a dictionary where the key is the word
    length, and the value is all of the words in "abc"
    """
    abc = ['abduce', 'abduct', 'bardic', 'braced', 'cabled']
    actual_words = scrabble.store_words(abc)
    expected_words = {6: ['abduce', 'abduct', 'bardic', 'braced', 'cabled']}
    if actual_words != expected_words:
        print("FAILED ON THE TEST")
        print("Expected output is", actual_words)
        print("Actual output is", expected_words)
    else:
        print("PASSED ON THE TEST")

    abc = ['newts', 'newest', 'strewn', 'twines', 'wisent']
    actual_words = scrabble.store_words(abc)
    expected_words = {5: ['newts'],
                      6: ['newest', 'strewn', 'twines', 'wisent']}
    if actual_words != expected_words:
        print("FAILED ON THE TEST")
        print("Expected output is", actual_words)
        print("Actual output is", expected_words)
    else:
        print("PASSED ON THE TEST")


def test_get_scores():
    """
    This is the test function to test get_scores() in file scrabble.py.
    it takes a list of words of words as input of test parameter, defined as 
    variable "words", get output scores of a dictionary where a dictionary
    containing the score points as keys and the words as values in "words"
    """
    words = ['abduce', 'abduct', 'bardic', 'braced', 'cabled']
    actual_scores = scrabble.get_scores(words)
    expected_scores = {11: ['abduce', 'abduct', 'bardic', 'braced', 'cabled']}
    if actual_scores != expected_scores:
        print("FAILED ON THE TEST")
        print("Expected output is", actual_scores)
        print("Actual output is", expected_scores)
    else:
        print("PASSED ON THE TEST")

    words = ['newts', 'newest', 'strewn', 'twines', 'wisent']
    actual_scores = scrabble.get_scores(words)
    expected_scores = {8: ['newts'],
                       9: ['newest', 'strewn', 'twines', 'wisent']}
    if actual_scores != expected_scores:
        print("FAILED ON THE TEST")
        print("Expected output is", actual_scores)
        print("Actual output is", expected_scores)
    else:
        print("PASSED ON THE TEST")


def test_get_words():
    """
    This is the test function to test get_words() in file scrabble.py.
    it takes max_length of output words, letters that the output words should
    contain, and a dictionary of words that has key of length of words and
    values of words. get a output list of words contains test_letters
    """
    test_max_length = 7
    test_word_dict = {6: ['abduce', 'abduct', 'bached', 'backed',
                          'bardic', 'braced', 'cabbed', 'cabled']}
    test_letters = 'abcd'
    actual_output_list = scrabble.get_words(test_max_length,
                                            test_word_dict, test_letters)
    expected_output_list = ['abduce', 'abduct', 'bached', 'backed',
                            'bardic', 'braced', 'cabbed', 'cabled']
    if actual_output_list != expected_output_list:
        print("FAILED ON THE TEST")
        print("Expected output is", actual_output_list)
        print("Actual output is", expected_output_list)
    else:
        print("PASSED ON THE TEST")

    test_max_length = 7
    test_word_dict = {5: ['newts'],
                      6: ['newest', 'strewn', 'twines', 'wisent']}
    test_letters = 'newst'
    actual_output_list = scrabble.get_words(test_max_length,
                                            test_word_dict, test_letters)
    expected_output_list = ['newts', 'newest', 'strewn', 'twines', 'wisent']
    if actual_output_list != expected_output_list:
        print("FAILED ON THE TEST")
        print("Expected output is", actual_output_list)
        print("Actual output is", expected_output_list)
    else:
        print("PASSED ON THE TEST")


def main():
    test_store_words()
    test_get_scores()
    test_get_words()


if __name__ == '__main__':
    main()
