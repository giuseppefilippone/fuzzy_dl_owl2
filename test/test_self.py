import unittest

from parser_interface import ParserInterface


class TestSelf(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("./examples/TestSuite/self1.txt")
        self.assertEqual(0.8, p.solve(), "TestSelf")

    def test_query2(self):
        p = ParserInterface("./examples/TestSuite/self2.txt")
        self.assertEqual(0.8, p.solve(), "TestSelf")


if __name__ == "__main__":
    unittest.main()
