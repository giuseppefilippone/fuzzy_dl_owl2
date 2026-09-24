import unittest

from fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept import (
    CrispConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept import (
    LeftConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept import (
    LinearConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept import (
    ModifiedConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept import (
    RightConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept import (
    TrapezoidalConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept import (
    TriangularConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.qowa_concept import QowaConcept
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier import TriangularModifier
from fuzzy_dl_owl2.fuzzydl.parser.dl_parser_clean import DLParser
from fuzzy_dl_owl2.fuzzydl.parser.dl_parser_fast import DLParserFast
from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.constants import FuzzyLogic

# Marker for table rows whose expected value is reached through non-dyadic
# arithmetic (the second segment of the linear modifier, see below); those
# rows are checked with assertAlmostEqual(places=12) instead of assertEqual.
APPROX = "~"


class TestModifiedConcept(unittest.TestCase):
    """ModifiedConcreteConcept.get_membership_degree on non-unit domains.

    Regression for the guard "if x <= 0.0 or x > 1.0: return 0.0" that used
    to open the method: it tested the FEATURE value x against the unit
    interval (the range of the degree y, not of x), so on any real domain,
    e.g. [0, 100], the composition was identically zero for every x outside
    (0, 1].  The Java oracle shares that defect; the Python fix is a
    deliberate divergence and the composition is now modifier(base(x)) with
    no guard on x at all.

    Modifiers used throughout (their own tables are in test_membership.py):

    * very = linear-modifier(2): a = 2/3, b = 1/3, so
        very(y) = y / 2         for 0 < y <= 2/3   (b/a is exactly 0.5)
        very(y) = 2 y - 1       for 2/3 < y < 1    (uses 1 - b, not dyadic)
      very(0) = 0, very(1) = 1.  Rows going through the second segment
      (base degree 0.75) are marked APPROX.
    * tm = triangular-modifier(0, 0.5, 1):
        tm(y) = 2 y             for 0 < y <= 0.5
        tm(y) = 2 (1 - y)       for 0.5 < y < 1
      tm(0) = tm(1) = 0 (closed zero boundaries), so the 1-plateau of every
      base maps to 0 while a base degree of 0.5 maps to 1.  All tm values
      used here are dyadic, hence exact.

    Every base lives on the domain [0, 100].  Probe values are exactly
    representable doubles and the base degrees at them are dyadic
    (0, 0.25, 0.5, 0.75, 1), so equality asserts are exact except where
    marked.  Each table covers: the two domain extremes, an interior point
    of every ramp, the plateau(s), and points outside the domain on both
    sides.  Outside the domain the composition follows the base concept
    (e.g. a left-shoulder is still 1 at x = -5), it is not forced to 0.
    """

    def setUp(self):
        self.very = LinearModifier("very", 2.0)
        self.tm = TriangularModifier("tm", 0.0, 0.5, 1.0)

    def check_table(self, f, table):
        for row in table:
            x, expected = row[0], row[1]
            got = f.get_membership_degree(x)
            msg = f"{f.compute_name()}({x})"
            if len(row) > 2 and row[2] == APPROX:
                self.assertAlmostEqual(got, expected, places=12, msg=msg)
            else:
                self.assertEqual(got, expected, msg=msg)

    def assert_not_identically_zero(self, f, xs):
        self.assertTrue(
            any(f.get_membership_degree(x) > 0.0 for x in xs),
            msg=f"{f.compute_name()} is identically zero on {xs}",
        )

    # ------------------------------------------------------------------
    # Modifier sanity: the degrees every table below feeds to the modifiers.
    # ------------------------------------------------------------------

    def test_modifier_values_used_by_the_tables(self):
        very, tm = self.very, self.tm
        self.assertEqual(very.get_membership_degree(0.0), 0.0)
        self.assertEqual(very.get_membership_degree(0.25), 0.125)
        self.assertEqual(very.get_membership_degree(0.5), 0.25)
        self.assertAlmostEqual(very.get_membership_degree(0.75), 0.5, places=12)
        self.assertEqual(very.get_membership_degree(1.0), 1.0)
        self.assertEqual(tm.get_membership_degree(0.0), 0.0)
        self.assertEqual(tm.get_membership_degree(0.25), 0.5)
        self.assertEqual(tm.get_membership_degree(0.5), 1.0)
        self.assertEqual(tm.get_membership_degree(0.75), 0.5)
        self.assertEqual(tm.get_membership_degree(1.0), 0.0)

    # ------------------------------------------------------------------
    # left-shoulder(0, 100, 20, 40): 1 on [0, 20], (40-x)/20, 0 on [40, 100]
    # ------------------------------------------------------------------

    def left(self):
        return LeftConcreteConcept("L", 0.0, 100.0, 20.0, 40.0)

    def test_left_shoulder_very(self):
        f = ModifiedConcreteConcept("veryL", self.very, self.left())
        self.check_table(
            f,
            [
                (0.0, 1.0),  # domain extreme, 1-plateau: very(1)
                (10.0, 1.0),  # 1-plateau
                (20.0, 1.0),  # x = a (closed one boundary)
                (25.0, 0.5, APPROX),  # ramp: base 0.75 -> very(0.75)
                (30.0, 0.25),  # ramp midpoint: base 0.5 -> very(0.5)
                (35.0, 0.125),  # ramp: base 0.25 -> very(0.25)
                (40.0, 0.0),  # x = b (closed zero boundary)
                (70.0, 0.0),  # 0-plateau
                (100.0, 0.0),  # domain extreme
                (-5.0, 1.0),  # below the domain: base is 1 there
                (150.0, 0.0),  # above the domain
            ],
        )
        self.assert_not_identically_zero(f, [0.0, 10.0, 30.0])

    def test_left_shoulder_triangular(self):
        f = ModifiedConcreteConcept("tmL", self.tm, self.left())
        self.check_table(
            f,
            [
                (0.0, 0.0),  # 1-plateau: tm(1) = 0
                (10.0, 0.0),
                (20.0, 0.0),
                (25.0, 0.5),  # base 0.75 -> tm(0.75)
                (30.0, 1.0),  # base 0.5 -> tm(0.5), the peak
                (35.0, 0.5),  # base 0.25 -> tm(0.25)
                (40.0, 0.0),
                (70.0, 0.0),
                (100.0, 0.0),
                (-5.0, 0.0),  # base is 1 there, tm(1) = 0
                (150.0, 0.0),
            ],
        )
        self.assert_not_identically_zero(f, [25.0, 30.0, 35.0])

    # ------------------------------------------------------------------
    # right-shoulder(0, 100, 20, 40): 0 on [0, 20], (x-20)/20, 1 on [40, 100]
    # ------------------------------------------------------------------

    def right(self):
        return RightConcreteConcept("R", 0.0, 100.0, 20.0, 40.0)

    def test_right_shoulder_very(self):
        f = ModifiedConcreteConcept("veryR", self.very, self.right())
        self.check_table(
            f,
            [
                (0.0, 0.0),  # domain extreme, 0-plateau
                (10.0, 0.0),  # 0-plateau
                (20.0, 0.0),  # x = a (closed zero boundary)
                (25.0, 0.125),  # ramp: base 0.25
                (30.0, 0.25),  # ramp midpoint: base 0.5
                (35.0, 0.5, APPROX),  # ramp: base 0.75
                (40.0, 1.0),  # x = b (closed one boundary)
                (70.0, 1.0),  # 1-plateau
                (100.0, 1.0),  # domain extreme
                (-5.0, 0.0),  # below the domain
                (150.0, 1.0),  # above the domain: base is 1 there
            ],
        )
        self.assert_not_identically_zero(f, [30.0, 70.0, 100.0])

    def test_right_shoulder_triangular(self):
        f = ModifiedConcreteConcept("tmR", self.tm, self.right())
        self.check_table(
            f,
            [
                (0.0, 0.0),
                (10.0, 0.0),
                (20.0, 0.0),
                (25.0, 0.5),  # base 0.25
                (30.0, 1.0),  # base 0.5, the peak
                (35.0, 0.5),  # base 0.75
                (40.0, 0.0),  # 1-plateau: tm(1) = 0
                (70.0, 0.0),
                (100.0, 0.0),
                (-5.0, 0.0),
                (150.0, 0.0),  # base is 1 there, tm(1) = 0
            ],
        )
        self.assert_not_identically_zero(f, [25.0, 30.0, 35.0])

    # ------------------------------------------------------------------
    # triangular(0, 100, 10, 20, 40): (x-10)/10 on (10, 20), (40-x)/20 on (20, 40)
    # ------------------------------------------------------------------

    def triangular(self):
        return TriangularConcreteConcept("Tri", 0.0, 100.0, 10.0, 20.0, 40.0)

    def test_triangular_very(self):
        f = ModifiedConcreteConcept("veryTri", self.very, self.triangular())
        self.check_table(
            f,
            [
                (0.0, 0.0),  # domain extreme
                (5.0, 0.0),  # below the support
                (10.0, 0.0),  # x = a (closed zero boundary)
                (12.5, 0.125),  # ascending side: base 0.25
                (15.0, 0.25),  # ascending side midpoint: base 0.5
                (17.5, 0.5, APPROX),  # ascending side: base 0.75
                (20.0, 1.0),  # x = b, the peak
                (25.0, 0.5, APPROX),  # descending side: base 0.75
                (30.0, 0.25),  # descending side midpoint: base 0.5
                (35.0, 0.125),  # descending side: base 0.25
                (40.0, 0.0),  # x = c (closed zero boundary)
                (70.0, 0.0),  # above the support
                (100.0, 0.0),  # domain extreme
                (-5.0, 0.0),  # below the domain
                (150.0, 0.0),  # above the domain
            ],
        )
        self.assert_not_identically_zero(f, [15.0, 20.0, 30.0])

    def test_triangular_triangular(self):
        f = ModifiedConcreteConcept("tmTri", self.tm, self.triangular())
        self.check_table(
            f,
            [
                (0.0, 0.0),
                (5.0, 0.0),
                (10.0, 0.0),
                (12.5, 0.5),  # base 0.25
                (15.0, 1.0),  # base 0.5, the peak
                (17.5, 0.5),  # base 0.75
                (20.0, 0.0),  # peak of the base: tm(1) = 0
                (25.0, 0.5),  # base 0.75
                (30.0, 1.0),  # base 0.5, the peak
                (35.0, 0.5),  # base 0.25
                (40.0, 0.0),
                (70.0, 0.0),
                (100.0, 0.0),
                (-5.0, 0.0),
                (150.0, 0.0),
            ],
        )
        self.assert_not_identically_zero(f, [12.5, 15.0, 30.0])

    # ------------------------------------------------------------------
    # trapezoidal(0, 100, 2, 10, 20, 30): (x-2)/8 on (2, 10), 1 on [10, 20],
    # (30-x)/10 on (20, 30)
    # ------------------------------------------------------------------

    def trapezoidal(self):
        return TrapezoidalConcreteConcept("T", 0.0, 100.0, 2.0, 10.0, 20.0, 30.0)

    def test_trapezoidal_very_maintainer_table(self):
        # The three values the fix was specified against: the composition on
        # [0, 100] is NOT identically zero.
        f = ModifiedConcreteConcept("veryT", self.very, self.trapezoidal())
        self.assertEqual(f.get_membership_degree(6.0), 0.25)  # very(0.5)
        self.assertEqual(f.get_membership_degree(15.0), 1.0)  # very(1)
        self.assertEqual(f.get_membership_degree(25.0), 0.25)  # very(0.5)

    def test_trapezoidal_very(self):
        f = ModifiedConcreteConcept("veryT", self.very, self.trapezoidal())
        self.check_table(
            f,
            [
                (0.0, 0.0),  # domain extreme
                (1.0, 0.0),  # below the support
                (2.0, 0.0),  # x = a (closed zero boundary)
                (4.0, 0.125),  # ascending side: base 0.25
                (6.0, 0.25),  # ascending side midpoint: base 0.5
                (8.0, 0.5, APPROX),  # ascending side: base 0.75
                (10.0, 1.0),  # x = b (core boundary)
                (15.0, 1.0),  # core plateau
                (20.0, 1.0),  # x = c (core boundary)
                (22.5, 0.5, APPROX),  # descending side: base 0.75
                (25.0, 0.25),  # descending side midpoint: base 0.5
                (27.5, 0.125),  # descending side: base 0.25
                (30.0, 0.0),  # x = d (closed zero boundary)
                (65.0, 0.0),  # above the support
                (100.0, 0.0),  # domain extreme
                (-5.0, 0.0),  # below the domain
                (150.0, 0.0),  # above the domain
            ],
        )
        self.assert_not_identically_zero(f, [6.0, 15.0, 25.0])

    def test_trapezoidal_triangular(self):
        f = ModifiedConcreteConcept("tmT", self.tm, self.trapezoidal())
        self.check_table(
            f,
            [
                (0.0, 0.0),
                (1.0, 0.0),
                (2.0, 0.0),
                (4.0, 0.5),  # base 0.25
                (6.0, 1.0),  # base 0.5, the peak
                (8.0, 0.5),  # base 0.75
                (10.0, 0.0),  # core: tm(1) = 0
                (15.0, 0.0),
                (20.0, 0.0),
                (22.5, 0.5),  # base 0.75
                (25.0, 1.0),  # base 0.5, the peak
                (27.5, 0.5),  # base 0.25
                (30.0, 0.0),
                (65.0, 0.0),
                (100.0, 0.0),
                (-5.0, 0.0),
                (150.0, 0.0),
            ],
        )
        self.assert_not_identically_zero(f, [4.0, 6.0, 25.0])

    # ------------------------------------------------------------------
    # crisp(0, 100, 20, 40): characteristic function of the closed [20, 40]
    # ------------------------------------------------------------------

    def crisp(self):
        return CrispConcreteConcept("C", 0.0, 100.0, 20.0, 40.0)

    def test_crisp_very(self):
        f = ModifiedConcreteConcept("veryC", self.very, self.crisp())
        self.check_table(
            f,
            [
                (0.0, 0.0),  # domain extreme
                (19.5, 0.0),  # just below a
                (20.0, 1.0),  # x = a (closed): very(1)
                (30.0, 1.0),  # interior of the interval
                (40.0, 1.0),  # x = b (closed)
                (40.5, 0.0),  # just above b
                (100.0, 0.0),  # domain extreme
                (-5.0, 0.0),  # below the domain
                (150.0, 0.0),  # above the domain
            ],
        )
        self.assert_not_identically_zero(f, [20.0, 30.0, 40.0])

    def test_crisp_triangular(self):
        # A crisp base only produces the degrees 0 and 1, and tm maps both to
        # 0 (closed zero boundaries of the triangle), so this particular
        # composition IS identically zero, by the arithmetic and not because
        # of any guard on x.
        f = ModifiedConcreteConcept("tmC", self.tm, self.crisp())
        self.check_table(
            f,
            [
                (0.0, 0.0),
                (19.5, 0.0),
                (20.0, 0.0),
                (30.0, 0.0),
                (40.0, 0.0),
                (40.5, 0.0),
                (100.0, 0.0),
                (-5.0, 0.0),
                (150.0, 0.0),
            ],
        )

    # ------------------------------------------------------------------
    # The composition is literally modifier(base(x)), with no guard on x.
    # ------------------------------------------------------------------

    def test_equals_direct_composition_everywhere(self):
        bases = [
            self.left(),
            self.right(),
            self.triangular(),
            self.trapezoidal(),
            self.crisp(),
        ]
        # Half-integer sweep well beyond the domain on both sides.
        xs = [-20.0 + 0.5 * i for i in range(0, 281)]  # -20 .. 120
        for base in bases:
            for mod in (self.very, self.tm):
                f = ModifiedConcreteConcept("m", mod, base)
                for x in xs:
                    self.assertEqual(
                        f.get_membership_degree(x),
                        mod.get_membership_degree(base.get_membership_degree(x)),
                        msg=f"{f.compute_name()}({x})",
                    )

    # ------------------------------------------------------------------
    # q-owa quantifier: must be a right-shoulder or a linear function
    # (Java parity; the port used to accept a left-shoulder instead).
    # ------------------------------------------------------------------

    QOWA_PREAMBLE = "(define-modifier very linear-modifier(2))\n"
    QOWA_USE = "(instance a (q-owa Q A B) 0.8)\n"

    @staticmethod
    def parse(text):
        # Mirror DLParserFast.get_kb: a fresh KB starts with the global
        # semantics unset, and get_kb defaults it to Lukasiewicz before
        # parsing (a KB may still override it with define-fuzzy-logic).
        DLParser.kb = KnowledgeBase()
        DLParser.queries_list = []
        constants.KNOWLEDGE_BASE_SEMANTICS = FuzzyLogic.LUKASIEWICZ
        DLParserFast.parse_string(text)
        return DLParser.kb

    def test_qowa_rejects_modified_quantifier(self):
        kb_text = (
            self.QOWA_PREAMBLE
            + "(define-fuzzy-concept R right-shoulder(0, 1, 0.25, 0.75))\n"
            + "(define-fuzzy-concept Q modified(very, R))\n"
            + self.QOWA_USE
        )
        with self.assertRaises(FuzzyOntologyException) as cm:
            self.parse(kb_text)
        self.assertIn("right or a linear", str(cm.exception))

    def test_qowa_rejects_left_shoulder_quantifier(self):
        kb_text = (
            self.QOWA_PREAMBLE
            + "(define-fuzzy-concept Q left-shoulder(0, 1, 0.25, 0.75))\n"
            + self.QOWA_USE
        )
        with self.assertRaises(FuzzyOntologyException) as cm:
            self.parse(kb_text)
        self.assertIn("right or a linear", str(cm.exception))

    def test_qowa_accepts_linear_quantifier(self):
        kb_text = (
            self.QOWA_PREAMBLE
            + "(define-fuzzy-concept Q linear(0.0, 1.0, 0.5, 0.4))\n"
            + self.QOWA_USE
        )
        kb = self.parse(kb_text)
        self.assertIsInstance(kb.concrete_concepts.get("Q"), LinearConcreteConcept)

    def test_qowa_accepts_right_shoulder_quantifier(self):
        # Positive control, same shape as examples/TestSuite/aggregation2.txt.
        kb_text = (
            self.QOWA_PREAMBLE
            + "(define-fuzzy-concept Q right-shoulder(0, 1, 0.25, 0.75))\n"
            + self.QOWA_USE
        )
        kb = self.parse(kb_text)
        self.assertIsInstance(kb.concrete_concepts.get("Q"), RightConcreteConcept)

    def test_qowa_parses_to_qowa_concept(self):
        kb_text = (
            self.QOWA_PREAMBLE
            + "(define-fuzzy-concept Q linear(0.0, 1.0, 0.5, 0.4))\n"
            + "(define-concept D (q-owa Q A B))\n"
        )
        kb = self.parse(kb_text)
        self.assertIsInstance(kb.concrete_concepts.get("Q"), LinearConcreteConcept)
        # A define-concept with a complex right-hand side lands in the
        # equivalence axioms, not in the lazy-unfolding definitions.
        axioms = [c for cs in kb.axioms_A_equiv_C.values() for c in cs]
        self.assertTrue(
            any(isinstance(c, QowaConcept) for c in axioms),
            msg="no QowaConcept found among the TBox equivalence axioms",
        )


if __name__ == "__main__":
    unittest.main()
