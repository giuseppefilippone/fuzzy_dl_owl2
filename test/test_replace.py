import unittest

from fuzzy_dl_owl2.fuzzydl.concept.all_some_concept import AllSomeConcept
from fuzzy_dl_owl2.fuzzydl.concept.atomic_concept import AtomicConcept
from fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept import (
    LinearlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept import ModifiedConcept
from fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept import (
    TriangularlyModifiedConcept,
)
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.concept.owa_concept import OwaConcept
from fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier import LinearModifier
from fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier import TriangularModifier
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class TestReplace(unittest.TestCase):
    """Concept.replace must perform plain substitution, preserving polarity.

    The Java oracle negates the result in the modified/OWA classes and
    dispatches on the replacement's type in the operator class (copy-paste of
    each class's complement()); these are deliberate divergences, see
    CLAUDE.md section 9. replace() is currently dead code in the reasoning
    paths, so these are construction-level checks, not KB solves.
    """

    def setUp(self):
        self.c = AtomicConcept("C")
        self.d = AtomicConcept("D")
        self.very = LinearModifier("very", 2.0)

    def test_atomic_plain(self):
        self.assertEqual(str(self.c.replace(self.c, self.d)), str(self.d))

    def test_some_plain(self):
        some = AllSomeConcept.some("R", self.c)
        self.assertEqual(
            str(some.replace(self.c, self.d)), str(AllSomeConcept.some("R", self.d))
        )

    def test_linearly_modified_preserves_polarity(self):
        mod = LinearlyModifiedConcept(self.c, self.very)
        result = mod.replace(self.c, self.d)
        self.assertEqual(
            str(result), str(LinearlyModifiedConcept(self.d, self.very))
        )
        self.assertNotEqual(result.type, ConceptType.COMPLEMENT)

    def test_triangularly_modified_preserves_polarity(self):
        roughly = TriangularModifier("roughly", 0.0, 0.5, 1.0)
        mod = TriangularlyModifiedConcept(self.c, roughly)
        result = mod.replace(self.c, self.d)
        self.assertEqual(
            str(result), str(TriangularlyModifiedConcept(self.d, roughly))
        )
        self.assertNotEqual(result.type, ConceptType.COMPLEMENT)

    def test_owa_preserves_polarity(self):
        owa = OwaConcept([0.6, 0.4], [self.c, self.d])
        result = owa.replace(self.c, self.d)
        self.assertEqual(str(result), str(OwaConcept([0.6, 0.4], [self.d, self.d])))
        self.assertNotEqual(result.type, ConceptType.COMPLEMENT)

    def test_operator_and_preserves_type(self):
        e = AtomicConcept("E")
        conj = OperatorConcept.goedel_and(self.c, self.d)
        result = conj.replace(self.c, e)
        self.assertEqual(str(result), str(OperatorConcept.goedel_and(e, self.d)))

    def test_operator_complement_replaces_child(self):
        neg = OperatorConcept.not_(self.c)
        result = neg.replace(self.c, self.d)
        self.assertIsNotNone(result)
        self.assertEqual(str(result), str(OperatorConcept.not_(self.d)))

    def test_operator_atomic_replacement_not_none(self):
        # The Java oracle's switch on the replacement's type returned null here.
        neg = OperatorConcept.not_(AllSomeConcept.some("R", self.c))
        result = neg.replace(self.c, self.d)
        self.assertIsNotNone(result)
        self.assertEqual(
            str(result), str(OperatorConcept.not_(AllSomeConcept.some("R", self.d)))
        )

    def test_modified_concept_is_abstract(self):
        with self.assertRaises(TypeError):
            ModifiedConcept(self.c, self.very)


if __name__ == "__main__":
    unittest.main()
