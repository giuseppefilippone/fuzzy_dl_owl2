import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestInverse(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/inverseRole1.txt")
        self.assertEqual(0.5, p.solve(), "TestInverse")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/inverseRole2.txt")
        self.assertEqual(0.8, p.solve(), "TestInverse")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/inverseRole3.txt")
        self.assertEqual(-1.0, p.solve(), "TestInverse")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/inverseRole4.txt")
        self.assertEqual(0.7, p.solve(), "TestInverse")

    def test_query5(self):
        p = ParserInterface("examples/TestSuite/inverseRole5.txt")
        self.assertEqual(0.8, p.solve(), "TestInverse")

    def test_query6(self):
        p = ParserInterface("examples/TestSuite/inverseRole6.txt")
        self.assertEqual(-1.0, p.solve(), "TestInverse")


if __name__ == "__main__":
    unittest.main()
