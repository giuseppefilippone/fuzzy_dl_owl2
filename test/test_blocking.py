import unittest

from parser_interface import ParserInterface


class TestBlocking(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/blockingLoop1.txt")
        self.assertEqual(0.8, p.solve(), "TestBlocking")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/blockingLoop2.txt")
        self.assertEqual(0.8, p.solve(), "TestBlocking")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/blockingLoop3.txt")
        self.assertEqual(0.8, p.solve(), "TestBlocking")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/blockingLoop4.txt")
        self.assertEqual(1.0, p.solve(), "TestBlocking")

    def test_query5(self):
        p = ParserInterface("examples/TestSuite/blockingLoop5.txt")
        self.assertEqual(0.0, p.solve(), "TestBlocking")

    def test_query6(self):
        p = ParserInterface("examples/TestSuite/blockingLoop6.txt")
        self.assertEqual(0.0, p.solve(), "TestBlocking")

    def test_query7(self):
        p = ParserInterface("examples/TestSuite/blockingDynamic1.txt")
        self.assertEqual(-1.0, p.solve(), "TestBlocking")

    def test_query8(self):
        p = ParserInterface("examples/TestSuite/blockingPairwise1.txt")
        self.assertEqual(0.0, p.solve(), "TestBlocking")

    def test_query9(self):
        p = ParserInterface("examples/TestSuite/blockingSet.txt")
        self.assertEqual(0.8, p.solve(), "TestBlocking")


if __name__ == "__main__":
    unittest.main()
