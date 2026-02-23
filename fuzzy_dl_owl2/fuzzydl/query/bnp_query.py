from __future__ import annotations

from fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number import (
    TriangularFuzzyNumber,
)
from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution
from fuzzy_dl_owl2.fuzzydl.query.query import Query


class BnpQuery(Query):
    """
    This class encapsulates a query to determine the best non-fuzzy performance (BNP) of a given triangular fuzzy number, which is the specific value within the fuzzy set that possesses the highest degree of membership. It serves as a wrapper around a `TriangularFuzzyNumber` instance, delegating the calculation of this representative crisp value to the number itself. To utilize this functionality, instantiate the object with the desired fuzzy number and invoke the `solve` method, which returns a `Solution` containing the computed BNP. Note that while the solving interface accepts a knowledge base, the current implementation performs the calculation independently of the knowledge base contents.

    :param c: The triangular fuzzy number for which the best non-fuzzy performance is determined.
    :type c: TriangularFuzzyNumber
    """


    def __init__(self, c: TriangularFuzzyNumber) -> None:
        """
        Initializes a new instance of the query object, associating it with a specific triangular fuzzy number. This constructor accepts a single argument, `c`, which is expected to be an instance of `TriangularFuzzyNumber`, and stores it as an attribute on the instance. The method also invokes the initialization logic of the parent class to ensure proper object setup. No validation is explicitly performed on the input type within this method, so passing an incompatible object may lead to errors during subsequent operations.

        :param c: The triangular fuzzy number to initialize the instance with.
        :type c: TriangularFuzzyNumber
        """

        super().__init__()
        self.c: TriangularFuzzyNumber = c

    def preprocess(self, kb: KnowledgeBase) -> None:
        """
        Prepares the query instance for execution by performing necessary initialization and validation steps using the provided `KnowledgeBase`. This method typically involves resolving identifiers, checking schema compatibility, or constructing an internal execution plan based on the structure of the knowledge base. It modifies the state of the query object in place and should generally be called once before the main query logic is executed. Subsequent calls may re-initialize the state or be ignored depending on the specific implementation.

        :param kb: The knowledge base instance to be prepared or transformed for subsequent operations.
        :type kb: KnowledgeBase
        """

        pass

    def solve(self, kb: KnowledgeBase) -> Solution:
        """
        Resolves the query by retrieving the best precise performance metric from the internal solver component. It accepts a KnowledgeBase as input to satisfy the solving interface, and returns the identified non-fuzzy result encapsulated within a Solution object.

        :param kb: The KnowledgeBase instance containing the problem definition or context.
        :type kb: KnowledgeBase

        :return: A Solution object representing the best non-fuzzy performance.

        :rtype: Solution
        """

        return Solution(self.c.get_best_non_fuzzy_performance())

    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the query object, formatted as a label for the best non-fuzzy performance metric. The string includes the name of the computation obtained from the internal component and ends with an equals sign, suggesting it is designed to precede the actual performance value. This method relies on the `compute_name` method of the internal component and does not modify the object's state.

        :return: A string label representing the best non-fuzzy performance metric for the computed name.

        :rtype: str
        """

        return f"Best non-fuzzy performance of {self.c.compute_name()} = "
