from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier


class LinearModifier(FuzzyModifier):
    def __init__(self, c: float) -> None:
        super().__init__()
        self._c: float = c

    def get_c(self) -> float:
        return self._c

    def __str__(self) -> str:
        return f"linear-modifier({self._c})"
