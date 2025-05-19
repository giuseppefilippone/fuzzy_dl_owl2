import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestFuzzyConcreteDomain(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("examples/TestSuite/fcd1.txt")
        self.assertEqual(1.0, p.solve(), "TestFuzzyConcreteDomain")

    def test_query2(self):
        p = ParserInterface("examples/TestSuite/fcd2.txt")
        self.assertEqual(1.0, p.solve(), "TestFuzzyConcreteDomain")

    def test_query3(self):
        p = ParserInterface("examples/TestSuite/fcd3.txt")
        self.assertEqual(1.0, p.solve(), "TestFuzzyConcreteDomain")

    def test_query4(self):
        p = ParserInterface("examples/TestSuite/fcd4.txt")
        self.assertEqual(1.0, p.solve(), "TestFuzzyConcreteDomain")

    def test_query5(self):
        p = ParserInterface("examples/TestSuite/fcd5.txt")
        self.assertEqual(0.25, p.solve(), "TestFuzzyConcreteDomain")

    def test_query6(self):
        p = ParserInterface("examples/TestSuite/fcd6.txt")
        self.assertEqual(0.2647, p.solve(), "TestFuzzyConcreteDomain")


if __name__ == "__main__":
    unittest.main()
