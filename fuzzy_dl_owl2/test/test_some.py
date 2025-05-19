import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestSome(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/some1.txt")
        self.assertEqual(0.8, p.solve(), "TestSome")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/some2.txt")
        self.assertEqual(0.8, p.solve(), "TestSome")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/some3.txt")
        self.assertEqual(0.6, p.solve(), "TestSome")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/some4.txt")
        self.assertEqual(0.8, p.solve(), "TestSome")


if __name__ == "__main__":
    unittest.main()
