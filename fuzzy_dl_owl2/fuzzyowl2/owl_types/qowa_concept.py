from fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition import ConceptDefinition
from fuzzy_dl_owl2.fuzzyowl2.util.constants import ConceptType


class QowaConcept(ConceptDefinition):

    def __init__(self, q: str, concepts: list[str]) -> None:
        super().__init__(ConceptType.QUANTIFIED_OWA)
        self._q: str = q
        self._concepts: list[str] = concepts

    def get_quantifier(self) -> str:
        return self._q

    def get_concepts(self) -> list[str]:
        return self._concepts

    def __str__(self) -> str:
        return f"(q-owa {self._q} {' '.join(self._concepts)})"
