import unittest

from parser_interface import ParserInterface


class TestWeightedConcept(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/weightedConcept1.txt")
        self.assertEqual(0.2857, p.solve(), "TestWeightedConcept")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/weightedConcept2.txt")
        self.assertEqual(0.4286, p.solve(), "TestWeightedConcept")


if __name__ == "__main__":
    unittest.main()
