import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestSymmetric(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/symmetric1.txt")
        self.assertEqual(0.7, p.solve(), "TestSymmetric")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/symmetric2.txt")
        self.assertEqual(0.7, p.solve(), "TestSymmetric")


if __name__ == "__main__":
    unittest.main()
