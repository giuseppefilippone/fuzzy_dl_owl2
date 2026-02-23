import traceback

from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query
from fuzzy_dl_owl2.fuzzydl.util.util import Util


class ClassificationQuery(Query):

    """This class defines a specific type of inquiry designed to trigger the classification of a knowledge base. It operates by invoking the classification method on the provided knowledge base object during the solve phase. If the classification completes without error, the query returns a successful solution with a score of 1.0; however, if the process raises an exception, it interprets this as an inconsistency within the knowledge base and returns the corresponding error state. Unlike other query types, this implementation does not require any preprocessing steps before execution."""

    def __init__(self) -> None:
        """Initializes a new instance of the ClassificationQuery class. This method delegates the core initialization logic to the parent class by invoking its constructor, ensuring that inherited attributes are properly set up. No specific parameters are required for this initialization, and any exceptions raised by the parent class during instantiation will be propagated to the caller."""

        super().__init__()

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the current query instance for execution by resolving and validating its parameters against the provided KnowledgeBase. This method typically performs lookups to map external identifiers or labels to internal representations used by the system, ensuring that all constraints are valid within the context of the specific knowledge base. It operates by mutating the internal state of the query object rather than returning a new instance, potentially raising exceptions if the referenced classes or entities do not exist in the KnowledgeBase.

        :param kb: The knowledge base instance to be prepared or modified for subsequent operations.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Executes the classification process on the provided KnowledgeBase to determine a solution. This method invokes the classification logic of the knowledge base and returns a Solution object representing a successful outcome if no errors occur. Should an exception be raised during classification, the method logs the traceback and returns a Solution indicating that the knowledge base is inconsistent, thereby preventing the exception from propagating.

        :param kb: The knowledge base instance to be solved.
        :type kb: KnowledgeBase

        :return: A Solution object representing the outcome of the classification attempt. It indicates success with a value of 1.0 or failure due to an inconsistent knowledge base.

        :rtype: Solution
        """

        try:
            kb.classify()
            return Solution(1.0)
        except Exception as ex:
            Util.debug(traceback.format_exc())
            return Solution(Solution.INCONSISTENT_KB)

    def __str__(self) -> str:
        """
        Returns the string representation of the `ClassificationQuery` object, specifically the constant prompt "Classify? <= ". This method is invoked when the object is converted to a string or printed, providing a standardized textual format that indicates the nature of the query. The output is static and does not depend on the internal state of the instance.

        :return: Returns the string representation of the object, specifically the prompt 'Classify? <= '.

        :rtype: str
        """

        return "Classify? <= "
