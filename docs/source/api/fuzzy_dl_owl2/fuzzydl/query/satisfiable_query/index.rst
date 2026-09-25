fuzzy_dl_owl2.fuzzydl.query.satisfiable_query
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.satisfiable_query



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class, **SatisfiableQuery**, that prepares fuzzy satisfiability queries by validating and storing a fuzzy concept, an optional individual, and a placeholder objective expression for later minimum/maximum satisfiability evaluation.


Description
-----------


SatisfiableQuery extends the generic Query abstraction to provide the shared foundation for minimum and maximum satisfiability checks in a fuzzy description-logic setting. Its role is to capture the common inputs of such queries — a fuzzy concept and an optional individual — while deferring the actual solving logic to concrete subclasses, which determine the bounds or the extent to which the concept is fulfilled. Because satisfiability is only meaningful for abstract concepts, initialization rejects concrete concepts with an error message, guaranteeing that only valid fuzzy concepts proceed to the reasoning stage.

The constructor emulates Java-style constructor overloading: ``typing.overload`` declarations advertise two accepted signatures (a concept alone, or a concept paired with an individual), while the variadic implementation checks the argument count and types through assertions before delegating to a private initializer. The single-argument path deliberately invokes that private two-argument initializer with ``None`` rather than re-entering ``__init__``, mirroring Java's ``this(c, null)`` idiom and preventing virtual dispatch into subclass constructors whose two-argument branch might reject ``None``. Once initialized, the query holds the concept, the optional individual, and a ``None``-valued objective expression drawn from the MILP layer, which concrete subclasses are expected to populate when the query is compiled into an optimization problem.

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

      Initializes the query object to test the general satisfiability of a given fuzzy concept. This method serves as an alternative constructor that delegates to the primary initialization routine, passing `None` as the secondary argument to indicate that the check is not bound to a specific individual or context. The private (name-mangled) initializer is called directly — mirroring Java's `this(c, null)` — instead of `self.__init__`, which would dispatch virtually into a subclass constructor whose two-argument branch may reject `None`.

      :param c: The fuzzy concept to be checked for satisfiability.
      :type c: Concept


