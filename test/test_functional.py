import unittest

from parser_interface import ParserInterface


class TestFunctional(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("./examples/TestSuite/functional1.txt")
        self.assertEqual(0.6, p.solve(), "TestFunctional")

    def test_query2(self):
        p = ParserInterface("./examples/TestSuite/functional2.txt")
        self.assertEqual(1.0, p.solve(), "TestFunctional")

    def test_query3(self):
        p = ParserInterface("./examples/TestSuite/functional3.txt")
        self.assertEqual(-1.0, p.solve(), "TestFunctional")

    def test_query4(self):
        p = ParserInterface("./examples/TestSuite/functional4.txt")
        self.assertEqual(1.0, p.solve(), "TestFunctional")


if __name__ == "__main__":
    unittest.main()
