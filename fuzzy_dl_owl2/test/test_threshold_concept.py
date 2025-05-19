import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestThresholdConcept(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/thresholdConcept1.txt")
        self.assertEqual(0.2, p.solve(), "TestThresholdConcept")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/thresholdConcept2.txt")
        self.assertEqual(0.4, p.solve(), "TestThresholdConcept")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/thresholdConcept3.txt")
        self.assertEqual(0.3, p.solve(), "TestThresholdConcept")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/thresholdConcept4.txt")
        self.assertEqual(0.3, p.solve(), "TestThresholdConcept")


if __name__ == "__main__":
    unittest.main()
