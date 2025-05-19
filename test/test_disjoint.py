import unittest

from parser_interface import ParserInterface


class TestDisjoint(unittest.TestCase):

    def test_query_1(self):
        p = ParserInterface("./examples/TestSuite/disjoint1.txt")
        self.assertEqual(1.0, p.solve(), "TestDisjoint")

    def test_query_2(self):
        p = ParserInterface("./examples/TestSuite/disjoint2.txt")
        self.assertEqual(0, p.solve(), "TestDisjoint")


if __name__ == "__main__":
    unittest.main()
