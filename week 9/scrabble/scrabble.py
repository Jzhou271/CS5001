"""
CS5001
Jing Zhou
Lab 9
Dictionaries--Scrabble
write a set of functions that determine the highest-scoring words that contain
specific letters.
"""
import string


def read_text_file():
    '''
    Function -- read_text_file
        Returns the content of the file "wordlist.txt"
    Parameters:
        None
    Returns the contents of the file as a list of strings
    Raises a ValueError if any errors occur while reading the file
        with the message "Error occurred reading the word list"
    '''
    try:
        input_file = open('wordlist.txt', 'r')
        file_data = input_file.readlines()
        input_file.close()
        return file_data
    except FileNotFoundError or PermissionError or OSError:
        raise ValueError("Error occurred reading the word list")


def store_words(file_data):
    '''
    Function -- store_words
        Returns words separated according to their lengths.
    Parameters:
        file_data -- a list of strings containing the words to be sorted
    Returns a dictionary where the key is the word length, and the value
        is all of the words in file_data that of that length
    '''
    words = dict()
    for word in file_data:
        if len(word) in words.keys():
            words[len(word)].append(word.strip())
        else:
            words[len(word)] = [word]
    return words


def interpret_input(data):
    '''
    Function -- interpret_input
        Identifies the letters and number of results to be displayed
        from the user input.
    Parameters:
        data -- string with user response
    Returns the number of highest scoring words to display
        and the letters the word should contain
    '''
    if not isinstance(data, str):
        raise TypeError("interpret_input is expecting a string parameter")

    outputs = ''
    letters = ''
    for i in data:
        # Identify letters
        if i in string.ascii_lowercase:
            letters += i
        # Identify number of results to be displayed
        if i in string.digits:
            outputs += i
    outputs = int(outputs)
    return outputs, letters


def get_words(max_length, word_dict, letters):
    '''
    Function -- get_words
        Returns the words that contain the letters specified by the user.
    Parameters:
        letters -- letters that the words should contain
        word_dict -- With length of words as key and the words as values
        max_length -- maximum length of the word to be displayed
    Returns a list of words containing the user input letters
    '''
    output_list = []
    for key in range(1, max_length + 1):
        try:
            word_list = word_dict[key]
        except KeyError:
            word_list = []

        for word in word_list:
            should_add = True
            for letter in letters:
                if word.count(letter) < letters.count(letter):
                    should_add = False
            if should_add:
                output_list.append(word)
    return output_list


def get_scores(words):
    '''
    Function -- get_scores
        Calculates the score for each word that contains the letters specified
        by the user and then displays 'n' highest scoring words;
        'n' being the number specified by the user.
    Parameters:
        words -- List of words containing the user input letters
    Returns a dictionary containing the points as keys and the words as values
    '''
    letter_scores = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4,
                     'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1,
                     'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
                     's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8,
                     'y': 4, 'z': 10
                     }
    keys = letter_scores.keys()
    values = letter_scores.values()
    score = 0
    get_scores = {}
    for word in words:
        for res in word:
            score += letter_scores[res]
        if score not in get_scores:
            get_scores[score] = [word]
        else:
            get_scores[score].append(word)
        score = 0
    return get_scores


def print_scores(scores, number):
    '''
    Function -- print_scores
        Print the 'n' highest-scoring words based on their scrabble score
    Parameters:
        scores -- dictionary filled with points as keys and words as values
        number -- number of highest scoring words to display
    '''
    if not isinstance(scores, dict):
        raise TypeError("scrabble_scores is expecting a dictionary as"
                        "the first parameter")
    if not isinstance(number, int):
        raise TypeError("scrabble_scores is expecting an integer as"
                        "the second parameter")

    count = 1
    for key in sorted(scores, reverse=True):
        for item in sorted(scores[key]):
            if count != number + 1:
                print(count, item, key)
                count += 1


def get_new_length(cmd):
    '''
    Function -- get_new_length
        Get the new length
    Parameters:
        cmd -- the command to change the length
    Returns the new length
    '''
    if not isinstance(cmd, str):
        raise TypeError("get_new_length is expecting a string as a parameter")
    length = ''
    for i in cmd:
        if i in string.digits:
            length += str(i)
    max_length = int(length)
    return max_length


def main():
    ''' The program driver '''
    file_data = read_text_file()
    word_dict = store_words(file_data)
    scrabble_word_lst = get_words(7, word_dict, 'abcd')
    scrabble_scores = get_scores(scrabble_word_lst)
    print(scrabble_scores)

    return
    max_length = 7

    cmd = input('> ')
    # Process user response
    while cmd != 'quit()':
        if cmd.startswith("len("):
            max_length = get_new_length(cmd)
        else:
            # Identify letters and number of results (n)
            # to display from user response
            outputs, letters = interpret_input(cmd)
            # Identify the words from wordlist.txt
            # that contain user input letters
            scrabble_word_lst = get_words(max_length, word_dict, letters)
            # Calculate the score for each word and add it to a dictionary
            # Tagging the score to the word
            scrabble_scores = get_scores(scrabble_word_lst)
            # Displays 'n' highest scoring words
            print_scores(scrabble_scores, outputs)

        # Get the user's next response if length is not changed
        cmd = input('> ')


if __name__ == '__main__':
    main()
