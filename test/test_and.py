import unittest

from parser_interface import ParserInterface


class TestAnd(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/and1.txt")
        self.assertEqual(0.7, p.solve(), "TestAnd")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/and2.txt")
        self.assertEqual(0.1, p.solve(), "TestAnd")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/and3.txt")
        self.assertEqual(0.7, p.solve(), "TestAnd")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/and4.txt")
        self.assertEqual(0.4, p.solve(), "TestAnd")


if __name__ == "__main__":
    unittest.main()
