import unittest

from fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept import (
    LinearConcreteConcept,
)
from fuzzy_dl_owl2.fuzzydl.exception.fuzzy_ontology_exception import (
    FuzzyOntologyException,
)

# Marker for table rows whose expected value is reached through non-dyadic
# arithmetic; those rows use assertAlmostEqual(places=12), the others are
# exact.
APPROX = "~"


def legacy_membership(f, value):
    """The pre-fix formula, valid only on the unit domain k1 = 0, k2 = 1.

    It compared the value with 0 and 1 (i.e. treated it as already
    normalised) while using the knee ``a`` in feature units.
    """

    if value <= 0:
        return 0.0
    if value >= 1.0:
        return 1.0
    if value <= f.a:
        return f.b / f.a * value
    return (value * (1.0 - f.b) + (f.b - f.a)) / (1.0 - f.a)


class TestLinearConcept(unittest.TestCase):
    """LinearConcreteConcept: membership in feature units and constructor checks.

    linear(k1, k2, a, b) is the piecewise linear function through
    (k1, 0), (a, b) and (k2, 1):

        0                                for x <= k1
        b (x - k1) / (a - k1)            for k1 < x <= a
        b + (1 - b) (x - a) / (k2 - a)   for a < x < k2
        1                                for x >= k2

    which is exactly what the MILP rows for the concept enforce.  The
    previous implementation compared x with 0 and 1 instead of k1 and k2,
    so it was right only on the unit domain; on [0, 100] every x >= 1
    saturated at 1.  On the unit domain the new formula reduces to the old
    one, and that identity is pinned below.

    The constructor (deliberate divergence from the Java oracle, which only
    checks k1 <= a and b <= 1) now requires k1 < k2, k1 < a < k2 (the
    degenerate knees a == k1 / a == k2 would make one ramp vertical) and
    0 <= b <= 1, reporting violations through Util.error, which raises
    FuzzyOntologyException.
    """

    def check_table(self, f, table):
        for row in table:
            x, expected = row[0], row[1]
            got = f.get_membership_degree(x)
            msg = f"{f.compute_name()}({x})"
            if len(row) > 2 and row[2] == APPROX:
                self.assertAlmostEqual(got, expected, places=12, msg=msg)
            else:
                self.assertEqual(got, expected, msg=msg)

    # ------------------------------------------------------------------
    # Unit domain: identical to the previous behaviour
    # ------------------------------------------------------------------

    def test_unit_domain(self):
        f = LinearConcreteConcept("Lin", 0.0, 1.0, 0.5, 0.4)
        self.check_table(
            f,
            [
                (0.0, 0.0),  # x = k1
                (0.25, 0.2),  # first ramp: 0.4 * 0.25 / 0.5
                (0.5, 0.4),  # x = a, value b
                (0.75, 0.7, APPROX),  # second ramp: 0.4 + 0.6 * 0.25 / 0.5
                (1.0, 1.0),  # x = k2
            ],
        )

    def test_unit_domain_matches_legacy_formula(self):
        # On k1 = 0, k2 = 1 the feature-unit formula must reproduce the old
        # one at every point (up to rounding of the second ramp).
        for a, b in ((0.5, 0.4), (0.5, 0.25), (0.25, 0.75), (0.8, 0.1)):
            f = LinearConcreteConcept("Lin", 0.0, 1.0, a, b)
            for i in range(-4, 25):
                x = i / 20.0  # -0.2 .. 1.2
                self.assertAlmostEqual(
                    f.get_membership_degree(x),
                    legacy_membership(f, x),
                    places=12,
                    msg=f"{f.compute_name()}({x})",
                )

    def test_unit_domain_out_of_domain(self):
        f = LinearConcreteConcept("Lin", 0.0, 1.0, 0.5, 0.4)
        self.assertEqual(f.get_membership_degree(-1.0), 0.0)
        self.assertEqual(f.get_membership_degree(2.0), 1.0)

    # ------------------------------------------------------------------
    # Percent domain [0, 100]: the case the old formula got wrong
    # ------------------------------------------------------------------

    def test_percent_domain(self):
        f = LinearConcreteConcept("Lin", 0.0, 100.0, 50.0, 0.4)
        self.check_table(
            f,
            [
                (0.0, 0.0),  # x = k1
                (25.0, 0.2, APPROX),  # first ramp: 0.4 * 25 / 50
                (50.0, 0.4),  # x = a, value b
                (75.0, 0.7, APPROX),  # second ramp: 0.4 + 0.6 * 25 / 50
                (100.0, 1.0),  # x = k2
            ],
        )

    def test_percent_domain_out_of_domain(self):
        f = LinearConcreteConcept("Lin", 0.0, 100.0, 50.0, 0.4)
        self.assertEqual(f.get_membership_degree(-1.0), 0.0)
        self.assertEqual(f.get_membership_degree(101.0), 1.0)

    def test_percent_domain_regression_not_saturated(self):
        # Pre-fix: every x >= 1 returned 1.0 on this domain.
        f = LinearConcreteConcept("Lin", 0.0, 100.0, 50.0, 0.4)
        self.assertLess(f.get_membership_degree(25.0), 1.0)
        self.assertLess(f.get_membership_degree(50.0), 1.0)
        self.assertLess(f.get_membership_degree(75.0), 1.0)

    # ------------------------------------------------------------------
    # A domain that does not start at 0
    # ------------------------------------------------------------------

    def test_shifted_domain(self):
        f = LinearConcreteConcept("Lin", 10.0, 30.0, 15.0, 0.25)
        self.check_table(
            f,
            [
                (10.0, 0.0),  # x = k1
                (12.5, 0.125),  # first ramp: 0.25 * 2.5 / 5
                (15.0, 0.25),  # x = a, value b
                (22.5, 0.625),  # second ramp: 0.25 + 0.75 * 7.5 / 15
                (30.0, 1.0),  # x = k2
                (5.0, 0.0),  # below the domain
                (35.0, 1.0),  # above the domain
            ],
        )

    def test_breakpoints_match_milp_encoding(self):
        # The three breakpoints the MILP rows are built on: (k1, 0), (a, b), (k2, 1).
        for k1, k2, a, b in (
            (0.0, 1.0, 0.5, 0.4),
            (0.0, 100.0, 50.0, 0.4),
            (10.0, 30.0, 15.0, 0.25),
            (-50.0, 50.0, 0.0, 0.75),
        ):
            f = LinearConcreteConcept("Lin", k1, k2, a, b)
            self.assertEqual(f.get_membership_degree(k1), 0.0, msg=f.compute_name())
            self.assertEqual(f.get_membership_degree(a), b, msg=f.compute_name())
            self.assertEqual(f.get_membership_degree(k2), 1.0, msg=f.compute_name())

    # ------------------------------------------------------------------
    # Constructor validation
    # ------------------------------------------------------------------

    def assert_rejected(self, k1, k2, a, b):
        with self.assertRaises(FuzzyOntologyException) as cm:
            LinearConcreteConcept("Lin", k1, k2, a, b)
        self.assertIn("Linear functions require", str(cm.exception))

    def test_rejects_a_equal_k1(self):
        self.assert_rejected(0.0, 1.0, 0.0, 0.4)

    def test_rejects_a_equal_k2(self):
        self.assert_rejected(0.0, 1.0, 1.0, 0.4)

    def test_rejects_a_below_k1(self):
        self.assert_rejected(0.0, 1.0, -0.5, 0.4)

    def test_rejects_a_above_k2(self):
        self.assert_rejected(0.0, 1.0, 1.5, 0.4)

    def test_rejects_k1_equal_k2(self):
        self.assert_rejected(1.0, 1.0, 1.0, 0.4)

    def test_rejects_k1_above_k2(self):
        self.assert_rejected(1.0, 0.0, 0.5, 0.4)

    def test_rejects_b_above_one(self):
        self.assert_rejected(0.0, 1.0, 0.5, 1.5)

    def test_rejects_b_below_zero(self):
        self.assert_rejected(0.0, 1.0, 0.5, -0.1)

    def test_accepts_b_boundaries(self):
        # b = 0 and b = 1 are legal knees (a flat first or second ramp).
        f0 = LinearConcreteConcept("Lin", 0.0, 1.0, 0.5, 0.0)
        self.assertEqual(f0.get_membership_degree(0.25), 0.0)
        self.assertEqual(f0.get_membership_degree(0.5), 0.0)
        self.assertEqual(f0.get_membership_degree(0.75), 0.5)
        f1 = LinearConcreteConcept("Lin", 0.0, 1.0, 0.5, 1.0)
        self.assertEqual(f1.get_membership_degree(0.25), 0.5)
        self.assertEqual(f1.get_membership_degree(0.5), 1.0)
        self.assertEqual(f1.get_membership_degree(0.75), 1.0)

    def test_stores_parameters_as_floats(self):
        f = LinearConcreteConcept("Lin", 0, 100, 50, 0.4)
        self.assertEqual((f.k1, f.k2, f.a, f.b), (0.0, 100.0, 50.0, 0.4))
        self.assertEqual(f.compute_name(), "linear(0.0, 100.0, 50.0, 0.4)")


if __name__ == "__main__":
    unittest.main()
