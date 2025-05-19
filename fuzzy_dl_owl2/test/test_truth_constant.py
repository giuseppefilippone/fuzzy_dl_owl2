import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestTruthConstant(unittest.TestCase):

    def test_query(self):
        p = ParserInterface("examples/TestSuite/truthconstant.txt")
        self.assertEqual(0.2, p.solve(), "TestTruthConstant")


if __name__ == "__main__":
    unittest.main()
