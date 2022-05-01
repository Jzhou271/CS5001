'''
recursion testfile
'''
import recursion
import unittest


class Testrecursion(unittest.TestCase):
    def test_positive_integer(self):
        """
        This test function has a positive integer as input, and we are also
        testing the size of the output, to see if it matches with the input
        length
        """
        input_number = 3
        output = recursion.list_of_strings_loop(input_number)
        self.assertEqual(input_number, len(output))

    def test_zero_input(self):
        """
        The test function tests 0 input case for list_of_strings_loop(),
        will be return an empty list
        """
        test_list = 0
        actual = recursion.list_of_strings_loop(test_list)
        expected = []
        self.assertEqual(actual, expected)

    def test_negative_input(self):
        """
        The test function tests negative number input for
        list_of_strings_loop(), will be raise ValueError
        """
        with self.assertRaises(ValueError):
            recursion.list_of_strings_loop(-5)

    def test_type_of_input_float(self):
        """
        The test function tests type of input number for list_of_strings_loop        
        the type of number must be an integer, otherwise, will be raise
        ValueError
        """
        with self.assertRaises(ValueError):
            recursion.list_of_strings_loop(3.77)

    def test_type_of_input_boolean(self):
        """
        The test function tests type of input number for list_of_strings_loop        
        the type of number must be an integer, otherwise, will be raise
        ValueError
        """
        with self.assertRaises(ValueError):
            recursion.list_of_strings_loop(True)

    def test_recursive_fixed(self):
        """
        The test function tests fixed and small values for recursive(), to
        check if the recursive() works correctly
        """
        actual = recursion.recursive(1, 'q', 'q')
        expected = 'qq'
        self.assertEqual(actual, expected)

        actual = recursion.recursive(2, 'c', 'c')
        expected = 'ccc'
        self.assertEqual(actual, expected)

        actual = recursion.recursive(3, 'fff', 'fff')
        expected = 'ffffff'
        self.assertEqual(actual, expected)

    def test_recursive_negative_iteration(self):
        """
        The test function tests negative number input for number of times of
        iteration in recursive(), will be raise ValueError
        """
        with self.assertRaises(ValueError):
            recursion.recursive(-4, 'abc', 'hfiueghwh')
    

def main():
    unittest.main()


if __name__ == "__main__":
    main()
