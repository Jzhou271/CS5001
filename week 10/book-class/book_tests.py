"""
CS5001
Jing Zhou
Lab 10
    Classes and Objects -- test suit for a class.
    Imports from book.py, and tests the Book class by creating objects,
    calling methods on those objects, and make sure the values of the
    attributes are what we expect.
"""
from book import Book
import unittest


class CrashTest(unittest.TestCase):
    """
    This is the unit test class, and it tests all the methods in
    Book class
    """
    def test_init(self):
        """
        This test is to check if the constructor works correctly
        """
        book = Book("9780394800011", "Cat in the Hat", "Dr. Suess", 1957,
                    "Hardcover", "college.txt")
        self.assertEqual(book.isbn, "9780394800011")
        self.assertEqual(book.title, "Cat in the Hat")
        self.assertEqual(book.author, "Dr. Suess")
        self.assertEqual(book.year, 1957)
        self.assertEqual(book.type_of_book, "Hardcover")
        self.assertEqual(book.filename, "college.txt")
        with self.assertRaises(ValueError):
            Book("978987456321", "college", "abc abc", 2022,
                 "PDF", "college.txt")
        with self.assertRaises(ValueError):
            Book("9780394800011", 123, "Dr.Rick", 1994, "PDF", "college.txt")

    def test_get_title(self):
        """
        This test is to check if get_title() works correctly
        """        
        book = Book("9780394800011", "Widely UU", "Celia Q", 1999,
                    "PDF", "college.txt")
        self.assertEqual(book.get_title(), "Widely UU")

    def test_get_author(self):
        """
        This test is to check if get_author() works correctly
        """ 
        book = Book("9780394800011", "Widely UU", "IvyAtemis", 1999,
                    "PDF", "college.txt")
        self.assertEqual(book.get_author(), "IvyAtemis")

    def test_get_year(self):
        """
        This test is to check if get_year() works correctly
        """ 
        book = Book("9780394800011", "Widely UU", "IvyAtemis", 1999,
                    "PDF", "college.txt")
        self.assertEqual(book.get_year(), 1999)

    def test_get_format(self):
        """
        This test is to check if get_format() works correctly
        """ 
        book = Book("9780394800011", "Widely UU", "IvyAtemis", 1999,
                    "PDF", "college.txt")
        self.assertEqual(book.get_format(), "PDF")
    
    def test_get_filename(self):
        """
        This test is to check if get_filename() works correct
        """ 
        book = Book("9780394800011", "Widely UU", "IvyAtemis", 1999,
                    "PDF", "college.txt")
        self.assertEqual(book.get_filename(), "college.txt")
    
    def test_get_readability_grade(self):
        """
        This test is to check if get_readability_grade() works correctly
        """ 
        book = Book("9789874563216", "Widely UU", "IvyAtemis", 2022,
                    "PDF", "college.txt")
        self.assertEqual(book.get_readability_grade(),
                         "College graduate")

    def test_get_index(self):
        """
        This test is to check if get_index() works correctly
        """ 
        book = Book("9780394800011", "college", "Dr.Rick", 1988,
                    "Hardcover", "college.txt")
        actual = book.get_index()
        expected = {'a': 2, 'analysis': 1, 'document': 1, 'estimate': 1,'flesch': 1,
                    'invented': 1, 'legibility': 1, 'linguistic': 1,
                    'of': 1, 'simple': 1, 'the': 1, 'to': 1, 'tool': 1,
                    'without': 1}
        self.assertDictEqual(actual, expected)

    def test_str(self):
        """
        This test is to check if __str__() works correctly
        """ 
        book = Book("9780394800011", "college", "Dr.Rick", 1988,
                    "Hardcover", "college.txt")
        actual = book.__str__()
        expected = "college by Dr.Rick, 1988\nISBN: 9780394800011, Hardcover, College graduate, college.txt"
        self.assertEqual(actual, expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
