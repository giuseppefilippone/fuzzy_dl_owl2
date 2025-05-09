from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class WeightedConcept(ConceptDefinition):

    def __init__(self, n: float, c: str) -> None:
        super().__init__(ConceptType.WEIGHTED_CONCEPT)
        self._n: float = n
        self._c: str = c

    def get_number(self) -> float:
        return self._n

    def get_fuzzy_concept(self) -> str:
        return self._c

    def __str__(self) -> str:
        return f"({self._n} {self._c})"
