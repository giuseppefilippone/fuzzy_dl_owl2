import unittest

from parser_interface import ParserInterface


class TestDatatype(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("./examples/TestSuite/datatype1.txt")
        self.assertEqual(1.0, p.solve(), "TestDatatype")

    def test_query2(self):
        p = ParserInterface("./examples/TestSuite/datatype2.txt")
        self.assertEqual(1.0, p.solve(), "TestDatatype")

    def test_query3(self):
        p = ParserInterface("./examples/TestSuite/datatype3.txt")
        self.assertEqual(1.0, p.solve(), "TestDatatype")

    def test_query4(self):
        p = ParserInterface("./examples/TestSuite/datatype4.txt")
        self.assertEqual(0.0, p.solve(), "TestDatatype")

    def test_query5(self):
        p = ParserInterface("./examples/TestSuite/datatype5.txt")
        self.assertEqual(1.0, p.solve(), "TestDatatype")

    def test_query6(self):
        p = ParserInterface("./examples/TestSuite/datatype6.txt")
        self.assertEqual(0.0, p.solve(), "TestDatatype")


if __name__ == "__main__":
    unittest.main()
