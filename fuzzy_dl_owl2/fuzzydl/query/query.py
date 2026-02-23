from __future__ import annotations

import time
from abc import ABC, abstractmethod

from fuzzy_dl_owl2.fuzzydl.knowledge_base import KnowledgeBase
from fuzzy_dl_owl2.fuzzydl.milp.solution import Solution


class Query(ABC):
    """
    This abstract base class serves as a foundational interface for defining questions that can be posed to a fuzzy knowledge base. It enforces the implementation of specific logic for preprocessing the knowledge base data and solving the query to produce a result, while also providing a mechanism for string representation. To facilitate performance analysis, the class includes built-in timing utilities that allow subclasses to record the start and end of the solving process and retrieve the total execution time in seconds.

    :param initial_time: Timestamp marking the start of the query execution, used to calculate the total duration of the solving process.
    :type initial_time: int
    :param total_time: Duration of the query execution in nanoseconds, calculated as the difference between the time when the query is solved and the initial time.
    :type total_time: int
    """


    def __init__(self) -> None:
        """Initializes a new instance of the `Query` class, preparing it to track time-related metrics. The method sets the `initial_time` and `total_time` attributes to zero, establishing a baseline state for subsequent operations. This ensures that the object starts with a clean slate before any timing logic is applied."""

        self.initial_time: int = 0
        self.total_time: int = 0

    def set_initial_time(self) -> None:
        """Records the current high-resolution monotonic time in nanoseconds as the starting point for the query. This method updates the `initial_time` attribute using `time.perf_counter_ns`, providing a precise timestamp for measuring execution duration or elapsed time. Note that invoking this method will overwrite any existing value in `initial_time`, effectively resetting the timer."""

        self.initial_time = time.perf_counter_ns()

    def set_total_time(self) -> None:
        """Calculates the elapsed duration since the operation began and stores the result in the instance. This method captures the current high-resolution time in nanoseconds and subtracts the timestamp stored in `initial_time` to compute the total execution time. The resulting duration is assigned to the `total_time` attribute, effectively finalizing the performance metric for the query. Note that calling this method multiple times will update `total_time` to reflect the duration from the original start time to the most recent call, rather than accumulating intervals."""

        end_time: int = time.perf_counter_ns()
        self.total_time = end_time - self.initial_time

    def get_total_time(self) -> float:
        """
        Returns the total execution time associated with the query in seconds. This method converts the internal time measurement, which is stored in nanoseconds, by dividing the raw value by one billion ($10^9$). The result is provided as a floating-point number for precise representation of the duration.

        :return: The total time in seconds.

        :rtype: float
        """

        return self.total_time / 1e9

    @abstractmethod
    def preprocess(self, knowledge_base: KnowledgeBase) -> None:
        """
        This abstract method defines the interface for preparing a query object before it is executed against a specific fuzzy knowledge base. Subclasses must implement this method to perform necessary setup operations, such as normalizing query terms, initializing data structures, or aligning the query with the knowledge base's schema. The method modifies the internal state of the query instance in place and does not return a value.

        :param knowledge_base: The fuzzy knowledge base over which the query preprocessing is performed.
        :type knowledge_base: KnowledgeBase
        """

        pass

    @abstractmethod
    def solve(self, knowledge_base: KnowledgeBase) -> Solution:
        """
        Resolves the current query by evaluating it against the provided knowledge base, which acts as the source of truth containing facts and rules. As an abstract method, it requires concrete subclasses to implement the specific reasoning or search algorithms necessary to derive a solution that satisfies the query's constraints. The method must handle edge cases such as unsolvable queries or empty knowledge bases, though the exact response—whether returning a null solution or raising an exception—is left to the implementation. While typically designed to be a read-only operation, side effects may occur depending on the specific logic defined in the subclass.

        :param knowledge_base: The repository of information or data used to derive the solution.
        :type knowledge_base: KnowledgeBase

        :return: A Solution object representing the result of resolving the query against the provided knowledge base.

        :rtype: Solution
        """

        pass

    @abstractmethod
    def __str__(self) -> str:
        """
        Returns a human-readable string representation of the query object. As an abstract method, it mandates that subclasses implement the logic for converting the query into a string format, which is utilized by the built-in `str()` function and print statements. The implementation should focus on describing the query's structure or intent rather than executing the query logic or interacting with the fuzzy knowledge base, ensuring that string conversion remains a side-effect-free operation.

        :return: A string representation of the object.

        :rtype: str
        """

        pass
