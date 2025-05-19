import unittest

from parser_interface import ParserInterface


class TestNot(unittest.TestCase):

    def test_query(self):
        p = ParserInterface("../examples/TestSuite/not.txt")
        self.assertEqual(1.0, p.solve(), "TestNot")


if __name__ == "__main__":
    unittest.main()
