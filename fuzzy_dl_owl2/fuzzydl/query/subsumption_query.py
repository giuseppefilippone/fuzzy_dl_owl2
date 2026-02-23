from __future__ import annotations

from abc import ABC

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class SubsumptionQuery(Query, ABC):
    """
    This abstract base class provides a structured interface for performing subsumption queries, specifically designed to evaluate the degree to which one concept is subsumed by another using fuzzy logic implications. Upon initialization, it accepts a subsumed concept, a subsumer concept, and a logic operator type defining the specific implication method to be used. A critical validation step ensures that neither concept is concrete, as subsumption queries are restricted to abstract concepts. The class prepares an objective expression attribute to hold the calculated degree of subsumption, which is typically populated by concrete subclasses.

    :param c1: The concept being subsumed, which must not be a concrete concept.
    :type c1: Concept
    :param c2: The concept acting as the subsumer in the subsumption relationship.
    :type c2: Concept
    :param type: The fuzzy implication operator used to evaluate the subsumption relationship.
    :type type: LogicOperatorType
    :param obj_expr: The objective expression representing the degree of subsumption.
    :type obj_expr: Expression
    """


    def __init__(self, c1: Concept, c2: Concept, s_type: LogicOperatorType) -> None:
        """
        Constructs a subsumption query object designed to evaluate the relationship between two concepts using a specified fuzzy implication logic. The initialization process enforces a strict constraint that neither the subsumed concept nor the subsumer concept can be concrete; if either is concrete, an error is triggered. Upon successful validation, the method stores the concepts, the logic operator type, and prepares a placeholder for the objective expression.

        :param c1: The subsumed concept in the logical relationship, which must be abstract (non-concrete).
        :type c1: Concept
        :param c2: The concept acting as the subsumer (general category) in the logical relationship. Must be an abstract concept.
        :type c2: Concept
        :param s_type: The fuzzy implication operator used to define the logical relationship.
        :type s_type: LogicOperatorType
        """

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
