import unittest

from parser_interface import ParserInterface


class TestAbsorption(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/absorption1.txt")
        self.assertEqual(0.7, p.solve(), "TestAbsorption")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/absorption2.txt")
        self.assertEqual(0.7, p.solve(), "TestAbsorption")

    def test_query3(self):
        p = ParserInterface("../examples/TestSuite/absorption3.txt")
        self.assertEqual(0.7, p.solve(), "TestAbsorption")

    def test_query4(self):
        p = ParserInterface("../examples/TestSuite/absorption4.txt")
        self.assertEqual(0.5, p.solve(), "TestAbsorption")

    def test_query5(self):
        p = ParserInterface("../examples/TestSuite/absorption5.txt")
        self.assertEqual(0.5, p.solve(), "TestAbsorption")


if __name__ == "__main__":
    unittest.main()
