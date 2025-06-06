import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable


class SigmaCount:
    """Sigma-count pending tasks."""

    def __init__(
        self,
        var: Variable,
        ind: Individual,
        inds: list[Individual],
        role: str,
        concept: Concept,
    ) -> None:
        self.variable: Variable = var
        self.individual: Individual = ind
        self.individuals: list[Individual] = inds
        self.role: str = role
        self.concept: Concept = concept

    def clone(self) -> typing.Self:
        return SigmaCount(
            self.variable.clone(),
            self.individual.clone(),
            [i.clone() for i in self.individuals],
            self.role,
            self.concept.clone(),
        )

    def get_variable(self) -> Variable:
        return self.variable

    def get_individual(self) -> Individual:
        return self.individual

    def get_individuals(self) -> list[Individual]:
        return self.individuals

    def get_role(self) -> str:
        return self.role

    def get_concept(self) -> Concept:
        return self.concept

    def __hash__(self) -> int:
        return hash(str(self))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return f"sigma-count({self.variable}, {self.individual}, {self.individuals}, {self.role}, {self.concept})"
