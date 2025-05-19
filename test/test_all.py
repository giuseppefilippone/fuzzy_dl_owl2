import unittest

from parser_interface import ParserInterface


class TestAll(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/all1.txt")
        self.assertEqual(1.0, p.solve(), "TestAll")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/all2.txt")
        self.assertEqual(0.7, p.solve(), "TestAll")

    def test_query3(self):
        p = ParserInterface("../examples/TestSuite/all3.txt")
        self.assertEqual(1.0, p.solve(), "TestAll")

    def test_query4(self):
        p = ParserInterface("../examples/TestSuite/all4.txt")
        self.assertEqual(0.8, p.solve(), "TestAll")


if __name__ == "__main__":
    unittest.main()
