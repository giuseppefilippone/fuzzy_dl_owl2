fuzzy_dl_owl2.fuzzydl.query.instance_query
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.instance_query



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that defines a framework for querying the membership degree of a specific individual relative to a given concept.


Description
-----------


It serves as a foundational component within a fuzzy description logic system, specifically designed to handle queries that determine the extent to which an individual belongs to a concept. By inheriting from the abstract base class, it enforces a strict validation rule during initialization that prevents the use of concrete concepts, ensuring that only abstract concepts are processed for instance retrieval. The structure stores the provided concept and individual as core attributes while reserving a placeholder for an expression object, which subclasses are expected to populate to represent the specific membership degree logic. This design facilitates the creation of specialized queries, such as those seeking minimum or maximum membership degrees, by providing a consistent interface and validation mechanism for all derived implementations.

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


