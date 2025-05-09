from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType


class PrimitiveConceptDefinition:

    def __init__(
        self,
        defined: str,
        definition: Concept,
        implication: LogicOperatorType,
        degree: float,
    ) -> None:
        self.defined: str = defined
        self.definition: Concept = definition
        self.degree: float = degree
        self.implication: LogicOperatorType = implication

    def clone(self) -> typing.Self:
        return PrimitiveConceptDefinition(
            self.defined, self.definition, self.implication, self.degree
        )

    def get_defined_concept(self) -> str:
        return self.defined

    def get_definition(self) -> Concept:
        return self.definition

    def set_definition(self, definition: Concept) -> None:
        self.definition = definition

    def get_degree(self) -> float:
        return self.degree

    def set_degree(self, deg: float) -> None:
        self.degree = deg

    def get_type(self) -> LogicOperatorType:
        return self.implication

    def __eq__(self, other: typing.Self) -> bool:
        return (
            isinstance(other, PrimitiveConceptDefinition)
            and self.defined == other.defined
            and self.definition == other.definition
            and self.degree == other.degree
            and self.implication == other.implication
        )

    def __ne__(self, other: typing.Self) -> bool:
        return not (self == other)

    def __lt__(self, other: typing.Self) -> bool:
        return isinstance(other, PrimitiveConceptDefinition) and hash(self) < hash(
            other
        )

    def __le__(self, other: typing.Self) -> bool:
        return not (self > other)

    def __gt__(self, other: typing.Self) -> bool:
        return isinstance(other, PrimitiveConceptDefinition) and hash(self) > hash(
            other
        )

    def __ge__(self, other: typing.Self) -> bool:
        return not (self < other)

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"{self.defined} =>_{self.implication.name[0]} {self.definition} >= {self.degree}"
