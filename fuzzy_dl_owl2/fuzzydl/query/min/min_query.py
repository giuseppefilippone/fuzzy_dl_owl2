from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class MinQuery(Query):
    """
    This class defines a minimization query used to retrieve the smallest possible value of a specific expression subject to the constraints defined in a knowledge base. It operates by accepting an objective expression during initialization and, upon execution, verifying the consistency of the knowledge base before performing an optimization to find the minimum. Users should instantiate this class with the expression they wish to minimize and pass it to a solver, noting that it handles inconsistent knowledge bases by returning a specific failure solution.

    :param obj_expr: The expression representing the objective function to be minimized.
    :type obj_expr: typing.Any
    """


    def __init__(self, expr: Expression) -> None:
        """
        Initializes a new instance of a minimization query by storing the provided objective expression. The constructor accepts an `Expression` object, which is assigned to the `obj_expr` attribute to define the target function to be minimized. It also invokes the initialization logic of the parent class to ensure proper setup of the inheritance hierarchy.

        :param expr: The objective expression to be minimized.
        :type expr: Expression
        """

        super().__init__()
        # Expression to be minimized.
        self.obj_expr = expr

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the internal state of the query object based on the provided knowledge base. This method is intended to be overridden by subclasses to perform specific initialization logic, such as validating the knowledge base structure, indexing relevant entities, or constructing intermediate data structures required for efficient query execution. Since it modifies the object's state, it should be invoked prior to executing the main query logic, and subclasses may raise exceptions if the provided knowledge base is incompatible with the specific query requirements.

        :param kb: The knowledge base object to be preprocessed.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> None:
        """
        Executes the minimization query by first resolving the ABox of the provided knowledge base and then optimizing a clone of that base against the query's objective expression. The method tracks the total execution time required for these operations. If the knowledge base is found to be inconsistent, the method catches the resulting exception and returns a specific `Solution` object indicating an inconsistent state; otherwise, it returns the `Solution` obtained from the optimization process.

        :param kb: The knowledge base containing the ontology and data to be solved and optimized. The ABox is solved directly on this instance, while optimization is performed on a clone.
        :type kb: KnowledgeBase
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
        Returns a string representation of the minimum query, formatted as a partial expression involving the object's target expression and a greater-than-or-equal-to operator. The output string combines the stored object expression with a question mark and the comparison symbol, providing a human-readable or serialization-friendly version of the query structure. This method has no side effects and does not alter the internal state of the object.

        :return: A string representation of the object, formatted as the object expression followed by a parameter placeholder and the greater-than-or-equal-to operator.

        :rtype: str
        """

        return f"{self.obj_expr} ? >= "
