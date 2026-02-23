fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query



.. ── LLM-GENERATED DESCRIPTION START ──

Determines the maximum degree to which one fuzzy concept is subsumed by another by transforming the logical relationship into a minimization problem within a knowledge base.


Description
-----------


MaxSubsumesQuery handles the computation of subsumption degrees by leveraging mixed-integer linear programming to optimize an objective derived from fuzzy logic implications. Depending on the configured operator type, such as Łukasiewicz or Zadeh, the logic constructs a corresponding implication or operator concept to represent the relationship between the input concepts. To preserve the integrity of the original data, the process operates on a cloned instance of the knowledge base, optionally solving the ABox before proceeding with the optimization. The preprocessing phase creates a new individual and links it to the constructed concept, setting the associated variable as the objective to be minimized. Finally, the optimization routine attempts to find the minimum value for this variable, which corresponds to the maximum subsumption degree, while gracefully managing exceptions related to inconsistent ontologies.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query.MaxSubsumesQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_subsumes_query_MaxSubsumesQuery.png
       :alt: UML Class Diagram for MaxSubsumesQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MaxSubsumesQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_subsumes_query_MaxSubsumesQuery.pdf
       :alt: UML Class Diagram for MaxSubsumesQuery
       :align: center
       :width: 14.1cm
       :class: uml-diagram

       UML Class Diagram for **MaxSubsumesQuery**

.. py:class:: MaxSubsumesQuery(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, type_: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.subsumption_query.SubsumptionQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.max.max_subsumes_query.MaxSubsumesQuery
      :parts: 1
      :private-bases:


   Represents a query to determine the maximum degree to which one fuzzy concept is subsumed by another within a knowledge base. It supports various fuzzy logic operators, including Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh, to define the semantics of the subsumption relationship. The query is resolved by transforming the subsumption check into an optimization problem, specifically minimizing the degree of an implication assertion derived from the input concepts. This process involves cloning the knowledge base, preprocessing the concepts into a solvable form, and optimizing an objective expression to retrieve the solution.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the subsumption query, formatted as a question asking whether the first concept subsumes the second. The representation interpolates the two concepts stored in the instance into a specific syntax that includes the phrase "subsumes" and the suffix "? <= ". This method is primarily intended for logging, debugging, or displaying the query to the user, and it does not modify the state of the object.

      :return: A string representing the subsumption query between `self.c1` and `self.c2`.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the query for execution by constructing a logical implication concept within the provided Knowledge Base. It creates a new individual and determines the specific implication structure based on the configured logic operator type (Lukasiewicz, Goedel, Kleene-Dienes, or Zadeh). The method retrieves the corresponding MILP variable for this individual and concept, sets the query's objective expression to minimize this variable, and adds an assertion linking them. As a side effect, it increments the Knowledge Base's counter for legacy binary variables and triggers the immediate solving of current assertions.

      :param kb: The KnowledgeBase instance on which to perform preprocessing operations. It is used to generate new individuals, access MILP variables, add assertions, and trigger the solving process.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the optimization query on the provided knowledge base to generate a solution. The method begins by initializing performance timers and conditionally cloning the knowledge base; if optimizations are disabled or nominals are present in the TBox, the ABox is solved within the clone, otherwise, the clone is created without the ABox. Following preprocessing, the method invokes the optimization routine on the cloned instance using the internal objective expression. If the ontology is found to be inconsistent during this process, the method catches the exception and returns a solution object indicating inconsistency. The original knowledge base remains unmodified, while internal timing metrics are updated.

      :param kb: The knowledge base containing the ontology to be solved or optimized.
      :type kb: KnowledgeBase

      :return: The Solution object resulting from optimizing the knowledge base, or a solution indicating inconsistency if the ontology is invalid.

      :rtype: Solution


