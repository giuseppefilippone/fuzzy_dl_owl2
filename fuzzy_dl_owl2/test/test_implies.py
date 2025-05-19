import unittest

from fuzzy_dl_owl2.test.parser_interface import ParserInterface


class TestImplies(unittest.TestCase):

    def test_query_g1(self):
        p = ParserInterface("examples/TestSuite/impliesG1.txt")
        self.assertEqual(0.4, p.solve(), "TestImplies")

    def test_query_g2(self):
        p = ParserInterface("examples/TestSuite/impliesG2.txt")
        self.assertEqual(0.8, p.solve(), "TestImplies")

    def test_query_kd1(self):
        p = ParserInterface("examples/TestSuite/impliesKd1.txt")
        self.assertEqual(0.9, p.solve(), "TestImplies")

    def test_query_kd2(self):
        p = ParserInterface("examples/TestSuite/impliesKd2.txt")
        self.assertEqual(0.9, p.solve(), "TestImplies")

    def test_query_l1(self):
        p = ParserInterface("examples/TestSuite/impliesL1.txt")
        self.assertEqual(0.5, p.solve(), "TestImplies")

    def test_query_l2(self):
        p = ParserInterface("examples/TestSuite/impliesL2.txt")
        self.assertEqual(0.7, p.solve(), "TestImplies")

    def test_query_l3(self):
        p = ParserInterface("examples/TestSuite/impliesL3.txt")
        self.assertEqual(0.7, p.solve(), "TestImplies")

    def test_query_z(self):
        p = ParserInterface("examples/TestSuite/impliesZ.txt")
        self.assertEqual(0.8, p.solve(), "TestImplies")


if __name__ == "__main__":
    unittest.main()
