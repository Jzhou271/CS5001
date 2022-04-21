"""
CS5001
Jing Zhou
Homework 7
    Connect Four -- Testcases
    Imports from connect_four.py, and tests the ConnectFour class by creating
    objects, calling methods on those objects, and make sure the values of the
    attributesare what we expect.
"""
from connect_four import ConnectFour
import unittest


class ConnectFourTests(unittest.TestCase):
    """
    This is the unit test class, and it tests all the methods in
    ConnectFour class
    """
    def test_init(self):
        """
        This test is to check if the constructor works correctly
        """
        expected_board = [[" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          [" ", " ", " ", " ", " ", " ", " "],
                          ]
        testcase = ConnectFour()
        self.assertEqual(testcase.board, expected_board)
        self.assertEqual(testcase.turns, 0)
        self.assertEqual(testcase.operation_stack, [])
        self.assertEqual(testcase.winner, ' ')
        self.assertEqual(testcase.finished, False)

    def test_str(self):
        """
        This test is to check if __str__() works correctly
        """
        testcase = ConnectFour()
        actual = testcase.__str__()
        expected = "| | | | | | | |\n"\
                   "---------------\n"\
                   "| | | | | | | |\n"\
                   "---------------\n"\
                   "| | | | | | | |\n"\
                   "---------------\n"\
                   "| | | | | | | |\n"\
                   "---------------\n"\
                   "| | | | | | | |\n"\
                   "---------------\n"\
                   "| | | | | | | |\n"\
                   "---------------\n"\

        self.assertEqual(actual, expected)

    def test_whose_turn(self):
        """
        This tests whose_turn(), and expected return a "X" as initial game's
        turn
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.whose_turn()
        expected = "X"
        self.assertEqual(actual, expected)

    def test_add_piece(self):
        """
        This tests add_piece() with integer number, and always expecting a
        None answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.add_piece(1)
        expected = None
        self.assertEqual(actual, expected)

    def test_undo(self):
        """
        This tests undo() with updated by add_piece(), and expecting a list
        works correctly
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.add_piece(1)
        actual = testcase.add_piece(2)
        actual = testcase.undo()
        expected = [[" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " ", " ", " "],
                    [" ", "X", " ", " ", " ", " ", " "],
                    ]
        self.assertEqual(actual, expected)

    def test_check_index(self):
        """
        This tests check_index(), and always expecting a True answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.check_index(3, 4)
        expected = True
        self.assertEqual(actual, expected)

    def test_check_pos(self):
        """
        This tests check_pos(), and always expecting a None answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.check_pos(4, 5)
        expected = None
        self.assertEqual(actual, expected)

    def test_is_full(self):
        """
        This tests is_full(), and always expecting a False answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.is_full()
        expected = False
        self.assertEqual(actual, expected)

    def test_is_win(self):
        """
        This tests is_win(), and always expecting a False answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.is_win()
        expected = False
        self.assertEqual(actual, expected)

    def test_get_winner(self):
        """
        This tests get_winner(), and always expecting a None answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.get_winner()
        expected = None
        self.assertEqual(actual, expected)

    def test_is_game_over(self):
        """
        This tests is_game_over(), and always expecting a False answer
        :return: none
        """
        testcase = ConnectFour()
        actual = testcase.is_game_over()
        expected = False
        self.assertEqual(actual, expected)


def main():
    unittest.main()


if __name__ == "__main__":
    main()
