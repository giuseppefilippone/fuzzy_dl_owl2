from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_expression import DegreeExpression
from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.individual.individual import Individual
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.expression import Expression
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.milp.term import Term
from fuzzy_dl_owl2.fuzzydl.milp.variable import Variable
from fuzzy_dl_owl2.fuzzydl.query.instance_query import InstanceQuery
from fuzzy_dl_owl2.fuzzydl.util.constants import VariableType


class MinInstanceQuery(InstanceQuery):
    """This class models a query designed to retrieve the greatest lower bound of the degree of membership for a specific individual relative to a given concept. It functions by transforming the logical query into an optimization problem, specifically utilizing a semi-continuous variable to represent the degree of membership. To execute the query, the user must provide a target concept and an individual; the `solve` method then clones the current knowledge base to prevent side effects, applies necessary constraints, and performs an optimization to calculate the result. The implementation includes specific handling for existential restrictions and manages inconsistent ontology states by returning a designated solution type."""


    def __init__(self, concept: Concept, individual: Individual) -> None:
        """
        Initializes a new instance of the `MinInstanceQuery` class, which represents a query regarding a specific individual and a concept. The method requires a `Concept` object and an `Individual` object as arguments to define the scope of the query. It performs the initialization by forwarding these arguments directly to the constructor of the superclass, relying on the parent class to handle the underlying state management.

        :param concept: The concept instance used for initialization.
        :type concept: Concept
        :param individual: The specific entity or instance being represented.
        :type individual: Individual
        """

        super().__init__(concept, individual)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the minimum instance query for solving by introducing a new semi-continuous variable into the Knowledge Base's MILP solver and setting it as the objective to be minimized. The method inspects the query's conclusion for existential quantifiers, triggering dynamic blocking on the Knowledge Base if specific patterns are detected. It then encodes the logical structure of the query by adding an assertion that links the negation of the conclusion to the new variable via a linear constraint, specifically enforcing that the negated conclusion is greater than or equal to one minus the variable. This process modifies the Knowledge Base state and immediately triggers a solving step for the accumulated assertions.

        :param kb: The knowledge base instance used to manage variables, assertions, and solver state.
        :type kb: KnowledgeBase
        """

        q: Variable = kb.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(1.0, q))

        if "(some " in str(self.conc) or "(b-some " in str(self.conc):
            kb.set_dynamic_blocking()

        # a: not c >= 1-q
        kb.add_assertion(
            self.ind,
            -self.conc,
            DegreeExpression.get_degree(Expression(1.0, Term(-1.0, q))),
        )
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Orchestrates the resolution of the query by performing ABox reasoning, preprocessing, and optimization on the provided Knowledge Base. The method initiates timing, solves the ABox of the input KB, and then operates on a cloned version to apply preprocessing steps and optimize against the objective expression. It returns the resulting solution after calculating the total execution time. In the event that the ontology is inconsistent, the method catches the exception and returns a Solution object marked as inconsistent rather than propagating the error.

        :param kb: The knowledge base containing the ontology and data to be solved and optimized.
        :type kb: KnowledgeBase

        :return: A Solution object representing the result of optimizing the preprocessed knowledge base. If the knowledge base is inconsistent, returns a Solution indicating an inconsistent state.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            kb.solve_abox()
            cloned: KnowledgeBase = kb.clone()
            self.preprocess(cloned)
            sol: Solution = cloned.optimize(self.obj_expr)
            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the query object, formatted to ask whether the individual stored in `self.ind` is an instance of the concept stored in `self.conc`, followed by a threshold comparison indicator. This method is primarily used for debugging or logging purposes to visualize the specific parameters of the query in a structured format.

        :return: A human-readable string representation of the object, formatted as a query regarding whether `ind` is an instance of `conc`.

        :rtype: str
        """

        return f"Is {self.ind} instance of {self.conc} ? >= "
