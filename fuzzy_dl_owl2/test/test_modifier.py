import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestModifier(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/modifier1.txt")
        self.assertEqual(0.5, p.solve(), "TestModifier")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/modifier2.txt")
        self.assertEqual(0.9, p.solve(), "TestModifier")


if __name__ == "__main__":
    unittest.main()
