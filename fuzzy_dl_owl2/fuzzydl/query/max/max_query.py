from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class MaxQuery(Query):
    """
    This class represents a query operation designed to determine the maximum possible value of a specific expression while maintaining consistency with the provided knowledge base. During execution, the system first verifies the consistency of the ABox and then performs an optimization on a cloned instance of the knowledge base. Internally, the target expression is negated before being passed to the optimizer, indicating that the underlying mechanism relies on minimization to achieve the maximization goal. If the knowledge base is found to be inconsistent, the query returns a solution indicating this state rather than a numerical result.

    :param obj_expr: The negated expression passed to the solver to find the maximum value.
    :type obj_expr: Expression
    """


    def __init__(self, expr: Expression) -> None:
        """
        Initializes a new instance of the MaxQuery class with the specified objective expression. The constructor transforms the maximization problem into a minimization problem by negating the provided expression, storing the result in the internal `obj_expr` attribute. It also invokes the superclass constructor to ensure proper initialization of any inherited components.

        :param expr: The expression to be maximized.
        :type expr: Expression
        """

        super().__init__()
        # Expression to be maximized
        self.obj_expr: Expression = Expression.negate_expression(expr)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the `MaxQuery` instance for execution by analyzing or indexing the provided `KnowledgeBase`. This method typically involves initializing internal state, optimizing the query structure, or setting up necessary bindings based on the schema and contents of the knowledge base. Since it returns `None`, the operation is performed in place, modifying the object's internal attributes to facilitate efficient computation of the maximum value during the subsequent evaluation phase.

        :param kb: The knowledge base to be prepared for further processing.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the optimization query against the provided KnowledgeBase by first performing ABox reasoning to ensure consistency and materialize inferences. The method creates a clone of the KnowledgeBase to preserve the original state and then runs an optimization routine on this clone using the query's objective expression. It measures and records the total execution time before returning the resulting Solution. If the KnowledgeBase is found to be inconsistent during the initial ABox solving phase, the method catches the exception and returns a Solution object indicating an inconsistent KB.

        :param kb: The knowledge base containing the ontology and data to be solved and optimized.
        :type kb: KnowledgeBase

        :return: A Solution object representing the optimization result of the knowledge base, or a Solution indicating inconsistency if the ontology cannot be solved.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            sol: Solution = cloned.optimize(self.obj_expr)
            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns a string representation of the maximum query object. This representation concatenates the object's expression attribute with the less-than-or-equal-to operator and a trailing space. The resulting string is typically used to display the constraint or condition defined by the query.

        :return: A string representing the object expression followed by the 'less than or equal to' operator.

        :rtype: str
        """

        return f"{self.obj_expr} <= "
