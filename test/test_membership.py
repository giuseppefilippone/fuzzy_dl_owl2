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
from fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier import TriangularModifier


class TestMembership(unittest.TestCase):
    """get_membership_degree of every concrete fuzzy set and modifier.

    Expected values come from the fuzzyDL membership-function formulas and
    were cross-checked against the Java oracle sources, with two exceptions:

    * TrapezoidalConcreteConcept, descending side (c, d): the Java oracle's
      third branch tests "x >= a", which is always true at that point, so it
      returns the ascending slope (x-a)/(b-a) > 1 instead of (d-x)/(d-c).
      The Python fix is a deliberate divergence; the tests here encode the
      correct (d-x)/(d-c) values.
    * LeftConcreteConcept: the Java oracle returns 0 for x <= a and 1 for
      x >= b around a DECREASING middle segment (b-x)/(b-a), which is
      internally inconsistent for a left-shoulder function. The Python port
      follows the standard formula (1 on [k1, a], decreasing on (a, b),
      0 on [b, k2]) and these tests encode that.

    Boundary conventions match the code (and Java): the zero plateaus are
    closed (<=/>=), so membership is 0 AT a and d for trapezoids, AT a and c
    for triangles, and 1 on the closed core [b, c].  All probe values are
    exactly representable doubles except where noted, so equality asserts
    are exact; assertAlmostEqual is used only where the implementation's
    slope arithmetic is not dyadic (e.g. linear-modifier with b/a = 1/3).
    """

    def check_table(self, f, table):
        for x, expected in table:
            self.assertEqual(
                f.get_membership_degree(x),
                expected,
                msg=f"{f.compute_name() if hasattr(f, 'compute_name') else f.name}({x})",
            )

    # ------------------------------------------------------------------
    # trapezoidal(k1, k2, a, b, c, d)
    # ------------------------------------------------------------------

    def test_trapezoidal(self):
        t = TrapezoidalConcreteConcept("T", 0.0, 100.0, 2.0, 10.0, 20.0, 30.0)
        self.check_table(
            t,
            [
                (1.0, 0.0),  # below the support
                (2.0, 0.0),  # x = a (closed zero boundary)
                (4.0, 0.25),  # ascending side: (4-2)/(10-2)
                (6.0, 0.5),  # ascending side midpoint
                (10.0, 1.0),  # x = b (core boundary)
                (15.0, 1.0),  # core plateau
                (20.0, 1.0),  # x = c (core boundary)
                (22.5, 0.75),  # descending side: (30-22.5)/(30-20)
                (25.0, 0.5),  # descending side midpoint
                (30.0, 0.0),  # x = d (closed zero boundary)
                (40.0, 0.0),  # above the support
            ],
        )

    def test_trapezoidal_descending_side_regression(self):
        # Regression for the v1.0.30 bug: the third branch tested "x >= a"
        # (always true there), so the descending side returned the ascending
        # slope (x-a)/(b-a) = 2.875 > 1 instead of (d-x)/(d-c) = 0.5.
        t = TrapezoidalConcreteConcept("T", 0.0, 100.0, 2.0, 10.0, 20.0, 30.0)
        self.assertEqual(t.get_membership_degree(25.0), 0.5)
        # ModerateFoodInsecurity example: buggy value was 4.495.
        mfi = TrapezoidalConcreteConcept("MFI", 0.0, 100.0, 5.0, 15.0, 35.0, 50.0)
        self.assertAlmostEqual(
            mfi.get_membership_degree(49.95), (50.0 - 49.95) / 15.0, places=12
        )
        self.assertLess(mfi.get_membership_degree(49.95), 1.0)

    # ------------------------------------------------------------------
    # triangular(k1, k2, a, b, c)
    # ------------------------------------------------------------------

    def test_triangular(self):
        t = TriangularConcreteConcept("Tri", 0.0, 100.0, 10.0, 20.0, 40.0)
        self.check_table(
            t,
            [
                (5.0, 0.0),  # below the support
                (10.0, 0.0),  # x = a (closed zero boundary)
                (12.5, 0.25),  # ascending side: (12.5-10)/(20-10)
                (15.0, 0.5),  # ascending side midpoint
                (20.0, 1.0),  # x = b (peak)
                (30.0, 0.5),  # descending side: (40-30)/(40-20)
                (35.0, 0.25),  # descending side
                (40.0, 0.0),  # x = c (closed zero boundary)
                (50.0, 0.0),  # above the support
            ],
        )

    # ------------------------------------------------------------------
    # left-shoulder(k1, k2, a, b): 1 on [k1, a], decreasing, 0 on [b, k2]
    # ------------------------------------------------------------------

    def test_left_shoulder(self):
        f = LeftConcreteConcept("L", 0.0, 100.0, 20.0, 40.0)
        self.check_table(
            f,
            [
                (0.0, 1.0),  # 1-plateau
                (10.0, 1.0),  # 1-plateau
                (20.0, 1.0),  # x = a (closed one boundary)
                (25.0, 0.75),  # descending side: (40-25)/(40-20)
                (30.0, 0.5),  # descending side midpoint
                (35.0, 0.25),  # descending side
                (40.0, 0.0),  # x = b (closed zero boundary)
                (100.0, 0.0),  # 0-plateau
            ],
        )

    # ------------------------------------------------------------------
    # right-shoulder(k1, k2, a, b): 0 on [k1, a], increasing, 1 on [b, k2]
    # ------------------------------------------------------------------

    def test_right_shoulder(self):
        f = RightConcreteConcept("R", 0.0, 100.0, 20.0, 40.0)
        self.check_table(
            f,
            [
                (0.0, 0.0),  # 0-plateau
                (20.0, 0.0),  # x = a (closed zero boundary)
                (25.0, 0.25),  # ascending side: (25-20)/(40-20)
                (30.0, 0.5),  # ascending side midpoint
                (35.0, 0.75),  # ascending side
                (40.0, 1.0),  # x = b (closed one boundary)
                (100.0, 1.0),  # 1-plateau
            ],
        )

    # ------------------------------------------------------------------
    # crisp(k1, k2, a, b): characteristic function of the closed [a, b]
    # ------------------------------------------------------------------

    def test_crisp(self):
        f = CrispConcreteConcept("C", 0.0, 100.0, 20.0, 40.0)
        self.check_table(
            f,
            [
                (0.0, 0.0),
                (19.5, 0.0),  # just below a
                (20.0, 1.0),  # x = a (closed)
                (30.0, 1.0),  # interior
                (40.0, 1.0),  # x = b (closed)
                (40.5, 0.0),  # just above b
                (100.0, 0.0),
            ],
        )

    # ------------------------------------------------------------------
    # linear(k1, k2, a, b): two segments through (0,0), (a,b), (1,1)
    # ------------------------------------------------------------------

    def test_linear(self):
        f = LinearConcreteConcept("Lin", 0.0, 1.0, 0.5, 0.25)
        self.check_table(
            f,
            [
                (-1.0, 0.0),  # below the domain
                (0.0, 0.0),  # x = 0 (closed zero boundary)
                (0.25, 0.125),  # first segment: (b/a)*x = 0.5*0.25
                (0.5, 0.25),  # x = a, value b
                (0.75, 0.625),  # second segment: (x(1-b)+(b-a))/(1-a)
                (1.0, 1.0),  # x = 1 (closed one boundary)
                (2.0, 1.0),  # above the domain
            ],
        )

    # ------------------------------------------------------------------
    # linear-modifier(c): a = c/(c+1), b = 1/(c+1), same two-segment shape
    # ------------------------------------------------------------------

    def test_linear_modifier(self):
        # c = 3 gives dyadic knees a = 0.75, b = 0.25.
        m = LinearModifier("lm3", 3.0)
        self.assertEqual(m.a, 0.75)
        self.assertEqual(m.b, 0.25)
        # Extremes and plateaus (exact).
        self.assertEqual(m.get_membership_degree(-0.5), 0.0)
        self.assertEqual(m.get_membership_degree(0.0), 0.0)
        self.assertEqual(m.get_membership_degree(1.0), 1.0)
        self.assertEqual(m.get_membership_degree(1.5), 1.0)
        # First segment, slope b/a = 1/3 (not dyadic).
        self.assertAlmostEqual(m.get_membership_degree(0.375), 0.125, places=12)
        self.assertAlmostEqual(m.get_membership_degree(0.75), 0.25, places=12)
        # Second segment: (0.875*0.75 - 0.5)/0.25 = 0.625 (dyadic).
        self.assertEqual(m.get_membership_degree(0.875), 0.625)

    # ------------------------------------------------------------------
    # triangular-modifier(a, b, c)
    # ------------------------------------------------------------------

    def test_triangular_modifier(self):
        m = TriangularModifier("tm", 0.0, 0.5, 1.0)
        self.assertEqual(m.get_membership_degree(-0.5), 0.0)
        self.assertEqual(m.get_membership_degree(0.0), 0.0)  # x = a (closed)
        self.assertEqual(m.get_membership_degree(0.25), 0.5)  # ascending side
        self.assertEqual(m.get_membership_degree(0.5), 1.0)  # x = b (peak)
        self.assertEqual(m.get_membership_degree(0.75), 0.5)  # descending side
        self.assertEqual(m.get_membership_degree(1.0), 0.0)  # x = c (closed)
        self.assertEqual(m.get_membership_degree(2.0), 0.0)

    # ------------------------------------------------------------------
    # modified(mod, f): f_mod(f_base(x)) on the domain (0, 1]
    # ------------------------------------------------------------------

    def test_modified_composition(self):
        # very = linear-modifier(2) over a trapezoidal base living in [0, 1].
        very = LinearModifier("very", 2.0)
        base = TrapezoidalConcreteConcept("TB", 0.0, 1.0, 0.0, 0.25, 0.5, 1.0)
        f = ModifiedConcreteConcept("veryTB", very, base)
        # Domain of the composition: (0, 1] (0 excluded, 1 included).
        self.assertEqual(f.get_membership_degree(0.0), 0.0)
        self.assertEqual(f.get_membership_degree(-1.0), 0.0)
        self.assertEqual(f.get_membership_degree(1.5), 0.0)
        # x = 1 is inside the domain: base(1) = 0 (x = d), very(0) = 0.
        self.assertEqual(f.get_membership_degree(1.0), 0.0)
        # Ascending side of the base: base(0.125) = 0.5, very(0.5) = 0.25.
        self.assertAlmostEqual(f.get_membership_degree(0.125), 0.25, places=12)
        # Core plateau: base(0.375) = 1, very(1) = 1 (exact).
        self.assertEqual(f.get_membership_degree(0.375), 1.0)
        # Descending side of the base: base(0.75) = 0.5, very(0.5) = 0.25.
        # Regression: pre-fix the base returned 3.0 there, so the modified
        # degree saturated at 1.0 instead of 0.25.
        self.assertAlmostEqual(f.get_membership_degree(0.75), 0.25, places=12)
        self.assertLess(f.get_membership_degree(0.75), 1.0)


if __name__ == "__main__":
    unittest.main()
