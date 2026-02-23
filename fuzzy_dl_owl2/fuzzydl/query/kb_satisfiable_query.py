from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.exception.inconsistent_ontology_exception import (
    InconsistentOntologyException,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class KbSatisfiableQuery(Query):
    """This class represents a query designed to determine the satisfiability of a Knowledge Base, effectively checking whether the base is logically consistent. It verifies if there exists at least one interpretation that satisfies all axioms defined within the provided Knowledge Base. To perform the check, an instance of this class should be created and its `solve` method called with the target `KnowledgeBase`. The query returns a `Solution` object containing a score of 1.0 if the base is satisfiable, or a status indicating inconsistency if contradictions are detected or an `InconsistentOntologyException` is raised during the reasoning process."""


    def __init__(self) -> None:
        """Initializes a new instance of the `KbSatisfiableQuery` class by delegating the setup process to its parent class. This constructor invokes the superclass's `__init__` method without passing any additional arguments, ensuring that the object is initialized according to the logic defined in the ancestor class. No specific attributes or state modifications are introduced at this level."""

        super().__init__()

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the provided knowledge base for the satisfiability evaluation process by performing necessary transformations or optimizations. This method operates via side effects, potentially modifying the internal state of the query object or the structure of the knowledge base itself to facilitate efficient querying. It does not return a value, and implementations should handle edge cases such as empty or already preprocessed knowledge bases gracefully.

        :param kb: The knowledge base object to be prepared or cleaned.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Evaluates the satisfiability of the provided Knowledge Base by verifying its internal consistency. If the knowledge base is determined to be consistent, the method returns a Solution object with a confidence score of 1.0. Conversely, if the knowledge base is inconsistent or if an InconsistentOntologyException is raised during the evaluation process, the method returns a Solution marked as inconsistent. This operation does not modify the input Knowledge Base.

        :param kb: The knowledge base to be solved or checked for consistency.
        :type kb: KnowledgeBase

        :return: A Solution object representing the outcome of the operation. It returns a solution initialized with 1.0 if the knowledge base is consistent, or a solution marked as inconsistent if the knowledge base is invalid or an ontology exception occurs.

        :rtype: Solution
        """

        try:
            return (
                Solution(1.0)
                if self.is_consistent_kb(kb)
                else Solution(Solution.INCONSISTENT_KB)
            )
        except InconsistentOntologyException:
            return Solution(Solution.INCONSISTENT_KB)

    def is_consistent_kb(self, kb: KnowledgeBase) -> bool:
        """
        Evaluates whether the provided KnowledgeBase is logically consistent by attempting to find a valid solution through optimization. The process begins by solving the ABox of the input knowledge base, which results in a modification of the input object. A clone of the knowledge base is then created to isolate the check; if this clone lacks individuals, a temporary individual is generated to ensure the optimization can proceed. The method returns True if the optimization yields a solution that is itself consistent, and False otherwise.

        :param kb: The knowledge base to be evaluated for logical consistency.
        :type kb: KnowledgeBase

        :return: True if the knowledge base is consistent, False otherwise. Consistency is determined by solving the ABox and verifying the existence of a valid solution after optimization.

        :rtype: bool
        """

        kb.solve_abox()
        cloned: KnowledgeBase = kb.clone()
        if len(cloned.individuals) == 0:
            cloned.get_new_individual()
            cloned.solve_assertions()
        sol: Solution = cloned.optimize(None)
        return sol is not None and sol.is_consistent_kb()

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the query object, specifically designed to serve as a label for the satisfiability check. The implementation returns the static text "Is KnowledgeBase satisfiable? = ", which is typically used to prefix the result of the query when displaying output to a user. This method ignores the internal state of the object and provides a consistent prompt regardless of the specific knowledge base being evaluated.

        :return: Returns a string representation of the object, specifically the text 'Is KnowledgeBase satisfiable? = '.

        :rtype: str
        """

        return "Is KnowledgeBase satisfiable? = "
