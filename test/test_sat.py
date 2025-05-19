import unittest

from parser_interface import ParserInterface


class TestSat(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("./examples/TestSuite/sat1.txt")
        self.assertEqual(0.0, p.solve(), "TestSat")

    def test_query2(self):
        p = ParserInterface("./examples/TestSuite/sat2.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query3(self):
        p = ParserInterface("./examples/TestSuite/sat3.txt")
        self.assertEqual(0.5, p.solve(), "TestSat")

    def test_query4(self):
        p = ParserInterface("./examples/TestSuite/sat4.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query5(self):
        p = ParserInterface("./examples/TestSuite/sat5.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query6(self):
        p = ParserInterface("./examples/TestSuite/sat6.txt")
        self.assertEqual(-1.0, p.solve(), "TestSat")

    def test_query7(self):
        p = ParserInterface("./examples/TestSuite/sat7.txt")
        self.assertEqual(0.5, p.solve(), "TestSat")


if __name__ == "__main__":
    unittest.main()
