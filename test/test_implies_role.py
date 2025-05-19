import unittest

from parser_interface import ParserInterface


class TestImpliesRole(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/impliesRole1.txt")
        self.assertEqual(0.6, p.solve(), "TestImpliesRole")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/impliesRole2.txt")
        self.assertEqual(0.7, p.solve(), "TestImpliesRole")


if __name__ == "__main__":
    unittest.main()
