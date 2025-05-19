import unittest

from parser_interface import ParserInterface


class TestInstance(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/instance1.txt")
        self.assertEqual(0.7, p.solve(), "TestInstance")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/instance2.txt")
        self.assertEqual(0.3, p.solve(), "TestInstance")


if __name__ == "__main__":
    unittest.main()
