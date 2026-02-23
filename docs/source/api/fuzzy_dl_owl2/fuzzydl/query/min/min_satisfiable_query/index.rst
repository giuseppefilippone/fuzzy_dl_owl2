fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.min.min_satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

Calculates the minimal degree to which a fuzzy concept is satisfiable, either generally or for a specific individual, by transforming the logical problem into a Mixed-Integer Linear Programming optimization task.


Description
-----------


The implementation extends the base satisfiability logic to function as a minimization problem, where the goal is to find the lowest truth value for a given concept within a fuzzy description logic ontology. By cloning the knowledge base before execution, the process prevents unintended side effects on the original data structure while allowing for optional inclusion or exclusion of the ABox based on configuration settings. To handle complex logical constructs, the system detects existential quantifiers to enable dynamic blocking and introduces a semi-continuous variable into the solver that serves as the objective for the optimization. The final solution is derived by minimizing this variable under constraints that link the negation of the concept to the variable's degree, with error handling in place to manage inconsistent ontologies and ensure the result is non-negative.

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
       :width: 12.0cm
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


