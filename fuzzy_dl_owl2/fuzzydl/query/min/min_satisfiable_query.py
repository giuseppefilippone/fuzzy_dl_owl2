from __future__ import annotations

import typing

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
from fuzzy_dl_owl2.fuzzydl.query.satisfiable_query import SatisfiableQuery
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import VariableType


class MinSatisfiableQuery(SatisfiableQuery):
    """This class defines a query to retrieve the minimal degree to which a fuzzy concept is satisfiable, either in general or with respect to a specific individual. It functions by transforming the logical problem into an optimization task, minimizing a variable that represents the satisfiability threshold. To use this entity, instantiate it with a `Concept` and optionally an `Individual`, then pass a `KnowledgeBase` to the `solve` method. The execution process clones the knowledge base to prevent side effects, handles existential restrictions by enabling dynamic blocking, and returns the calculated minimal degree or a status indicating inconsistency."""


    @typing.overload
    def __init__(self, c: Concept) -> None: ...

    @typing.overload
    def __init__(self, c: Concept, a: Individual) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes the query object by accepting either a single `Concept` or a `Concept` paired with an `Individual`. The method validates the input types and argument count, raising an assertion error if the first argument is not a `Concept` or if the second argument (when provided) is not an `Individual`. Depending on the number of arguments, the initialization logic is delegated to private helper methods to configure the internal state for the specific query type.

        :param args: Variable positional arguments representing either a single Concept or a Concept paired with an Individual.
        :type args: typing.Any
        """

        assert len(args) in [1, 2]
        assert isinstance(args[0], Concept)
        if len(args) == 1:
            self.__min_sat_query_init_1(*args)
        else:
            assert isinstance(args[1], Individual)
            self.__min_sat_query_init_2(*args)

    def __min_sat_query_init_1(self, c: Concept) -> None:
        """
        This method initializes the minimum satisfiability query object with a specific fuzzy concept intended for satisfiability testing. It delegates the core initialization logic to the parent class constructor, passing the provided concept to establish the internal state required for the query. This routine is part of the object's construction lifecycle, ensuring that the query is properly configured to evaluate the logical consistency of the given concept.

        :param c: The fuzzy concept to be evaluated for satisfiability.
        :type c: Concept
        """

        super().__init__(c)

    def __min_sat_query_init_2(self, c: Concept, a: Individual) -> None:
        """
        Initializes the minimum satisfiability query by delegating to the superclass constructor with the provided concept and individual. This method sets up the internal state necessary to evaluate whether the concept is satisfiable with respect to the specific individual. It acts as a constructor variant that binds the concept and individual arguments to the query instance.

        :param c: The fuzzy concept to be tested for satisfiability.
        :type c: Concept
        :param a: The individual entity used to evaluate the concept's satisfiability.
        :type a: Individual
        """

        super().__init__(c, a)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the KnowledgeBase to handle the query by transforming it into an optimization problem and solving the resulting constraints. It first inspects the conclusion string for existential quantifiers, enabling dynamic blocking on the KnowledgeBase if specific patterns are found. A new semi-continuous variable is then introduced into the underlying MILP solver to serve as the objective target. The method updates the internal variable counter, sets the objective expression to minimize this new variable, and adds a constraint linking the negated conclusion to the variable's degree. Finally, it triggers the immediate solving of the accumulated assertions.

        :param kb: The KnowledgeBase object that encapsulates the MILP solver, manages variable and assertion state, and controls solving behavior.
        :type kb: KnowledgeBase
        """

        if "(some " in str(self.conc) or "(b-some " in str(self.conc):
            kb.set_dynamic_blocking()
        q: Variable = kb.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(1.0, q))
        kb.add_assertion(
            self.ind,
            -self.conc,
            DegreeExpression.get_degree(Expression(1.0, Term(-1.0, q))),
        )
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Attempts to solve the minimal satisfiable query by optimizing the provided knowledge base. The method modifies the input knowledge base by incrementing its binary variable counter and creates a clone of the base, optionally excluding the ABox based on configuration or the presence of a specific individual. If no individual is currently assigned, a new one is generated within the cloned context. The process involves solving the ABox (if applicable), preprocessing the data, and executing an optimization routine against the objective expression. The resulting solution value is enforced to be non-negative. In the event of an inconsistent ontology, the method catches the exception and returns a solution indicating inconsistency. Additionally, the method tracks and updates the internal timing statistics for the operation.

        :param kb: The knowledge base defining the ontology and constraints for the optimization problem.
        :type kb: KnowledgeBase

        :return: A Solution object representing the optimal value found for the objective expression. If the ontology is inconsistent, returns a Solution indicating an inconsistent knowledge base. The solution value is guaranteed to be non-negative.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            kb.old_binary_variables += 1
            use_abox = self.ind is not None or ConfigReader.OPTIMIZATIONS == 0
            cloned: KnowledgeBase = kb.clone() if use_abox else kb.clone_without_abox()
            if self.ind is None:
                self.ind: Individual = cloned.get_new_individual()
            if use_abox:
                cloned.solve_abox()
            self.preprocess(cloned)
            sol: Solution = cloned.optimize(self.obj_expr)
            if sol.get_solution() < 0.0:
                sol = Solution(-sol.get_solution())
            self.set_total_time()
            return sol

        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the satisfiability query, formatted to indicate the concept being evaluated. If an individual is associated with the query instance, the string includes the individual's identifier in brackets. The output always concludes with a greater-than-or-equal-to symbol, suggesting a threshold or comparison context.

        :return: A string representation of the object, formatted as a satisfiability query for the concept and optionally the individual.

        :rtype: str
        """

        if self.ind is not None:
            return f"Is Concept {self.conc} satisfiable? [Individual {self.ind}] >= "
        return f"Is Concept {self.conc} satisfiable? >= "
