from fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype import FuzzyDatatype


class TrapezoidalFunction(FuzzyDatatype):
    def __init__(self, a: float, b: float, c: float, d: float) -> None:
        super().__init__()
        self._a: float = a
        self._b: float = b
        self._c: float = c
        self._d: float = d

    def get_a(self) -> float:
        return self._a

    def get_b(self) -> float:
        return self._b

    def get_c(self) -> float:
        return self._c

    def get_d(self) -> float:
        return self._d

    def __str__(self) -> str:
        return f"trapezoidal({self._k1}, {self._k2}, {self._a}, {self._b}, {self._c}, {self._d})"
