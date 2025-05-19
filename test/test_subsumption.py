import unittest

from parser_interface import ParserInterface


class TestSubsumption(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/subsumption1.txt")
        self.assertEqual(0.5, p.solve(), "TestSubsumption")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/subsumption2.txt")
        self.assertEqual(0.0, p.solve(), "TestSubsumption")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/subsumption3.txt")
        self.assertEqual(0.3, p.solve(), "TestSubsumption")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/subsumption4.txt")
        self.assertEqual(1.0, p.solve(), "TestSubsumption")


if __name__ == "__main__":
    unittest.main()
