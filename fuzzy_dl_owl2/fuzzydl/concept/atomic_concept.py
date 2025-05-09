from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class AtomicConcept(Concept):
    def __init__(self, name: str) -> None:
        super().__init__(c_type=ConceptType.ATOMIC, name=name)

    @staticmethod
    def new_atomic_concept() -> typing.Self:
        Concept.num_new_concepts += 1
        return AtomicConcept(
            f"NewConcept{Concept.SPECIAL_STRING}{Concept.num_new_concepts}"
        )

    def is_concrete(self) -> bool:
        return False

    def is_atomic(self) -> bool:
        return True

    def is_complemented_atomic(self) -> bool:
        return False

    def get_atomic_concepts(self) -> set[typing.Self]:
        return self.compute_atomic_concepts()

    def compute_name(self) -> str:
        return self.name

    def get_atoms(self) -> list[typing.Self]:
        return [self]

    def get_clauses(self, is_type: typing.Callable) -> set[typing.Self]:
        return set([self])

    def clone(self) -> typing.Self:
        return AtomicConcept(self.name)

    def compute_atomic_concepts(self) -> set[typing.Self]:
        return [self]

    def get_roles(self) -> set[str]:
        return set()

    def replace(self, a: typing.Self, c: typing.Self) -> typing.Optional[typing.Self]:
        if c.type == ConceptType.ATOMIC:
            if self == a:
                return c
            return self
        Util.error(f"Error replacing in concept {self}")

    def reduce_idempotency(self, is_type: typing.Callable) -> typing.Self:
        return self

    def __invert__(self) -> typing.Self:
        return -self

    def __neg__(self) -> typing.Self:
        return OperatorConcept.not_(self)

    def __and__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.and_(self, value)

    def __or__(self, value: typing.Self) -> typing.Self:
        return OperatorConcept.or_(self, value)

    def __rshift__(self, value: typing.Self) -> typing.Self:
        # return ImpliesConcept([self, value], ConceptType.GOEDEL_IMPLIES)
        pass

    def __eq__(self, value: typing.Self) -> bool:
        return isinstance(value, AtomicConcept) and str(self) == str(value)

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __hash__(self) -> int:
        return hash(self.name)

    def __repr__(self) -> str:
        return str(self)

    # def __str__(self) -> str:
    #     return self.compute_name()
