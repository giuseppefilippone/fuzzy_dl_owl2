import unittest

from test_aggregation import TestAggregation
from test_all import TestAll
from test_and import TestAnd
from test_blocking import TestBlocking
from test_datatype import TestDatatype
from test_disjoint import TestDisjoint
from test_functional import TestFunctional
from test_fuzzy_concrete_domain import TestFuzzyConcreteDomain
from test_fuzzy_number import TestFuzzyNumber
from test_implies import TestImplies
from test_implies_role import TestImpliesRole
from test_inconsistency import TestInconsistency
from test_instance import TestInstance
from test_inverse import TestInverse
from test_modifier import TestModifier
from test_not import TestNot
from test_or import TestOr
from test_reflexive import TestReflexive
from test_related import TestRelated
from test_rough_sets import TestRoughSets
from test_sat import TestSat
from test_self import TestSelf
from test_show_statement import TestShowStatement
from test_some import TestSome
from test_subsumption import TestSubsumption
from test_symmetric import TestSymmetric
from test_tbox import TestTbox
from test_threshold_concept import TestThresholdConcept
from test_transitive import TestTransitive
from test_truth_constant import TestTruthConstant
from test_weighted_concept import TestWeightedConcept
from test_weighted_sum import TestWeightedSum


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestAggregation))
    suite.addTests(loader.loadTestsFromTestCase(TestAll))
    suite.addTests(loader.loadTestsFromTestCase(TestAnd))
    suite.addTests(loader.loadTestsFromTestCase(TestDatatype))
    suite.addTests(loader.loadTestsFromTestCase(TestDisjoint))
    suite.addTests(loader.loadTestsFromTestCase(TestFunctional))
    suite.addTests(loader.loadTestsFromTestCase(TestFuzzyConcreteDomain))
    suite.addTests(loader.loadTestsFromTestCase(TestFuzzyNumber))
    suite.addTests(loader.loadTestsFromTestCase(TestImplies))
    suite.addTests(loader.loadTestsFromTestCase(TestImpliesRole))
    suite.addTests(loader.loadTestsFromTestCase(TestInconsistency))
    suite.addTests(loader.loadTestsFromTestCase(TestInstance))
    suite.addTests(loader.loadTestsFromTestCase(TestInverse))
    suite.addTests(loader.loadTestsFromTestCase(TestModifier))
    suite.addTests(loader.loadTestsFromTestCase(TestNot))
    suite.addTests(loader.loadTestsFromTestCase(TestOr))
    suite.addTests(loader.loadTestsFromTestCase(TestReflexive))
    suite.addTests(loader.loadTestsFromTestCase(TestRelated))
    suite.addTests(loader.loadTestsFromTestCase(TestRoughSets))
    suite.addTests(loader.loadTestsFromTestCase(TestSat))
    suite.addTests(loader.loadTestsFromTestCase(TestSelf))
    suite.addTests(loader.loadTestsFromTestCase(TestShowStatement))
    suite.addTests(loader.loadTestsFromTestCase(TestSome))
    suite.addTests(loader.loadTestsFromTestCase(TestSubsumption))
    suite.addTests(loader.loadTestsFromTestCase(TestSymmetric))
    suite.addTests(loader.loadTestsFromTestCase(TestTbox))
    suite.addTests(loader.loadTestsFromTestCase(TestThresholdConcept))
    suite.addTests(loader.loadTestsFromTestCase(TestTransitive))
    suite.addTests(loader.loadTestsFromTestCase(TestTruthConstant))
    suite.addTests(loader.loadTestsFromTestCase(TestWeightedConcept))
    suite.addTests(loader.loadTestsFromTestCase(TestWeightedSum))
    suite.addTests(loader.loadTestsFromTestCase(TestBlocking))
    return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2, failfast=True)
    runner.run(suite())
