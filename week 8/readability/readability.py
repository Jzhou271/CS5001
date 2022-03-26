"""
CS5001
Jing Zhou
Lab 8
What to do
to implement the functions that are required by the provided driver program.
modify the driver program so that any errors that are raised by the modules
are handled by printing an appropriate message to the screen.
"""
import readability


def analyze_file_data(file_data):
    '''
    Function: analyze_file_data
       Calculates the number of sentences, words, and syllabues in file_data
    Parameters:
       file_data -- the data to analyze
    Returns the number of sentences (int), the number of words (int),
       and the number of syllables in file_data
    '''
    sentences = 0
    words = 0
    syllables = 0
    # count number of words
    for line in file_data:
        word_list = line.split()
        words += len(word_list)
    # count number of sentences        
        sentences += line.count('!')
        sentences += line.count('?')
        sentences += line.count(':')
        sentences += line.count(';')
        line.replace('...', '.')
        sentences += line.count('.')
    # count number of syllables
        for word in word_list:
            syllables += count_syllables(word.lower())
    return sentences, words, syllables


def count_syllables(word):
    '''
    Function: count_syllables
       Counts the total number of syllables in the provided word
    Parameters:
       word -- the word that we want to count the syllables of
    Returns the number of syllables in the word
    '''
    word = word.lower()
    consonants = "bcdfghjklmnpqrstvwxz"
    for character in word:
        if not character.isalnum():
            word = word.replace(character, "")
    if word[-1] == 'e':
        word = word[:-1]
    for character in consonants:
        word = word.replace(character, " ")
    groups = word.split()
    syllables = len(groups)
    if syllables == 0:
        syllables = 1
    return syllables


def flesch_index(sentences, words, syllables):
    '''
    Function: flesch_index
       calculates the Flesch readability index
    Parameters:
       sentences (int) -- the number of sentences in a document
       words (int) -- the number of words in a document
       syllables (int) -- the number of syllables
    Returns the Flesch readability index calculated by the provided formula
    '''
    return 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)


def flesch_grade(index):
    '''
    Function: flesch_grade
       Caclulates the Flesch grade (educational level)
    Parameters:
       index (float) -- Flesch readability index
    Returns the educational level
    '''
    if 90 <= index <= 100:
        return "5th Grader"
    elif 80 <= index <= 89.9:
        return "6th Grader"
    elif 70 <= index <= 79.9:
        return "7th Grader"
    elif 65 <= index <= 69.9:
        return "8th Grader"
    elif 50 <= index <= 64.9:
        return "High schooler"
    elif 30 <= index <= 49.9:
        return "College"
    elif 0 <= index <= 29.9:
        return "College graduate"
    elif index < 0:
        return "Law school graduate"


def main():
    """ The main driver of the program. """
    # Ask user for name of file to analyze.
    filename = input("Filename: ")
    try:
        # Open file for reading.
        input_file = open(filename, 'r')
    # case 1: In case the user tries to open a non-existing file
    except FileNotFoundError:
        print(filename, "does not exist")
        return
    # case 2: In case the user tries to open a file they do not have
    # permission to open
    except PermissionError:
        print("Filename", filename, "\n"
              "You do not have sufficient permissions to open", filename)
        return
    # case 3: In case of any operating system error
    except OSError:
        print("Filename", filename, "\n"
              "An unexpected error occurred while attempting to open",
              filename)
        return

    # Read all of the contents of the file
    # into a list of strings called filedata.
    filedata = input_file.readlines()

    # Analyze the data from the file to calculate
    # the number of sentences, the number of words
    # and the number of syllables in the file
    sentences, words, syllables = analyze_file_data(filedata)
    index = flesch_index(sentences, words, syllables)
    grade = flesch_grade(index)

    # Close the file.
    input_file.close()

    # Output result.
    print()
    print("Syllables:", syllables)
    print("Words:", words)
    print("Sentences:", sentences)
    print("Words per Sentence: {0:.1f}".format(words / sentences))
    print("Syllables per Word: {0:.1f}".format(syllables / words))
    print()
    print("Flesch Index: {0:.1f}".format(index))
    print("Flesch Grade:", grade)


if __name__ == '__main__':
    main()
