import unittest

from parser_interface import ParserInterface


class TestWeightedSum(unittest.TestCase):

    def test_query_1(self):
        p = ParserInterface("../examples/TestSuite/weightedSum.txt")
        self.assertEqual(0.8, p.solve(), "TestWeightedSum")

    # w-sum-zero: min-instance? goes through the complemented encoding.

    def test_query_2(self):
        # C pinned at 0.05, B = 1: 0.8 * 0.05 + 0.2 * 1
        p = ParserInterface("../examples/TestSuite/weightedSumZero1.txt")
        self.assertEqual(0.24, p.solve(), "TestWeightedSumZero")

    def test_query_3(self):
        # a component at 0 zeroes the whole sum
        p = ParserInterface("../examples/TestSuite/weightedSumZero2.txt")
        self.assertEqual(0.0, p.solve(), "TestWeightedSumZero")

    def test_query_4(self):
        # both components positive: 0.6 * 1 + 0.4 * 0.5
        p = ParserInterface("../examples/TestSuite/weightedSumZero3.txt")
        self.assertEqual(0.8, p.solve(), "TestWeightedSumZero")

    def test_query_5(self):
        p = ParserInterface("../examples/TestSuite/weightedSumZero4.txt")
        self.assertEqual(1.0, p.solve(), "TestWeightedSumZero")

    def test_query_6(self):
        # missing component B: it may be 0, so the minimum is 0
        p = ParserInterface("../examples/TestSuite/weightedSumZero5.txt")
        self.assertEqual(0.0, p.solve(), "TestWeightedSumZero")

    def test_query_7(self):
        # missing component B: it may be 1, so the maximum is 0.6 + 0.4
        p = ParserInterface("../examples/TestSuite/weightedSumZero6.txt")
        self.assertEqual(1.0, p.solve(), "TestWeightedSumZero")

    def test_query_8(self):
        # component B forced to 0 via (not B) >= 1
        p = ParserInterface("../examples/TestSuite/weightedSumZero7.txt")
        self.assertEqual(0.0, p.solve(), "TestWeightedSumZero")

    def test_query_9(self):
        p = ParserInterface("../examples/TestSuite/weightedSumZero8.txt")
        self.assertEqual(0.0, p.solve(), "TestWeightedSumZero")


if __name__ == "__main__":
    unittest.main()
