'''
Jing Zhou
Final -- gradebook testfile
You must implement a testing class that thoroughly tests
the methods described in gradebook.py

You do not need to implement the methods, the description given
in the comments are sufficient for creating tests
'''
from gradebook import Gradebook
import unittest


class GradeBookTest(unittest.TestCase):
    def test_init(self):
        """
        This test is to check if the constructor works correctly
        """
        gradebook = Gradebook("course_name", 2022, "Spring", "Lee Chard",
                              ["Jack", "Tom"])
        self.assertEqual(gradebook.course_name, "course_name")
        self.assertEqual(gradebook.year, 2022)
        self.assertEqual(gradebook.semester, "Spring")
        self.assertEqual(gradebook.instructor, "Lee Chard")
        self.assertEqual(gradebook.students, ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook(1, 2022, "Spring", "Lee Chard", ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook("course_name", 200, "Spring", "Lee Chard",
                      ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook("course_name", "2022", "Spring", "Lee Chard",
                      ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook("course_name", 2022, "Winter", "Lee Chard",
                      ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook("course_name", 2022, 2022, "Lee Chard",
                      ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook("course_name", 2022, "Spring", 2022,
                      ["Jack", "Tom"])
        with self.assertRaises(ValueError):
            Gradebook("course_name", 2022, "Spring", "Lee", "Tom")
        with self.assertRaises(ValueError):
            Gradebook("course_name", 2022, "Spring", "Lee", ["Tom", 2022])

    def test_average_grade(self):
        """
        This test is to check if average_grade() works correctly
        """

        gradebook = Gradebook("course_name", 2022, "Spring", "Lee Chard",
                              ["Jack", "Tom"])
        self.assertEqual(0, gradebook.average_grade())
        gradebook.add_grade({"Tom": 100, "Jack": 80})
        self.assertEqual(90, gradebook.average_grade())
        gradebook.add_grade({"Tom": 90, "Jack": 70})
        self.assertEqual(170, gradebook.average_grade())

    def test_letter_grade(self):
        """
        This test is to check if letter_grade() works correctly
        """
        gradebook = Gradebook("course_name", 2022, "Spring", "Lee Chard",
                              ["Jack", "Tom"])
        gradebook.add_grade({"Tom": 100, "Jack": 80})
        gradebook.add_grade({"Tom": 90, "Jack": 70})
        with self.assertRaises(ValueError):
            gradebook.letter_grade(0)
        self.assertEqual(gradebook.letter_grade(2),
                         {"Tom": "A", "Jack": "C+"})


def main():
    unittest.main()


if __name__ == "__main__":
    main()
