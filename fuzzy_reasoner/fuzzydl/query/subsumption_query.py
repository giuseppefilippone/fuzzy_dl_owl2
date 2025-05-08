from __future__ import annotations

from fuzzy_reasoner.fuzzydl.concept.concept import Concept
from fuzzy_reasoner.fuzzydl.milp.expression import Expression
from fuzzy_reasoner.fuzzydl.query.query import Query
from fuzzy_reasoner.fuzzydl.util.constants import LogicOperatorType
from fuzzy_reasoner.fuzzydl.util.util import Util


class SubsumptionQuery(Query):

    def __init__(self, c1: Concept, c2: Concept, s_type: LogicOperatorType) -> None:
        if c1.is_concrete():
            Util.error(f"Error: {c1} cannot be a concrete concept.")
        if c2.is_concrete():
            Util.error(f"Error: {c1} cannot be a concrete concept.")
        self.c1: Concept = c1
        self.c2: Concept = c2
        self.type: LogicOperatorType = s_type
        self.obj_expr: Expression = None
