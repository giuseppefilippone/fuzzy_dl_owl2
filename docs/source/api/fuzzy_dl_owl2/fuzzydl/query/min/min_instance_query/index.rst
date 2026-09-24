fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query





.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy description-logic query that computes the greatest lower bound of the degree to which a given individual is an instance of a concept, by translating the logical question into a mixed-integer linear program and minimizing a semi-continuous membership variable.


Description
-----------


``MinInstanceQuery`` specializes the generic instance query to answer the question "what is the minimum degree to which an individual belongs to a concept?" in a fuzzy ontology, where membership is a matter of degree rather than a boolean fact. Rather than evaluating the logic directly, the reasoning task is reduced to numerical optimization: a fresh semi-continuous variable is introduced to stand for the membership degree, and that variable becomes the objective of a MILP minimization performed over the knowledge base's solver. The encoding works by asserting that the individual belongs to the *negation* of the target concept with a degree of at least one minus the new variable, so that minimizing the variable drives the provable membership degree as high as the constraints permit; the resulting optimum is exactly the tightest lower bound derivable from the ontology. When the queried concept contains existential restrictions, detected through textual markers such as "(some " or "(b-some ", dynamic blocking is activated on the knowledge base to keep the reasoning procedure finite.

Execution is designed to be side-effect free and robust: the knowledge base is first solved at the ABox level, then cloned before any preprocessing constraints are applied, ensuring the caller's original state remains untouched while the query runs. Inconsistency is handled gracefully — if the ontology turns out to be unsatisfiable, the raised exception is intercepted and a dedicated solution object flagging the inconsistent state is returned instead of letting the error propagate upward. Timing instrumentation records the total reasoning time, and a human-readable string representation of the query is provided for debugging and logging purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query.MinInstanceQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_instance_query_MinInstanceQuery.png
       :alt: UML Class Diagram for MinInstanceQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MinInstanceQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_instance_query_MinInstanceQuery.pdf
       :alt: UML Class Diagram for MinInstanceQuery
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **MinInstanceQuery**

.. py:class:: MinInstanceQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.min.min_instance_query.MinInstanceQuery
      :parts: 1
      :private-bases:


   This class models a query designed to retrieve the greatest lower bound of the degree of membership for a specific individual relative to a given concept. It functions by transforming the logical query into an optimization problem, specifically utilizing a semi-continuous variable to represent the degree of membership. To execute the query, the user must provide a target concept and an individual; the `solve` method then clones the current knowledge base to prevent side effects, applies necessary constraints, and performs an optimization to calculate the result. The implementation includes specific handling for existential restrictions and manages inconsistent ontology states by returning a designated solution type.


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the query object, formatted to ask whether the individual stored in `self.ind` is an instance of the concept stored in `self.conc`, followed by a threshold comparison indicator. This method is primarily used for debugging or logging purposes to visualize the specific parameters of the query in a structured format.

      :return: A human-readable string representation of the object, formatted as a query regarding whether `ind` is an instance of `conc`.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the minimum instance query for solving by introducing a new semi-continuous variable into the Knowledge Base's MILP solver and setting it as the objective to be minimized. The method inspects the query's conclusion for existential quantifiers, triggering dynamic blocking on the Knowledge Base if specific patterns are detected. It then encodes the logical structure of the query by adding an assertion that links the negation of the conclusion to the new variable via a linear constraint, specifically enforcing that the negated conclusion is greater than or equal to one minus the variable. This process modifies the Knowledge Base state and immediately triggers a solving step for the accumulated assertions.

      :param kb: The knowledge base instance used to manage variables, assertions, and solver state.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Orchestrates the resolution of the query by performing ABox reasoning, preprocessing, and optimization on the provided Knowledge Base. The method initiates timing, solves the ABox of the input KB, and then operates on a cloned version to apply preprocessing steps and optimize against the objective expression. It returns the resulting solution after calculating the total execution time. In the event that the ontology is inconsistent, the method catches the exception and returns a Solution object marked as inconsistent rather than propagating the error.

      :param kb: The knowledge base containing the ontology and data to be solved and optimized.
      :type kb: KnowledgeBase

      :return: A Solution object representing the result of optimizing the preprocessed knowledge base. If the knowledge base is inconsistent, returns a Solution indicating an inconsistent state.

      :rtype: Solution

