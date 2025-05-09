from __future__ import annotations

import re
import typing
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.util.constants import ConceptType


class Thing(ABC):

    def is_simplified(self) -> bool:
        """
        This function check if current formula is simplified, i.e., if:
            - The only negated elements are literal of kind (~ A), where A is an AtomicProposition
            - The OR operator is between:
                - Two literals => A | B
                - One literal and a AND => A | (B & C) - (A & B) | C
                - Two (or more) OR => (A & B) | (C & D) | (E & F)
            - The AND operator is between:
                - Two literals => A & B
                - One literal and a OR => A & (B | C) - (A | B) & C
                - Two (or more) AND => (A | B) & (C | D) & (E | F)
            - The only operators are AND, OR and NOT
        """
        return True

    def reduce_truth_values(self) -> typing.Self:
        return self

    def reduce_idempotency(self, is_type: typing.Callable) -> typing.Self:
        return self

    def reduce_double_negation(self) -> typing.Self:
        return self

    def distribute(self, c_type: ConceptType) -> typing.Self:
        return self

    def de_morgan(self) -> typing.Self:
        return self

    def reduce_quantifiers(self) -> typing.Self:
        return self

    def normal_form(self, is_type: typing.Callable) -> typing.Self:
        return self

    def classic_cnf(self) -> typing.Self:
        return self.normal_form(
            lambda x: isinstance(x, ConceptType) and x == ConceptType.OR
        )

    def classic_dnf(self) -> typing.Self:
        return self.normal_form(
            lambda x: isinstance(x, ConceptType) and x == ConceptType.AND
        )

    def goedel_cnf(self) -> typing.Self:
        return self.normal_form(
            lambda x: isinstance(x, ConceptType) and x == ConceptType.GOEDEL_OR
        )

    def goedel_dnf(self) -> typing.Self:
        return self.normal_form(
            lambda x: isinstance(x, ConceptType) and x == ConceptType.GOEDEL_AND
        )

    def lukasiewicz_cnf(self) -> typing.Self:
        return self.normal_form(
            lambda x: isinstance(x, ConceptType) and x == ConceptType.LUKASIEWICZ_OR
        )

    def lukasiewicz_dnf(self) -> typing.Self:
        return self.normal_form(
            lambda x: isinstance(x, ConceptType) and x == ConceptType.LUKASIEWICZ_AND
        )

    @staticmethod
    def contains_negated_subconcept(v: list[typing.Self], cj: typing.Self) -> int:
        try:
            return v.index(-cj)
        except ValueError:
            return -1

    @staticmethod
    def contains_subconcept(v: list[typing.Self], cj: typing.Self) -> bool:
        return cj in v

    @staticmethod
    def remove_element(v: list[typing.Self], i: int) -> None:
        if len(v) > i:
            v.pop(i)

    def is_concrete(self) -> bool:
        return False

    @abstractmethod
    def compute_name(self) -> typing.Optional[str]:
        pass

    def get_atoms(self) -> list[typing.Self]:
        return list()

    def get_clauses(self, is_type: typing.Callable) -> list[typing.Self]:
        return list()

    @abstractmethod
    def clone(self) -> typing.Self:
        pass

    @abstractmethod
    def compute_atomic_concepts(self) -> set[typing.Self]:
        pass

    def get_atomic_concepts(self) -> set[typing.Self]:
        return self.compute_atomic_concepts()

    @abstractmethod
    def get_roles(self) -> set[str]:
        pass

    @abstractmethod
    def replace(self, a: typing.Self, c: typing.Self) -> typing.Optional[typing.Self]:
        pass

    def has_nominals(self) -> bool:
        return "(b-some " in str(self)

    def __invert__(self) -> typing.Self:
        return -self

    @abstractmethod
    def __neg__(self) -> typing.Self:
        pass

    def __lt__(self, value: typing.Self) -> typing.Self:
        a, b = re.sub(r"[\(\)]+", "", str(self)), re.sub(r"[\(\)]+", "", str(value))
        return a < b

    def __le__(self, value: typing.Self) -> typing.Self:
        return not (self > value)

    def __gt__(self, value: typing.Self) -> typing.Self:
        a, b = re.sub(r"[\(\)]+", "", str(self)), re.sub(r"[\(\)]+", "", str(value))
        return a > b

    def __ge__(self, value: typing.Self) -> typing.Self:
        return not (self < value)

    @abstractmethod
    def __eq__(self, value: typing.Self) -> bool:
        pass

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __repr__(self) -> str:
        return str(self)

    # def __str__(self) -> str:
    #     return self.compute_name()


class Concept(Thing):
    SPECIAL_STRING = "@"
    DEFAULT_NAME = f"Concept{SPECIAL_STRING}"
    num_new_concepts = 1

    def __init__(
        self, c_type: ConceptType = ConceptType.ATOMIC, name: str = ""
    ) -> None:
        self._type: ConceptType = c_type
        self._name: str = name

    @property
    def type(self) -> ConceptType:
        return self._type

    @type.setter
    def type(self, new_type: ConceptType) -> None:
        self._type = new_type

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def is_atomic(self) -> bool:
        return self.type == ConceptType.ATOMIC

    def is_complemented_atomic(self) -> bool:
        return False

    # @abstractmethod
    def __iand__(self, value: typing.Self) -> typing.Self:
        pass

    def __and__(self, value: typing.Self) -> typing.Self:
        pass

    # @abstractmethod
    def __ior__(self, value: typing.Self) -> typing.Self:
        pass

    # @abstractmethod
    def __or__(self, value: typing.Self) -> typing.Self:
        pass

    # @abstractmethod
    def __irshift__(self, value: typing.Self) -> typing.Self:
        pass

    # @abstractmethod
    def __rshift__(self, value: typing.Self) -> typing.Self:
        pass

    def __eq__(self, value: typing.Self) -> bool:
        return str(self) == str(value)

    def __ne__(self, value: typing.Self) -> bool:
        return not (self == value)

    def __str__(self) -> str:
        if self.name is None:
            self.name = self.compute_name()
        return self.name
