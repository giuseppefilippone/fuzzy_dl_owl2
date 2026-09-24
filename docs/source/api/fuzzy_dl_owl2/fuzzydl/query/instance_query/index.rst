fuzzy_dl_owl2.fuzzydl.query.instance_query
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.instance_query





.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class for fuzzy description-logic queries that determine the degree to which a specific individual is an instance of a given concept, typically to find minimum or maximum membership degrees.


Description
-----------


InstanceQuery anchors a family of graded-membership queries in a fuzzy description-logic reasoner, where an individual's belonging to a concept is a matter of degree rather than a simple yes-or-no fact. It extends a generic query abstraction and enforces a key modelling constraint at construction time: the supplied concept must be abstract, and passing a concrete (datatype-style) concept raises an error, since graded membership is only meaningful for abstract concepts. The concept and individual are kept as state, while a placeholder for a linear expression is deliberately left empty for subclasses to populate; once the query has been compiled into a mixed-integer linear program, that expression encodes the individual's degree of membership in the concept. By deferring both the expression construction and the solving logic to concrete subclasses, the design allows variants such as minimum- and maximum-degree queries to share validation and state management while specialising only the reasoning machinery.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_instance_query_InstanceQuery.png
       :alt: UML Class Diagram for InstanceQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **InstanceQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_instance_query_InstanceQuery.pdf
       :alt: UML Class Diagram for InstanceQuery
       :align: center
       :width: 11.4cm
       :class: uml-diagram

       UML Class Diagram for **InstanceQuery**

.. py:class:: InstanceQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery
      :parts: 1
      :private-bases:


   This abstract base class defines a framework for querying specific instances of a concept relative to a particular individual, typically used to identify instances with minimum or maximum membership degrees. Upon initialization, it accepts a concept and an individual, validating that the concept is abstract and raising an error if a concrete concept is provided. It maintains an expression attribute to represent the degree of membership, which is intended to be populated by subclasses to facilitate the specific query logic.

   :param conc: The concept for which to retrieve the instance.
   :type conc: Concept
   :param ind: The individual for which to retrieve the instance.
   :type ind: Individual
   :param obj_expr: Expression representing the degree of membership of the individual to the concept.
   :type obj_expr: Expression


   .. py:attribute:: conc
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: ind
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None

