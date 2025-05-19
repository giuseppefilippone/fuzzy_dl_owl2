import unittest

from parser_interface import ParserInterface


class TestReflexive(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/reflexive1.txt")
        self.assertEqual(0.8, p.solve(), "TestReflexive")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/reflexive2.txt")
        self.assertEqual(0.8, p.solve(), "TestReflexive")


if __name__ == "__main__":
    unittest.main()
