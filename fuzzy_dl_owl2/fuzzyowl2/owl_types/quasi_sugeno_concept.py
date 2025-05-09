from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class QsugenoConcept(ConceptDefinition):

    def __init__(self, weights: list[float], concepts: list[str]) -> None:
        super().__init__(ConceptType.QUASI_SUGENO)
        self._weights: list[float] = weights
        self._concepts: list[str] = concepts

    def get_weights(self) -> list[float]:
        return self._weights

    def get_concepts(self) -> list[str]:
        return self._concepts

    def __str__(self) -> str:
        return (
            f"(q-sugeno ({' '.join(map(str, self._weights))}) ({' '.join(self._concepts)}))"
        )
