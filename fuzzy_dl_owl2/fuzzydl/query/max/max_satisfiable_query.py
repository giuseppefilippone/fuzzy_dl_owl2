from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.degree.degree_variable import DegreeVariable
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


class MaxSatisfiableQuery(SatisfiableQuery):
    """This class models a query to determine the maximal degree to which a fuzzy concept is satisfiable within a given knowledge base. It operates by formulating an optimization problem that seeks the highest possible truth value for a given concept, either in general or with respect to a specific individual. To use it, instantiate the object with the target concept and optionally an individual; if the individual is omitted, the query will generate a new one to assess general satisfiability. When executed, the query clones the knowledge base to prevent side effects, preprocesses the concept to handle specific logical constructs like universal quantifiers, and solves a mixed-integer linear program to return the optimal satisfaction degree."""


    @typing.overload
    def __init__(self, c: Concept) -> None: ...

    @typing.overload
    def __init__(self, c: Concept, a: Individual) -> None: ...

    def __init__(self, *args) -> None:
        """
        Initializes a new instance for handling maximum satisfiability queries, accepting either one or two arguments. The first argument is mandatory and must be a `Concept` object, which serves as the primary subject of the query. If a second argument is provided, it must be either `None` or an `Individual` object, allowing the query to be scoped to a specific entity. The constructor delegates the actual setup to private helper methods depending on the number of arguments supplied.

        :param args: A variable-length argument list accepting either a single Concept, or a Concept followed by an optional Individual (or None).
        :type args: typing.Any
        """

        assert len(args) in [1, 2]
        assert isinstance(args[0], Concept)
        if len(args) == 1:
            self.__max_sat_query_init_1(*args)
        else:
            assert args[1] is None or isinstance(args[1], Individual)
            self.__max_sat_query_init_2(*args)

    def __max_sat_query_init_1(self, c: Concept) -> None:
        """
        Initializes the query instance to evaluate the maximum satisfiability of a specific fuzzy concept. This method delegates the core setup logic to the parent class constructor, passing the provided concept to ensure the query context is correctly established. It prepares the object for subsequent reasoning operations by storing the concept within the inherited query structure.

        :param c: The fuzzy concept to be tested for satisfiability.
        :type c: Concept
        """

        super().__init__(c)

    def __max_sat_query_init_2(self, c: Concept, a: Individual) -> None:
        """
        Initializes the instance by delegating to the superclass constructor with a specific concept and individual. This setup prepares a satisfiability query designed to evaluate whether the provided individual satisfies the given concept. As a specialized initialization method, it relies on the parent class to handle the actual assignment and validation of the arguments, ensuring the query is correctly configured for subsequent operations.

        :param c: The fuzzy concept to be evaluated for satisfiability.
        :type c: Concept
        :param a: The specific individual instance for which the satisfiability of the concept is being evaluated.
        :type a: Individual
        """

        super().__init__(c, a)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the query for optimization by inspecting the conclusion string for specific logical constructs, such as universal quantifiers or negated bounded existential quantifiers. If these patterns are detected, the method enables dynamic blocking on the provided KnowledgeBase to handle the query efficiently. It retrieves the corresponding MILP variable, updates the internal counter for legacy binary variables, and constructs an objective expression designed to maximize the variable's value. Finally, it adds the assertion to the knowledge base and triggers the solving of the current set of assertions, modifying the state of both the query and the knowledge base.

        :param kb: The KnowledgeBase instance managing the MILP model and solver state. It is accessed to retrieve variables, configure blocking strategies, add assertions, and trigger the solving process.
        :type kb: KnowledgeBase
        """

        if "(all " in str(self.conc) or "(not (b-some " in str(self.conc):
            kb.set_dynamic_blocking()
        q: Variable = kb.milp.get_variable(self.ind, self.conc)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(-1.0, q))
        kb.add_assertion(self.ind, self.conc, DegreeVariable.get_degree(q))
        kb.solve_assertions()

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Solves the Max-Satisfiability query for the provided Knowledge Base by cloning the input and executing a sequence of logical optimizations. The method determines whether to utilize the ABox based on configuration settings or the presence of a specific individual, initializing a new individual if one is not already defined. It preprocesses the cloned Knowledge Base, resolves the ABox if required, and performs optimization using the instance's objective expression. If the calculated solution value is negative, it is converted to its absolute value before returning. The method handles inconsistent ontologies by returning a specific solution state and updates internal timing metrics as a side effect.

        :param kb: The knowledge base containing the ontology and instance data to be optimized.
        :type kb: KnowledgeBase

        :return: A Solution object representing the result of the optimization process, containing the optimal value (normalized to be non-negative) or a status indicating the knowledge base is inconsistent.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
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
        Returns a human-readable string representation of the satisfiability query, formatted as a question asking if the stored concept is satisfiable. If the query is constrained by a specific individual, indicated by `self.ind` not being None, the string includes the individual's identifier within brackets. The resulting string always terminates with a less-than-or-equal-to symbol and a space, suggesting it may be used as a prefix for further output or solver interaction.

        :return: Returns a string representation of the satisfiability query, formatted to include the concept and optionally the individual.

        :rtype: str
        """

        if self.ind is not None:
            return f"Is Concept {self.conc} satisfiable? [Individual {self.ind}] <= "
        return f"Is Concept {self.conc} satisfiable? <= "
