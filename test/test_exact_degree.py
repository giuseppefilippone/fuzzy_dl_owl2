import unittest

from parser_interface import ParserInterface

from fuzzy_dl_owl2.fuzzydl.util import constants
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader


class TestExactDegree(unittest.TestCase):
    """An assertion at the exact membership degree of a datatype restriction
    must be satisfiable, and min-instance? must return that degree.

    The feature values (4.4, 2.9, 3.05, ...) are not exactly representable
    in binary. With the Gurobi default Big-M (1000 * (2^31 - 1)) the
    datatype-restriction rows lose the threshold below the double ulp of 2M
    and the exact assertion becomes inconsistent; KnowledgeBase.adapt_big_m
    (or an explicit maxVal) keeps M at the scale of the feature ranges.
    """

    # (KB file, expected degree): right-shoulder(2,5), left-shoulder(2,5),
    # trapezoidal(2,10,20,30), triangular(10,20,40), several points per side.
    CASES = [
        ("datatypeExact1.txt", 0.8),
        ("datatypeExact2.txt", 0.3),
        ("datatypeExact3.txt", 0.35),
        ("datatypeExact4.txt", 0.2),
        ("datatypeExact5.txt", 0.7),
        ("datatypeExact6.txt", 0.3),
        ("datatypeExact7.txt", 0.6),
        ("datatypeExact8.txt", 0.25),
        ("datatypeExact9.txt", 0.1),
        ("datatypeExact10.txt", 0.29),
        ("datatypeExact11.txt", 0.55),
        ("datatypeExact12.txt", 0.89),
        ("datatypeExact13.txt", 0.28),
    ]

    def test_exact_degree_is_consistent(self):
        for kb_file, expected in self.CASES:
            with self.subTest(kb=kb_file):
                p = ParserInterface(f"../examples/TestSuite/{kb_file}")
                self.assertEqual(expected, p.solve(), "TestExactDegree")

    def test_maxval_override_from_config(self):
        saved = (ConfigReader.MAXVAL, constants.MAXVAL, constants.MAXVAL2)
        try:
            ConfigReader.load_parameters(None, maxVal="1000000")
            self.assertEqual(1000000.0, ConfigReader.MAXVAL)
            self.assertEqual(1000000.0, constants.MAXVAL)
            self.assertEqual(2000000.0, constants.MAXVAL2)
            ConfigReader.load_parameters(None, maxVal="auto")
            self.assertIsNone(ConfigReader.MAXVAL)
            self.assertEqual(constants.MAXVAL_DEFAULT, constants.MAXVAL)
        finally:
            ConfigReader.MAXVAL, constants.MAXVAL, constants.MAXVAL2 = saved


if __name__ == "__main__":
    unittest.main()
