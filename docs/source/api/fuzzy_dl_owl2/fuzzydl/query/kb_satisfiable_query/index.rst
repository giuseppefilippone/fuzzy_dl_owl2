fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

Determines the satisfiability of a knowledge base by checking for logical consistency through optimization and ABox solving.


Description
-----------


Verifying the logical consistency of a knowledge base is the primary objective, achieved by extending the base query functionality to determine satisfiability. The evaluation process involves solving the ABox of the input knowledge base and then creating a clone to perform an optimization check, ensuring that the original structure is preserved while testing for contradictions. To handle edge cases where the knowledge base might be empty of individuals, the logic automatically generates a temporary individual to facilitate the optimization process. Ultimately, the operation returns a solution object indicating a perfect score if the base is consistent, or a specific inconsistency status if contradictions are detected or an ontology exception is raised during the reasoning phase.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query.KbSatisfiableQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_kb_satisfiable_query_KbSatisfiableQuery.png
       :alt: UML Class Diagram for KbSatisfiableQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **KbSatisfiableQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_kb_satisfiable_query_KbSatisfiableQuery.pdf
       :alt: UML Class Diagram for KbSatisfiableQuery
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **KbSatisfiableQuery**

.. py:class:: KbSatisfiableQuery

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query.KbSatisfiableQuery
      :parts: 1
      :private-bases:


   This class represents a query designed to determine the satisfiability of a Knowledge Base, effectively checking whether the base is logically consistent. It verifies if there exists at least one interpretation that satisfies all axioms defined within the provided Knowledge Base. To perform the check, an instance of this class should be created and its `solve` method called with the target `KnowledgeBase`. The query returns a `Solution` object containing a score of 1.0 if the base is satisfiable, or a status indicating inconsistency if contradictions are detected or an `InconsistentOntologyException` is raised during the reasoning process.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the query object, specifically designed to serve as a label for the satisfiability check. The implementation returns the static text "Is KnowledgeBase satisfiable? = ", which is typically used to prefix the result of the query when displaying output to a user. This method ignores the internal state of the object and provides a consistent prompt regardless of the specific knowledge base being evaluated.

      :return: Returns a string representation of the object, specifically the text 'Is KnowledgeBase satisfiable? = '.

      :rtype: str



   .. py:method:: is_consistent_kb(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> bool

      Evaluates whether the provided KnowledgeBase is logically consistent by attempting to find a valid solution through optimization. The process begins by solving the ABox of the input knowledge base, which results in a modification of the input object. A clone of the knowledge base is then created to isolate the check; if this clone lacks individuals, a temporary individual is generated to ensure the optimization can proceed. The method returns True if the optimization yields a solution that is itself consistent, and False otherwise.

      :param kb: The knowledge base to be evaluated for logical consistency.
      :type kb: KnowledgeBase

      :return: True if the knowledge base is consistent, False otherwise. Consistency is determined by solving the ABox and verifying the existence of a valid solution after optimization.

      :rtype: bool



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the provided knowledge base for the satisfiability evaluation process by performing necessary transformations or optimizations. This method operates via side effects, potentially modifying the internal state of the query object or the structure of the knowledge base itself to facilitate efficient querying. It does not return a value, and implementations should handle edge cases such as empty or already preprocessed knowledge bases gracefully.

      :param kb: The knowledge base object to be prepared or cleaned.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Evaluates the satisfiability of the provided Knowledge Base by verifying its internal consistency. If the knowledge base is determined to be consistent, the method returns a Solution object with a confidence score of 1.0. Conversely, if the knowledge base is inconsistent or if an InconsistentOntologyException is raised during the evaluation process, the method returns a Solution marked as inconsistent. This operation does not modify the input Knowledge Base.

      :param kb: The knowledge base to be solved or checked for consistency.
      :type kb: KnowledgeBase

      :return: A Solution object representing the outcome of the operation. It returns a solution initialized with 1.0 if the knowledge base is consistent, or a solution marked as inconsistent if the knowledge base is invalid or an ontology exception occurs.

      :rtype: Solution


