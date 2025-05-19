import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestAggregation(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/aggregation1.txt")
        self.assertEqual(0.6, p.solve(), "TestOwa")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/aggregation2.txt")
        self.assertEqual(0.6, p.solve(), "TestQ-Owa")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/aggregation3.txt")
        self.assertEqual(0.4, p.solve(), "TestSugeno")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/aggregation4.txt")
        self.assertEqual(0.9, p.solve(), "TestQ-Sugeno")

    def test_query5(self):
        p = ParserInterface("examples/TestSuite/aggregation5.txt")
        self.assertEqual(0.5, p.solve(), "TestChoquet")

    def test_query6(self):
        p = ParserInterface("examples/TestSuite/aggregation6.txt")
        self.assertEqual(0.6, p.solve(), "TestWeightedMin")

    def test_query7(self):
        p = ParserInterface("examples/TestSuite/aggregation7.txt")
        self.assertEqual(0.6, p.solve(), "TestWeightedMax")


if __name__ == "__main__":
    unittest.main()
