from __future__ import annotations

import typing

from fuzzy_dl_owl2.fuzzydl.classification_node import ClassificationNode
from fuzzy_dl_owl2.fuzzydl.concept.concept import Concept
from fuzzy_dl_owl2.fuzzydl.concept.implies_concept import ImpliesConcept
from fuzzy_dl_owl2.fuzzydl.concept.operator_concept import OperatorConcept
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
from fuzzy_dl_owl2.fuzzydl.query.subsumption_query import SubsumptionQuery
from fuzzy_dl_owl2.fuzzydl.util.config_reader import ConfigReader
from fuzzy_dl_owl2.fuzzydl.util.constants import LogicOperatorType, VariableType


class MinSubsumesQuery(SubsumptionQuery):
    """This class models a query designed to retrieve the minimum degree of subsumption between two fuzzy concepts within a knowledge base, effectively determining the infimum truth value of the assertion that one concept is subsumed by another. It supports various fuzzy logic operators—specifically Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh—translating the subsumption relationship into the corresponding logical implication for the selected logic. To use this entity, one must instantiate it with the two concepts involved in the relationship and the desired logic operator type, and then invoke the solve method with a target knowledge base. The solving process is optimized: if the knowledge base is pre-classified and the concepts are atomic, the result is fetched directly from the classification hierarchy; otherwise, the system clones the knowledge base, formulates a mixed-integer linear programming problem to minimize the degree of the implication, and returns the computed solution or an inconsistency flag if the ontology is invalid."""


    def __init__(self, c1: Concept, c2: Concept, type_: LogicOperatorType) -> None:
        """
        Initializes a new instance of a minimum subsumption query involving two specified concepts. This constructor accepts the left-hand and right-hand concepts, along with a logic operator type that defines the specific nature of the query. It delegates the actual initialization process to the parent class, passing the provided arguments to configure the underlying query structure.

        :param c1: The first concept operand involved in the logical operation.
        :type c1: Concept
        :param c2: The second Concept operand involved in the logical operation.
        :type c2: Concept
        :param type_: Specifies the logical operation to be performed between the two concepts.
        :type type_: LogicOperatorType
        """

        super().__init__(c1, c2, type_)

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the knowledge base for a minimum subsumption query by translating the logical relationship into a constraint suitable for optimization. If the knowledge base is already classified, the method returns immediately to avoid redundant processing. It constructs a specific implication concept based on the configured logic operator (Lukasiewicz, Gödel, Zadeh, or Kleene-Dienes) to represent the subsumption of the second concept by the first. A new semi-continuous optimization variable is introduced to represent the degree of subsumption, and an assertion is added to the knowledge base linking this variable to the negation of the constructed concept. The method concludes by invoking the solver to process the new assertions and update the knowledge base state.

        :param kb: The knowledge base instance to be modified by adding new variables, assertions, and solving constraints related to the logical operator.
        :type kb: KnowledgeBase
        """

        if kb.is_classified():
            return

        ind: Individual = kb.get_new_individual()

        if self.type == LogicOperatorType.LUKASIEWICZ:
            conc: Concept = OperatorConcept.lukasiewicz_or(-self.c2, self.c1)
        elif self.type == LogicOperatorType.GOEDEL:
            conc: Concept = ImpliesConcept.goedel_implies(self.c2, self.c1)
        elif self.type == LogicOperatorType.ZADEH:
            conc: Concept = ImpliesConcept.zadeh_implies(self.c2, self.c1)
        else:  # LogicOperatorType.KLEENE_DIENES
            conc: Concept = OperatorConcept.goedel_or(-self.c2, self.c1)

        q: Variable = kb.milp.get_new_variable(VariableType.SEMI_CONTINUOUS)
        kb.old_01_variables += 1
        self.obj_expr: Expression = Expression(Term(1.0, q))

        # a: not c or d >= 1-q
        kb.add_assertion(
            ind,
            -conc,
            DegreeExpression.get_degree(Expression(1.0, Term(-1.0, q))),
        )
        kb.solve_assertions()

    # def solve(self, kb: KnowledgeBase) -> Solution:
    #     try:
    #         self.set_initial_time()
    #         if ConfigReader.OPTIMIZATIONS == 0 or kb.has_nominals_in_tbox():
    #             cloned: KnowledgeBase = kb.clone()
    #             cloned.solve_abox()
    #         else:
    #             cloned: KnowledgeBase = kb.clone_without_abox()
    #         self.preprocess(cloned)
    #         sol: Solution = cloned.optimize(self.obj_expr)
    #         self.set_total_time()
    #         return sol
    #     except InconsistentOntologyException:
    #         return Solution(Solution.INCONSISTENT_KB)

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Solves the minimum subsumption query by evaluating the provided Knowledge Base. If the ontology is inconsistent, the method returns a solution indicating inconsistency immediately. For classified knowledge bases involving atomic concepts, it attempts to resolve the query using pre-computed classification nodes, returning a certainty of 1.0 if one of the concepts is the top-level 'Thing' or utilizing subsumption flags otherwise. In the general case, the method creates a clone of the knowledge base—potentially solving or removing the ABox depending on configuration and the presence of nominals—applies preprocessing, and executes an optimization routine to determine the solution. Throughout the process, the method updates internal timing metrics to track execution duration.

        :param kb: The knowledge base containing the ontology definitions and assertions to be processed.
        :type kb: KnowledgeBase

        :return: A Solution object containing the result of the reasoning task, which may be a subsumption flag, an optimization score, or an inconsistency indicator.

        :rtype: Solution
        """

        try:
            self.set_initial_time()
            if kb.is_classified() and self.c1.is_atomic() and self.c2.is_atomic():
                n1: typing.Optional[ClassificationNode] = kb.get_classification_node(
                    str(self.c1)
                )
                n2: typing.Optional[ClassificationNode] = kb.get_classification_node(
                    str(self.c2)
                )
                if n1 is not None and n1.is_thing():
                    sol: Solution = Solution(1.0)
                elif n2 is not None and n1.is_thing():
                    sol: Solution = Solution(1.0)
                else:
                    sol: Solution = Solution(kb.get_subsumption_flags(n1, n2))
            else:
                if ConfigReader.OPTIMIZATIONS == 0 or kb.has_nominals_in_tbox():
                    cloned: KnowledgeBase = kb.clone()
                    cloned.solve_abox()
                else:
                    cloned: KnowledgeBase = kb.clone_without_abox()
                self.preprocess(cloned)
                sol: Solution = cloned.optimize(self.obj_expr)

            self.set_total_time()
            return sol
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the subsumption query, formatted to display the relationship between the two components involved. The output string follows the pattern '{c1} subsumes {c2} ? >= ', where {c1} and {c2} are the string representations of the corresponding attributes. This method is side-effect free and implicitly converts the internal attributes to strings, making it suitable for debugging and logging purposes.

        :return: A string representation of the object in the format '{c1} subsumes {c2} ? >= '.

        :rtype: str
        """

        return f"{self.c1} subsumes {self.c2} ? >= "
