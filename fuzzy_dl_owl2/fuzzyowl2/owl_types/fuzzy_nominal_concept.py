from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class FuzzyNominalConcept(ConceptDefinition):

    def __init__(self, n: float, i: str) -> None:
        super().__init__(ConceptType.FUZZY_NOMINAL)
        self._n: float = n
        self._i: str = i

    def get_degree(self) -> float:
        return self._n

    def get_individual(self) -> str:
        return self._i

    def __str__(self) -> str:
        return f"({self.get_degree()}, {self.get_individual()})"
