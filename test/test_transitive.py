import unittest

from parser_interface import ParserInterface


class TestTransitive(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/transitive1.txt")
        self.assertEqual(0.2, p.solve(), "TestTransitive")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/transitive2.txt")
        self.assertEqual(0.5, p.solve(), "TestTransitive")

    def test_query3(self):
        p = ParserInterface("../examples/TestSuite/transitive3.txt")
        self.assertEqual(0.9, p.solve(), "TestTransitive")

    def test_query4(self):
        p = ParserInterface("../examples/TestSuite/transitive4.txt")
        self.assertEqual(0.9, p.solve(), "TestTransitive")


if __name__ == "__main__":
    unittest.main()
