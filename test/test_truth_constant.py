import unittest

from parser_interface import ParserInterface


class TestTruthConstant(unittest.TestCase):

    def test_query(self):
        p = ParserInterface("../examples/TestSuite/truthconstant.txt")
        self.assertEqual(0.2, p.solve(), "TestTruthConstant")


if __name__ == "__main__":
    unittest.main()
