from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier import FuzzyModifier


class TriangularModifier(FuzzyModifier):
    def __init__(self, a: float, b: float, c: float) -> None:
        super().__init__()
        self._a: float = a
        self._b: float = b
        self._c: float = c

    def get_a(self) -> float:
        return self._a

    def get_b(self) -> float:
        return self._b

    def get_c(self) -> float:
        return self._c

    def __str__(self) -> str:
        return f"triangular-modifier({self._a}, {self._b}, {self._c})"
