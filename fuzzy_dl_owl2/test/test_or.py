import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestOr(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/or1.txt")
        self.assertEqual(0.0, p.solve(), "TestOr")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/or2.txt")
        self.assertEqual(1.0, p.solve(), "TestOr")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/or3.txt")
        self.assertEqual(0.0, p.solve(), "TestOr")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/or4.txt")
        self.assertEqual(1.0, p.solve(), "TestOr")


if __name__ == "__main__":
    unittest.main()
