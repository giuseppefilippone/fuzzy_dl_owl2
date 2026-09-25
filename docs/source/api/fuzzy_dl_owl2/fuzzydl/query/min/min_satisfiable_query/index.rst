fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a fuzzy description-logic query that computes the minimal degree to which a fuzzy concept is satisfiable, either in general or with respect to a specific individual, by recasting the logical question as a mixed-integer linear optimization problem.


Description
-----------


MinSatisfiableQuery specializes the generic satisfiability-query machinery for the fuzzy setting, where satisfiability is not a yes/no matter but a matter of degree. Two overloaded construction forms are supported — one taking only a concept, for concept-level satisfiability, and one pairing a concept with an individual, for instance-level satisfiability — with the argument shapes and types validated through assertions before being delegated to small private helpers that forward to the superclass constructor. The central design decision is to compile the question into a MILP: preprocessing introduces a fresh semi-continuous variable into the underlying solver to serve as the satisfiability threshold, sets the objective to minimize that variable, and adds an assertion binding the negation of the queried concept to the variable's degree, so that the program's optimum is exactly the minimal satisfiability degree. Because existential restrictions in the concept can prevent the reasoning procedure from terminating, dynamic blocking is enabled on the knowledge base whenever the concept's textual form contains an existential quantifier pattern.

Execution is deliberately side-effect free with respect to the caller's knowledge base: the base is cloned, with the ABox dropped when no individual is involved and optimizations are enabled, and a fresh individual is minted for concept-only queries. When the ABox is retained it is solved first, after which the optimization runs against the prepared objective expression. The optimal value is normalized to be non-negative before being returned, and an ontology-inconsistency exception raised anywhere in the pipeline is caught and converted into a solution that flags the knowledge base as inconsistent rather than propagating the error. Timing statistics are recorded around the solve so that query performance can be tracked alongside the result, and a human-readable string representation of the query is provided for reporting purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query.MinSatisfiableQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_satisfiable_query_MinSatisfiableQuery.png
       :alt: UML Class Diagram for MinSatisfiableQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **MinSatisfiableQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_min_min_satisfiable_query_MinSatisfiableQuery.pdf
       :alt: UML Class Diagram for MinSatisfiableQuery
       :align: center
       :width: 11.6cm
       :class: uml-diagram

       UML Class Diagram for **MinSatisfiableQuery**

.. py:class:: MinSatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)
              MinSatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.satisfiable_query.SatisfiableQuery`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query.MinSatisfiableQuery
      :parts: 1
      :private-bases:


   This class defines a query to retrieve the minimal degree to which a fuzzy concept is satisfiable, either in general or with respect to a specific individual. It functions by transforming the logical problem into an optimization task, minimizing a variable that represents the satisfiability threshold. To use this entity, instantiate it with a `Concept` and optionally an `Individual`, then pass a `KnowledgeBase` to the `solve` method. The execution process clones the knowledge base to prevent side effects, handles existential restrictions by enabling dynamic blocking, and returns the calculated minimal degree or a status indicating inconsistency.


   .. py:method:: __min_sat_query_init_1(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      This method initializes the minimum satisfiability query object with a specific fuzzy concept intended for satisfiability testing. It delegates the core initialization logic to the parent class constructor, passing the provided concept to establish the internal state required for the query. This routine is part of the object's construction lifecycle, ensuring that the query is properly configured to evaluate the logical consistency of the given concept.

      :param c: The fuzzy concept to be evaluated for satisfiability.
      :type c: Concept



   .. py:method:: __min_sat_query_init_2(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Initializes the minimum satisfiability query by delegating to the superclass constructor with the provided concept and individual. This method sets up the internal state necessary to evaluate whether the concept is satisfiable with respect to the specific individual. It acts as a constructor variant that binds the concept and individual arguments to the query instance.

      :param c: The fuzzy concept to be tested for satisfiability.
      :type c: Concept
      :param a: The individual entity used to evaluate the concept's satisfiability.
      :type a: Individual



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the satisfiability query, formatted to indicate the concept being evaluated. If an individual is associated with the query instance, the string includes the individual's identifier in brackets. The output always concludes with a greater-than-or-equal-to symbol, suggesting a threshold or comparison context.

      :return: A string representation of the object, formatted as a satisfiability query for the concept and optionally the individual.

      :rtype: str



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Prepares the KnowledgeBase to handle the query by transforming it into an optimization problem and solving the resulting constraints. It first inspects the conclusion string for existential quantifiers, enabling dynamic blocking on the KnowledgeBase if specific patterns are found. A new semi-continuous variable is then introduced into the underlying MILP solver to serve as the objective target. The method updates the internal variable counter, sets the objective expression to minimize this new variable, and adds a constraint linking the negated conclusion to the variable's degree. Finally, it triggers the immediate solving of the accumulated assertions.

      :param kb: The KnowledgeBase object that encapsulates the MILP solver, manages variable and assertion state, and controls solving behavior.
      :type kb: KnowledgeBase



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Attempts to solve the minimal satisfiable query by optimizing the provided knowledge base. The method modifies the input knowledge base by incrementing its binary variable counter and creates a clone of the base, optionally excluding the ABox based on configuration or the presence of a specific individual. If no individual is currently assigned, a new one is generated within the cloned context. The process involves solving the ABox (if applicable), preprocessing the data, and executing an optimization routine against the objective expression. The resulting solution value is enforced to be non-negative. In the event of an inconsistent ontology, the method catches the exception and returns a solution indicating inconsistency. Additionally, the method tracks and updates the internal timing statistics for the operation.

      :param kb: The knowledge base defining the ontology and constraints for the optimization problem.
      :type kb: KnowledgeBase

      :return: A Solution object representing the optimal value found for the objective expression. If the ontology is inconsistent, returns a Solution indicating an inconsistent knowledge base. The solution value is guaranteed to be non-negative.

      :rtype: Solution


