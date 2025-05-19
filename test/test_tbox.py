import unittest

from parser_interface import ParserInterface


class TestTbox(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/domain.txt")
        self.assertEqual(0.8, p.solve(), "TestTbox")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/range.txt")
        self.assertEqual(0.8, p.solve(), "TestTbox")

    def test_query3(self):
        p = ParserInterface("../examples/TestSuite/disjoint1.txt")
        self.assertEqual(1.0, p.solve(), "TestTbox")

    def test_query4(self):
        p = ParserInterface("../examples/TestSuite/lazy.txt")
        self.assertEqual(0.8, p.solve(), "TestTbox")


if __name__ == "__main__":
    unittest.main()
