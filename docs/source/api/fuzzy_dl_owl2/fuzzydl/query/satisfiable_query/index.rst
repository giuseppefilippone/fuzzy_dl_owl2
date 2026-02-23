fuzzy_dl_owl2.fuzzydl.query.satisfiable_query
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

A base class representing min/max satisfiability queries for fuzzy concepts within a logic framework.


Description
-----------


Designed to function as an abstract interface, the software evaluates the degree to which a specific fuzzy concept is satisfied, optionally within the context of a particular individual. Strict validation rules ensure that the target concept is not concrete, thereby maintaining logical consistency during the evaluation process. Method overloading supports flexible initialization, allowing queries to be constructed with just a concept or with both a concept and an individual. Internal state management stores the relevant concept, individual, and a placeholder for the resulting objective expression, preparing the groundwork for subsequent satisfiability checks and bound calculations.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.satisfiable_query.SatisfiableQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_satisfiable_query_SatisfiableQuery.png
       :alt: UML Class Diagram for SatisfiableQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SatisfiableQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_satisfiable_query_SatisfiableQuery.pdf
       :alt: UML Class Diagram for SatisfiableQuery
       :align: center
       :width: 12.0cm
       :class: uml-diagram

       UML Class Diagram for **SatisfiableQuery**

.. py:class:: SatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)
              SatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.satisfiable_query.SatisfiableQuery
      :parts: 1
      :private-bases:


   This abstract class serves as the foundational interface for min/max satisfiability queries within a fuzzy logic framework. It is designed to evaluate the degree to which a specific fuzzy concept is satisfied, optionally in the context of a particular individual. Upon initialization, the class requires a non-concrete concept and accepts an optional individual argument, storing these entities along with a placeholder for the resulting objective expression. By enforcing constraints on the input concept and providing a common structure for storing query parameters, it facilitates the implementation of specific satisfiability checks that determine the bounds or extent of concept fulfillment.


   .. py:method:: __satisfiable_query_init_1(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual) -> None

      Initializes a satisfiability query designed to evaluate whether a specific individual satisfies a given fuzzy concept. This method assigns the provided concept and individual to the instance attributes `self.conc` and `self.ind`, respectively, while setting the objective expression to None. It performs a validation step to ensure the concept is not concrete, raising an error if the input violates this constraint. This setup prepares the query object for subsequent satisfiability testing operations involving the specified individual.

      :param c: The fuzzy concept to be tested for satisfiability. Must not be a concrete concept.
      :type c: Concept
      :param a: The individual entity used during the satisfiability test.
      :type a: Individual



   .. py:method:: __satisfiable_query_init_2(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Initializes the query object to test the general satisfiability of a given fuzzy concept. This method serves as an alternative constructor that delegates to the primary initialization routine, passing `None` as the secondary argument to indicate that the check is not bound to a specific individual or context. By invoking the main initialization logic with these parameters, it configures the internal state necessary to determine if the concept is logically consistent within the current knowledge base.

      :param c: The fuzzy concept to be checked for satisfiability.
      :type c: Concept


