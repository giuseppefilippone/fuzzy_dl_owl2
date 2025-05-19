import unittest

from parser_interface import ParserInterface


class TestRoughSets(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/roughSets1.txt")
        self.assertEqual(0.6, p.solve(), "TestRoughSets")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/roughSets2.txt")
        self.assertEqual(1.0, p.solve(), "TestRoughSets")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/roughSets3.txt")
        self.assertEqual(1.0, p.solve(), "TestRoughSets")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/roughSets4.txt")
        self.assertEqual(1.0, p.solve(), "TestRoughSets")

    def test_query5(self):
        p = ParserInterface("examples/TestSuite/roughSets5.txt")
        self.assertEqual(1.0, p.solve(), "TestRoughSets")


if __name__ == "__main__":
    unittest.main()
