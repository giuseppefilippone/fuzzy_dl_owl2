from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


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
