fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query





.. ── LLM-GENERATED DESCRIPTION START ──

A query that computes the minimum degree to which one fuzzy concept subsumes another in a fuzzy description logic knowledge base, casting the question as a mixed-integer linear programming problem.


Description
-----------


MinSubsumesQuery specialises the generic subsumption query to answer "to what degree is one concept subsumed by another?" under a user-chosen fuzzy logic — Łukasiewicz, Gödel, Kleene-Dienes, or Zadeh — with the selected operator dictating how the subsumption relationship is rewritten into its corresponding fuzzy implication. The central design decision is the reduction of subsumption testing to optimisation: preprocessing constructs the appropriate implication concept, introduces a fresh semi-continuous variable to represent the subsumption degree, and injects an assertion into the knowledge base so that minimising that variable yields the infimum truth value of the implication. Solving follows a two-tier strategy for efficiency: when the knowledge base has already been classified and both concepts are atomic, the answer is read directly from the precomputed classification hierarchy (with special handling when a concept is the top concept), bypassing the solver entirely; otherwise the knowledge base is cloned — retaining or discarding the ABox depending on the configured optimisation level and the presence of nominals in the TBox — preprocessed, and optimised over the objective expression built earlier. Robustness is handled by catching ontology-inconsistency exceptions and returning a solution that flags the inconsistent knowledge base rather than propagating the error, while timing metrics are recorded around the solve step to support performance instrumentation. A human-readable string rendering of the query rounds out the class, formatting the two concepts into a "subsumes" question suitable for logging and debugging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query.MinSubsumesQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_subsumes_query_MinSubsumesQuery.png
       :alt: UML Class Diagram for MinSubsumesQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MinSubsumesQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_subsumes_query_MinSubsumesQuery.pdf
       :alt: UML Class Diagram for MinSubsumesQuery
       :align: center
       :width: 13.9cm
       :class: uml-diagram

       UML Class Diagram for **MinSubsumesQuery**

.. py:class:: MinSubsumesQuery(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, type_: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.subsumption_query.SubsumptionQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.min.min_subsumes_query.MinSubsumesQuery
      :parts: 1
      :private-bases:


   This class models a query designed to retrieve the minimum degree of subsumption between two fuzzy concepts within a knowledge base, effectively determining the infimum truth value of the assertion that one concept is subsumed by another. It supports various fuzzy logic operators—specifically Łukasiewicz, Gödel, Kleene-Dienes, and Zadeh—translating the subsumption relationship into the corresponding logical implication for the selected logic. To use this entity, one must instantiate it with the two concepts involved in the relationship and the desired logic operator type, and then invoke the solve method with a target knowledge base. The solving process is optimized: if the knowledge base is pre-classified and the concepts are atomic, the result is fetched directly from the classification hierarchy; otherwise, the system clones the knowledge base, formulates a mixed-integer linear programming problem to minimize the degree of the implication, and returns the computed solution or an inconsistency flag if the ontology is invalid.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the subsumption query, formatted to display the relationship between the two components involved. The output string follows the pattern '{c1} subsumes {c2} ? >= ', where {c1} and {c2} are the string representations of the corresponding attributes. This method is side-effect free and implicitly converts the internal attributes to strings, making it suitable for debugging and logging purposes.

      :return: A string representation of the object in the format '{c1} subsumes {c2} ? >= '.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the knowledge base for a minimum subsumption query by translating the logical relationship into a constraint suitable for optimization. If the knowledge base is already classified, the method returns immediately to avoid redundant processing. It constructs a specific implication concept based on the configured logic operator (Lukasiewicz, Gödel, Zadeh, or Kleene-Dienes) to represent the subsumption of the second concept by the first. A new semi-continuous optimization variable is introduced to represent the degree of subsumption, and an assertion is added to the knowledge base linking this variable to the negation of the constructed concept. The method concludes by invoking the solver to process the new assertions and update the knowledge base state.

      :param kb: The knowledge base instance to be modified by adding new variables, assertions, and solving constraints related to the logical operator.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solves the minimum subsumption query by evaluating the provided Knowledge Base. If the ontology is inconsistent, the method returns a solution indicating inconsistency immediately. For classified knowledge bases involving atomic concepts, it attempts to resolve the query using pre-computed classification nodes, returning a certainty of 1.0 if one of the concepts is the top-level 'Thing' or utilizing subsumption flags otherwise. In the general case, the method creates a clone of the knowledge base—potentially solving or removing the ABox depending on configuration and the presence of nominals—applies preprocessing, and executes an optimization routine to determine the solution. Throughout the process, the method updates internal timing metrics to track execution duration.

      :param kb: The knowledge base containing the ontology definitions and assertions to be processed.
      :type kb: KnowledgeBase

      :return: A Solution object containing the result of the reasoning task, which may be a subsumption flag, an optimization score, or an inconsistency indicator.

      :rtype: Solution

