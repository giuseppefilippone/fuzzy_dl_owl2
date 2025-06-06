from __future__ import annotations

from abc import ABC

from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class RelatedQuery(Query, ABC):
    """Entailment of a role assertion query"""

    def __init__(self) -> None:
        super().__init__()
        # Abstract role
        self.role: str = None
        # Subject of the relation.
        self.ind1: Individual = None
        # Object of the relation.
        self.ind2: Individual = None
        # Objective expression
        self.obj_expr: Expression = None
