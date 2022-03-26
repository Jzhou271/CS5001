import readability


def test_analyze_file_data():
    """
    This is the fixed test for analyze_file_data() in readability.py,
    to check if actual outputs are the same as expected outputs
    """
    # test method using input a txt file to runout the output
    input_file = open("declaration.txt")
    actual_sentences, actual_words, actual_syllables = \
        readability.analyze_file_data(input_file)
    expected_sentences, expected_words, expected_syllables = 56, 1322, 2178
    if actual_sentences != expected_sentences or \
            actual_words != expected_words or \
            actual_syllables != expected_syllables:
        print("FAILED ON THE TEST")
        print("Expected sentences is", expected_sentences,
              "But actual sentences is", actual_sentences)
        print("Expected words is", expected_words,
              "But actual words is", actual_words)
        print("Expected syllables is", expected_syllables,
              "But actual syllables is", actual_syllables)
    else:
        print("PASSED ON THE TEST")

    # test method using input a string to runout the output
    test_text = ["flesch invented a simple tool to estimate the \
legibility of a document without linguistic analysis."]
    actual_sentences, actual_words, actual_syllables = \
        readability.analyze_file_data(test_text)
    expected_sentences, expected_words, expected_syllables = 1, 15, 31
    if actual_sentences != expected_sentences or \
            actual_words != expected_words or \
            actual_syllables != expected_syllables:
        print("FAILED ON THE TEST")
        print("Expected sentences is", expected_sentences,
              "But actual sentences is", actual_sentences)
        print("Expected words is", expected_words,
              "But actual words is", actual_words)
        print("Expected syllables is", expected_syllables,
              "But actual syllables is", actual_syllables)
    else:
        print("PASSED ON THE TEST")

        test_text = ["Don't worry it works great!"]
    actual_sentences, actual_words, actual_syllables = \
        readability.analyze_file_data(test_text)
    expected_sentences, expected_words, expected_syllables = 1, 5, 6
    if actual_sentences != expected_sentences or \
            actual_words != expected_words or \
            actual_syllables != expected_syllables:
        print("FAILED ON THE TEST")
        print("Expected sentences is", expected_sentences,
              "But actual sentences is", actual_sentences)
        print("Expected words is", expected_words,
              "But actual words is", actual_words)
        print("Expected syllables is", expected_syllables,
              "But actual syllables is", actual_syllables)
    else:
        print("PASSED ON THE TEST")


def test_count_syllables():
    """
    This is the fixed test for count_syllables() in readability.py,
    to check if actual output is the same as expected output
    """
    test_word = "goirghrwuhweeqqqaaa"
    actual = readability.count_syllables(test_word)
    expected = 4
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected count syllables is", expected,
              "But actual count syllables is", actual)
    else:
        print("PASSED ON THE TEST")

        test_word = "dontworryitok"
    actual = readability.count_syllables(test_word)
    expected = 4
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected count syllables is", expected,
              "But actual count syllables is", actual)
    else:
        print("PASSED ON THE TEST")


def test_flesch_grade():
    """
    This is the fixed test for flesch_grade() in readability.py,
    to check if actual output is the same as expected output
    """
    test_grade = 54.2
    actual = readability.flesch_grade(test_grade)
    expected = "High schooler"
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected flesch grade is", expected,
              "But actual flesch grade is", actual)
    else:
        print("PASSED ON THE TEST")

    test_grade = 98.5
    actual = readability.flesch_grade(test_grade)
    expected = "5th Grader"
    if actual != expected:
        print("FAILED ON THE TEST")
        print("Expected flesch grade is", expected,
              "But actual flesch grade is", actual)
    else:
        print("PASSED ON THE TEST")
        return


def main():
    test_analyze_file_data()
    test_count_syllables()
    test_flesch_grade()


if __name__ == "__main__":
    main()
