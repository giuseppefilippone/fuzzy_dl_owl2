from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class RelatedQuery(Query):

    def __init__(self) -> None:
        super().__init__()
        self.role: str = None
        self.ind1: Individual = None
        self.ind2: Individual = None
        self.obj_expr: Expression = None
