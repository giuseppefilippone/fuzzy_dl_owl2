from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class SubsumptionQuery(Query):

    def __init__(self, c1: Concept, c2: Concept, s_type: LogicOperatorType) -> None:
        super().__init__()
        if c1.is_concrete():
            Util.error(f"Error: {c1} cannot be a concrete concept.")
        if c2.is_concrete():
            Util.error(f"Error: {c1} cannot be a concrete concept.")
        # Subsumed concept
        self.c1: Concept = c1
        # Subsumer concept
        self.c2: Concept = c2
        # Fuzzy implication used
        self.type: LogicOperatorType = s_type
        # Objective epxression
        self.obj_expr: Expression = None
