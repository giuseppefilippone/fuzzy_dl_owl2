import unittest

from parser_interface import ParserInterface

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query import MinSatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class TestSat(unittest.TestCase):

    def test_query1(self):
        p = ParserInterface("../examples/TestSuite/sat1.txt")
        self.assertEqual(0.0, p.solve(), "TestSat")

    def test_query2(self):
        p = ParserInterface("../examples/TestSuite/sat2.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query3(self):
        p = ParserInterface("../examples/TestSuite/sat3.txt")
        self.assertEqual(0.5, p.solve(), "TestSat")

    def test_query4(self):
        p = ParserInterface("../examples/TestSuite/sat4.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query5(self):
        p = ParserInterface("../examples/TestSuite/sat5.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query6(self):
        p = ParserInterface("../examples/TestSuite/sat6.txt")
        self.assertEqual(-1.0, p.solve(), "TestSat")

    def test_query7(self):
        p = ParserInterface("../examples/TestSuite/sat7.txt")
        self.assertEqual(0.5, p.solve(), "TestSat")

    # Regression tests for the one-argument (min-sat? C) bug: the virtual
    # re-dispatch in SatisfiableQuery bounced None into the subclass
    # constructor, whose two-argument branch rejected it.

    def test_query8(self):
        # (min-sat? Hot) -> a fresh individual is invented
        p = ParserInterface("../examples/TestSuite/sat10.txt")
        self.assertEqual(0.0, p.solve(), "TestSat")

    def test_query9(self):
        # (min-sat? Hot a)
        p = ParserInterface("../examples/TestSuite/sat11.txt")
        self.assertEqual(0.6, p.solve(), "TestSat")

    def test_query10(self):
        # (max-sat? Hot)
        p = ParserInterface("../examples/TestSuite/sat12.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query11(self):
        # (max-sat? Hot a)
        p = ParserInterface("../examples/TestSuite/sat13.txt")
        self.assertEqual(1.0, p.solve(), "TestSat")

    def test_query12_concrete_concept_rejected(self):
        # (min-sat? HighX a) must still fail: HighX is a concrete concept.
        p = ParserInterface("../examples/TestSuite/sat14.txt")
        with self.assertRaises(FuzzyOntologyException) as ctx:
            p.solve()
        self.assertIn("cannot be a concrete concept", str(ctx.exception))

    def test_construction_without_individual(self):
        # Pure construction sanity check (no solver needed): both the
        # one-argument form and the explicit None individual must build.
        c = Concept(ConceptType.ATOMIC, "Hot")
        q1 = MinSatisfiableQuery(c)
        self.assertIsNone(q1.ind)
        q2 = MinSatisfiableQuery(c, None)
        self.assertIsNone(q2.ind)


if __name__ == "__main__":
    unittest.main()
