import unittest

from parser_interface import ParserInterface


class TestFuzzyNumber(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/fuzzyNumber1.txt")
        self.assertEqual(7.5, p.solve(), "TestFuzzyNumber")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/fuzzyNumber2.txt")
        self.assertEqual(-1.8333, p.solve(), "TestFuzzyNumber")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/fuzzyNumber3.txt")
        self.assertEqual(2.5, p.solve(), "TestFuzzyNumber")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/fuzzyNumber4.txt")
        self.assertEqual(11.0, p.solve(), "TestFuzzyNumber")

    def test_query5(self):
        p = ParserInterface("examples/TestSuite/fuzzyNumber5.txt")
        self.assertEqual(2.0, p.solve(), "TestFuzzyNumber")


if __name__ == "__main__":
    unittest.main()
