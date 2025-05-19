import unittest

from parser_interface import ParserInterface


class TestWeightedSum(unittest.TestCase):

    def test_query_1(self):
        p = ParserInterface("examples/TestSuite/weightedSum.txt")
        self.assertEqual(0.8, p.solve(), "TestWeightedSum")


if __name__ == "__main__":
    unittest.main()
