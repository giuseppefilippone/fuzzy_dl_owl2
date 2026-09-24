fuzzy_dl_owl2.fuzzydl.query.query
=================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.query





.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that defines the interface every query must follow when evaluated against a fuzzy knowledge base, complete with built-in execution-time measurement.


Description
-----------


The ``Query`` class is the foundational contract for all concrete query types in the fuzzy description-logic reasoner, guaranteeing that every query shares a uniform lifecycle regardless of its specific purpose. Subclasses are required to implement three operations: a preprocessing step that prepares or normalizes the query in the context of a given ``KnowledgeBase``, a solving step that performs the actual reasoning and returns a ``Solution``, and a string conversion for human-readable display. Declaring these as abstract methods ensures that no query can be instantiated without complete reasoning logic, while leaving the algorithms themselves entirely to the concrete implementations. Separating preprocessing from solving also allows knowledge-base-specific setup to happen once, before the reasoning step runs.

A second responsibility is performance instrumentation. The base class records a high-resolution monotonic timestamp when a query starts and computes the elapsed duration in nanoseconds when it finishes, exposing the result as a floating-point number of seconds. Embedding this timing in the common ancestor means every query variant reports execution cost consistently, which is useful for benchmarking the underlying optimization-based reasoning. The timing state is deliberately minimal—two integer attributes initialized to zero—so subclasses incur no overhead beyond what they actively use, and repeated invocations recompute the measurement from the original start point rather than accumulating intervals.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.query.Query


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_query_Query.png
       :alt: UML Class Diagram for Query
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Query**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_query_Query.pdf
       :alt: UML Class Diagram for Query
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **Query**

.. py:class:: Query

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.query.Query
      :parts: 1
      :private-bases:


   This abstract base class serves as a foundational interface for defining questions that can be posed to a fuzzy knowledge base. It enforces the implementation of specific logic for preprocessing the knowledge base data and solving the query to produce a result, while also providing a mechanism for string representation. To facilitate performance analysis, the class includes built-in timing utilities that allow subclasses to record the start and end of the solving process and retrieve the total execution time in seconds.

   :param initial_time: Timestamp marking the start of the query execution, used to calculate the total duration of the solving process.
   :type initial_time: int
   :param total_time: Duration of the query execution in nanoseconds, calculated as the difference between the time when the query is solved and the initial time.
   :type total_time: int


   .. py:method:: __str__() -> str
      :abstractmethod:


      Returns a human-readable string representation of the query object. As an abstract method, it mandates that subclasses implement the logic for converting the query into a string format, which is utilized by the built-in `str()` function and print statements. The implementation should focus on describing the query's structure or intent rather than executing the query logic or interacting with the fuzzy knowledge base, ensuring that string conversion remains a side-effect-free operation.

      :return: A string representation of the object.

      :rtype: str



   .. py:method:: get_total_time() -> float

      Returns the total execution time associated with the query in seconds. This method converts the internal time measurement, which is stored in nanoseconds, by dividing the raw value by one billion ($10^9$). The result is provided as a floating-point number for precise representation of the duration.

      :return: The total time in seconds.

      :rtype: float



   .. py:method:: preprocess(knowledge_base: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None
      :abstractmethod:


      This abstract method defines the interface for preparing a query object before it is executed against a specific fuzzy knowledge base. Subclasses must implement this method to perform necessary setup operations, such as normalizing query terms, initializing data structures, or aligning the query with the knowledge base's schema. The method modifies the internal state of the query instance in place and does not return a value.

      :param knowledge_base: The fuzzy knowledge base over which the query preprocessing is performed.
      :type knowledge_base: KnowledgeBase



   .. py:method:: set_initial_time() -> None

      Records the current high-resolution monotonic time in nanoseconds as the starting point for the query. This method updates the `initial_time` attribute using `time.perf_counter_ns`, providing a precise timestamp for measuring execution duration or elapsed time. Note that invoking this method will overwrite any existing value in `initial_time`, effectively resetting the timer.



   .. py:method:: set_total_time() -> None

      Calculates the elapsed duration since the operation began and stores the result in the instance. This method captures the current high-resolution time in nanoseconds and subtracts the timestamp stored in `initial_time` to compute the total execution time. The resulting duration is assigned to the `total_time` attribute, effectively finalizing the performance metric for the query. Note that calling this method multiple times will update `total_time` to reflect the duration from the original start time to the most recent call, rather than accumulating intervals.



   .. py:method:: solve(knowledge_base: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution
      :abstractmethod:


      Resolves the current query by evaluating it against the provided knowledge base, which acts as the source of truth containing facts and rules. As an abstract method, it requires concrete subclasses to implement the specific reasoning or search algorithms necessary to derive a solution that satisfies the query's constraints. The method must handle edge cases such as unsolvable queries or empty knowledge bases, though the exact response—whether returning a null solution or raising an exception—is left to the implementation. While typically designed to be a read-only operation, side effects may occur depending on the specific logic defined in the subclass.

      :param knowledge_base: The repository of information or data used to derive the solution.
      :type knowledge_base: KnowledgeBase

      :return: A Solution object representing the result of resolving the query against the provided knowledge base.

      :rtype: Solution



   .. py:attribute:: initial_time
      :type:  int
      :value: 0



   .. py:attribute:: total_time
      :type:  int
      :value: 0

