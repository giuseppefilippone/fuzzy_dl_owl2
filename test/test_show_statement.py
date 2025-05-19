import unittest

from parser_interface import ParserInterface


class TestShowStatement(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("./examples/TestSuite/showStatement1.txt")
        self.assertEqual(0.25, p.solve(), "TestShowStatement")

    def test_query2(self):
        p = ParserInterface("./examples/TestSuite/showStatement2.txt")
        self.assertEqual(1.0, p.solve(), "TestShowStatement")


if __name__ == "__main__":
    unittest.main()
