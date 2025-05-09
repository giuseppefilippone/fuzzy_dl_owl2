from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedSumZeroConcept(ConceptDefinition):

    def __init__(self, wc: list[ConceptDefinition]) -> None:
        super().__init__(ConceptType.WEIGHTED_SUM_ZERO)
        self._wc: list[ConceptDefinition] = wc

    def get_weighted_concepts(self) -> list[ConceptDefinition]:
        return self._wc

    def __str__(self) -> str:
        return f"(w-sum-zero {self._wc})"
