import readability


def test_count():
    test_word = "read?"
    actual = readability.count_syllables(test_word)
    print(actual)
    expected = 1
    if actual != expected:
        print("FAIL")
    else:
        print("PASS")
        return


def main():
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

    filedata = input_file.readlines()
    sentences, words, syllables = analyze_file_data(filedata)
    input_file.close()
    test_count()

if __name__ == "__main__":
    main()
