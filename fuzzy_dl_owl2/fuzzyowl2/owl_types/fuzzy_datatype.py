import abc

class FuzzyDatatype(abc.ABC):

    def __init__(self) -> None:
        self._k1: float = 0.0
        self._k2: float = 0.0

    def get_min_value(self) -> float:
        return self._k1

    def get_max_value(self) -> float:
        return self._k2

    def set_min_value(self, min: float) -> None:
        self._k1 = min

    def set_max_value(self, max: float) -> None:
        self._k2 = max

    def __repr__(self) -> str:
        return str(self)
