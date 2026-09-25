fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query
================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

A query that checks whether a fuzzy description-logic knowledge base is logically satisfiable, returning a solution scored at 1.0 when the base admits at least one satisfying interpretation and an inconsistency-marked solution otherwise.


Description
-----------


**KbSatisfiableQuery** is a specialised query type within the fuzzydl reasoning framework whose sole responsibility is global consistency checking: rather than asking about a particular concept or individual, it asks whether the knowledge base as a whole can be satisfied by any interpretation at all. It derives from the generic Query abstraction, which lets it plug into the same solve-and-report pipeline as every other kind of query, and it deliberately provides an empty preprocessing step because satisfiability checking requires no query-specific transformation of the input. A human-readable label is also supplied so that results can be presented to users as a direct answer to the question of whether the knowledge base is satisfiable.

The reasoning itself proceeds defensively and in two layers. The public ``solve`` method acts as a safe entry point: it delegates to an internal consistency test and converts the boolean outcome into a **Solution** object, wrapping the computation in exception handling so that an **InconsistentOntologyException** raised deep inside the reasoner surfaces as the same inconsistency result rather than as a crash. The internal test first solves the ABox of the given knowledge base and then continues its work on a clone, a deliberate design decision that shields the caller's original object from the mutations performed during reasoning; if that clone contains no individuals, a temporary one is injected so the underlying mixed-integer optimisation has something concrete to reason about. The final verdict comes from running the optimisation over the cloned knowledge base and inspecting whether the resulting solution reports consistency, which is then exposed to the caller either as a positive solution or as one flagged as inconsistent.

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
       :width: 9.3cm
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


