fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query





.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description-logic query that computes the maximum degree to which a given individual is an instance of a concept, by posing a mixed-integer linear optimization problem over the knowledge base.


Description
-----------


In fuzzy ontologies, membership in a concept is a matter of degree rather than a binary fact, so answering an instance query means finding the highest truth value the knowledge base can justify. **MaxInstanceQuery**, the central class, achieves this by introducing a fresh optimization variable representing the individual's membership degree, asserting that the individual belongs to the concept to at least that degree, and then maximizing the variable through the MILP solver. The maximization is expressed indirectly as the minimization of the variable's negation, matching the convention expected by the underlying optimizer, while a legacy counter of binary degree variables is kept in sync.

A key design decision is that all preparation happens on a *clone* of the knowledge base, so the assertions, solver state, and internal bookkeeping added while setting up the query never leak into the original ontology; this keeps queries side-effect free and allows many different queries to be run against the same knowledge base. During preparation, the concept's textual representation is inspected for universal restrictions or negated existential restrictions, and if either is present, dynamic blocking is enabled on the cloned knowledge base — a strategy required to reason correctly about those constructs. The assertion tying together the individual, the concept, and the degree variable is then handed to the solver before optimization begins.

At execution time the ABox is solved first, since a satisfiable ABox is a prerequisite for meaningful optimization; the cloned knowledge base is then prepared and optimized, with wall-clock timing recorded around the entire workflow. If solving reveals an inconsistent ontology, the exception is caught and a solution flagged as inconsistent is returned instead of the error propagating upward, giving callers a uniform result object in every case. The query also renders itself as a human-readable question ending in "? <=", reflecting the syntax convention used to distinguish maximum-membership queries from their plain counterparts.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query.MaxInstanceQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_instance_query_MaxInstanceQuery.png
       :alt: UML Class Diagram for MaxInstanceQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MaxInstanceQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_max_max_instance_query_MaxInstanceQuery.pdf
       :alt: UML Class Diagram for MaxInstanceQuery
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **MaxInstanceQuery**

.. py:class:: MaxInstanceQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.max.max_instance_query.MaxInstanceQuery
      :parts: 1
      :private-bases:


   This class implements a reasoning query designed to calculate the maximum degree of membership for a specific individual within a given concept. It functions by constructing an optimization problem that maximizes the variable associated with the individual's membership, effectively retrieving the highest truth value supported by the knowledge base. To ensure the integrity of the original state, the query operates on a cloned version of the knowledge base, where it preprocesses the problem by adding necessary assertions and enabling dynamic blocking strategies for complex logical constructs like universal quantification. The execution involves solving the ABox and optimizing the objective expression, returning a solution that reflects the maximum membership degree or indicates an inconsistent ontology if the constraints cannot be satisfied.


   .. py:method:: __str__() -> str

      Returns a formatted string representation of the query, posing the question of whether the individual `self.ind` is an instance of the concept `self.conc`. The string is constructed using an f-string and concludes with the suffix "? <=", adhering to a specific syntax likely used for display or serialization within the module. This operation is read-only and does not alter the state of the object.

      :return: Returns a string representation of the object, formatted as a question asking if `self.ind` is an instance of `self.conc`.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the knowledge base for a maximum instance query by initializing the necessary MILP variables and constraints. It retrieves the variable associated with the specific individual and concept, increments the counter for legacy binary variables, and constructs an objective expression to maximize the retrieved variable. If the concept expression involves universal restrictions or negated existential restrictions, the method enables dynamic blocking on the knowledge base to handle these specific logic constructs. Finally, it adds an assertion linking the individual, concept, and variable degree to the knowledge base and triggers the solver to process these assertions.

      :param kb: The KnowledgeBase instance managing the MILP context, variable storage, and assertion solving. It is updated with new constraints and internal counters during the preprocessing step.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Executes the solving workflow for the maximum instance query, starting a timer and invoking the ABox solver on the provided KnowledgeBase, potentially modifying it in place. The method then creates a clone of the KnowledgeBase to perform preprocessing and optimization based on the instance's objective expression, ensuring the optimization logic does not further alter the original input. After calculating the total execution time, the resulting Solution is returned. If the ontology is determined to be inconsistent during the ABox solving phase, the method handles the exception by returning a Solution indicating an inconsistent KnowledgeBase.

      :param kb: The knowledge base containing the ontology and constraints to be solved and optimized.
      :type kb: KnowledgeBase

      :return: The Solution object resulting from the optimization of the preprocessed knowledge base, or a solution indicating an inconsistent ontology.

      :rtype: Solution

