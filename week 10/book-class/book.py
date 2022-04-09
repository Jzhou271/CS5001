import readability
import os
import string


class Book:
    """
        class: Book
        Attributes: self, isbn, title, author, year, type_of_book, filename
        Methods:
        get_title(get book title)
        get_author(get author's name)
        get_year(get year of book is published)
        get_format(get type of book)
        get_filename(read txt file from input)
    """
    def __init__(self, isbn, title, author, year, type_of_book, filename):
        """
        Constructor -- creates new instances of book
        Parameters:
           self -- the current object
           isbn -- isbn number of a book
           title -- book name
           author -- book author
           year -- year of book
           book format -- type of book
           filename -- read txt file from input
        May raise ValueError because invalid string is provided to the book.
        or os path is incorrect while read the file
        """
        if type(isbn) != int and len(str(isbn)) != 13:
            raise ValueError("Invalid ISBN provided to this Book")
        if str(isbn)[0] != "9" and \
           (str(isbn)[1:2] != "78" or str(isbn)[1:2] != "79"):
            raise ValueError("Invalid ISBN provided to this Book")
        if type(title) is not str:
            raise ValueError("Invalid title provided to this Book")
        if type(author) is not str:
            raise ValueError("Invalid author provided to this Book")
        if type(year) is not int:
            raise ValueError("Invalid year provided to this Book")
        if type_of_book not in ["Hardcover", "Softcover", "Kindle", "PDF"]:
            raise ValueError("Invalid format provided to this Book")
        if not os.path.isfile(filename):
            raise ValueError("Invalid filename provided to this Book")

        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        self.type_of_book = type_of_book
        self.filename = filename

    def get_title(self):
        """
        get_title(get book title)
        :param: self, the current object
        :return: none
        """
        return self.title

    def get_author(self):
        """
        get_author(get author's name)
        :param: self, the current object
        :return: none
        """
        return self.author

    def get_year(self):
        """
        get_year(get year of book is published)
        :param: self, the current object
        :return: none
        """
        return self.year

    def get_format(self):
        """
        get_format(get type of book)
        :param: self, the current object
        :return: none
        """
        return self.type_of_book

    def get_filename(self):
        """
        get_filename(read txt file from input)
        :param: self, the current object
        :return: none
        """
        return self.filename

    def __str__(self):
        """
        Method -- returns a string that represents this book
        :param: self, the current object
        return: none
        """
        ref = self.get_title() + " by " + self.get_author()
        ref += ", " + str(self.get_year()) + "\n"
        ref += "ISBN: " + str(self.isbn) + ", "
        ref += self.get_format() + ", " + str(self.get_readability_grade())
        ref += ", " + self.filename
        return ref

    def get_readability_grade(self):
        """
        May raise OSError, or PermissionError or FileNotFoundError because
        this method uses open() and the file may have been removed, or may
        not have the correct permissions. import readability file to return
        sentences, words, syllables, index, and grade
        :param: self, the current object
        :return: none
        """
        try:
            file = open(self.filename)
            file_data = file.readlines()
            file.close()
            sentences, words, syllables = \
                readability.analyze_file_data(file_data)
            index = readability.flesch_index(sentences, words, syllables)
            grade = readability.flesch_grade(index)
        except PermissionError or FileNotFoundError or OSError:
            raise ValueError("Error occurred while calculating the Flesch \
                              grade for Cat in the Hat")
        return grade

    def get_index(self):
        """
        May raise OSError, or PermissionError or FileNotFoundError because
        this method uses open() and the file may have been removed, or may
        not have the correct permissions.
        Word as the key and the number of times it appears in the txt file as
        the value
        :param: self, the current object
        :return: none
        """
        try:
            file = open(self.filename)
            file_data = file.readlines()
            file.close()
        except OSError or PermissionError:
            raise ValueError("Error occurred while generating the index for \
                              Cat in the Hat")
        dictionary = dict()
        line = ""
        for lines in file_data:
            line = line.lower()
            line += lines.strip()
        for hyphen in range(len(line)):
            # remove punctuation marks from line
            line = line.translate(line.maketrans("", "", string.punctuation))
        words = line.split(" ")
        for word in words:
            # check if the word is already in dictionary
            if word in dictionary:
                # increment count of word by 1
                dictionary[word] = dictionary[word] + 1
            else:
                # add the word to dictionary with count 1
                dictionary[word] = 1
        return dictionary
