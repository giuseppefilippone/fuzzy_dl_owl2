import unittest

from parser_interface import ParserInterface


class TestInconsistency(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("./examples/TestSuite/inconsistent1.txt")
        self.assertEqual(-1.0, p.solve(), "TestInconsistency")

    def test_query2(self):
        p = ParserInterface("./examples/TestSuite/inconsistent2.txt")
        self.assertEqual(-1.0, p.solve(), "TestInconsistency")

    def test_query3(self):
        p = ParserInterface("./examples/TestSuite/inconsistent3.txt")
        self.assertEqual(-1.0, p.solve(), "TestInconsistency")

    def test_query4(self):
        p = ParserInterface("./examples/TestSuite/inconsistent4.txt")
        self.assertEqual(-1.0, p.solve(), "TestInconsistency")

    def test_query5(self):
        p = ParserInterface("./examples/TestSuite/inconsistent5.txt")
        self.assertEqual(-1.0, p.solve(), "TestInconsistency")

    def test_query6(self):
        p = ParserInterface("./examples/TestSuite/inconsistent6.txt")
        self.assertEqual(-1.0, p.solve(), "TestInconsistency")


if __name__ == "__main__":
    unittest.main()
