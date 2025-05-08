from __future__ import annotations

from abc import ABC

from fuzzy_reasoner.fuzzydl.concept.concept import Concept
from fuzzy_reasoner.fuzzydl.individual.individual import Individual
from fuzzy_reasoner.fuzzydl.milp.expression import Expression
from fuzzy_reasoner.fuzzydl.query.query import Query
from fuzzy_reasoner.fuzzydl.util.util import Util


class InstanceQuery(Query, ABC):
    def __init__(self, concept: Concept, individual: Individual) -> None:
        if concept.is_concrete():
            Util.error(f"Error: {concept} cannot be a concrete concept.")

        self.conc: Concept = concept
        self.ind: Individual = individual
        self.obj_expr: Expression = None
