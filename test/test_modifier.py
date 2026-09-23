import unittest

from parser_interface import ParserInterface


class TestModifier(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/modifier1.txt")
        self.assertEqual(0.5, p.solve(), "TestModifier")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/modifier2.txt")
        self.assertEqual(0.9, p.solve(), "TestModifier")

    # Regression tests for the modifier-over-complex-concept bug:
    # (min-instance? a (mod D)) collapsed to 0 whenever D was a
    # some/all restriction (abstract role or concrete feature).

    def test_query3(self):
        # Baseline without modifier: HighX(30) = 0.25
        p = ParserInterface("../examples/TestSuite/modifier3.txt")
        self.assertEqual(0.25, p.solve(), "TestModifier")

    def test_query4(self):
        # Modifier over a concrete restriction: very(0.25) = 0.125
        p = ParserInterface("../examples/TestSuite/modifier4.txt")
        self.assertEqual(0.125, p.solve(), "TestModifier")

    def test_query5(self):
        # max-instance? on the same concept must agree with min-instance?
        p = ParserInterface("../examples/TestSuite/modifier5.txt")
        self.assertEqual(0.125, p.solve(), "TestModifier")

    def test_query6(self):
        # Same as test_query4, via a defined concept D = (some f HighX)
        p = ParserInterface("../examples/TestSuite/modifier6.txt")
        self.assertEqual(0.125, p.solve(), "TestModifier")

    def test_query7(self):
        # Baseline without modifier: (some R C) with C(b) = 0.9
        p = ParserInterface("../examples/TestSuite/modifier7.txt")
        self.assertEqual(0.9, p.solve(), "TestModifier")

    def test_query8(self):
        # Modifier over an abstract role restriction: very(0.9) = 0.8
        p = ParserInterface("../examples/TestSuite/modifier8.txt")
        self.assertEqual(0.8, p.solve(), "TestModifier")

    def test_query9(self):
        # max-instance? is only an upper bound here: ABox degrees are lower
        # bounds, so C(b) may reach 1.0 and very(1.0) = 1.0. (Unlike
        # modifier5, where the functional feature pins the degree exactly.)
        p = ParserInterface("../examples/TestSuite/modifier9.txt")
        self.assertEqual(1.0, p.solve(), "TestModifier")

    def test_query10(self):
        # Unchanged case: modifier over an atomic concept
        p = ParserInterface("../examples/TestSuite/modifier10.txt")
        self.assertEqual(0.8, p.solve(), "TestModifier")

    def test_query11(self):
        # Unchanged case: modifier applied to the datatype itself
        p = ParserInterface("../examples/TestSuite/modifier11.txt")
        self.assertEqual(0.125, p.solve(), "TestModifier")

    def test_query12(self):
        # Unchanged case: modifier over a conjunction of atomic concepts
        p = ParserInterface("../examples/TestSuite/modifier12.txt")
        self.assertEqual(0.4, p.solve(), "TestModifier")


if __name__ == "__main__":
    unittest.main()
