fuzzy_dl_owl2.fuzzydl.query.instance_query
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.instance_query



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class provides a framework for querying the membership degree of a specific individual within a given concept.


Description
-----------


Extending the generic ``Query`` interface, this abstract class establishes a structural foundation for evaluating how strongly a specific individual belongs to a particular concept. It enforces a strict design constraint by validating that the provided concept is abstract, raising an error if a concrete concept is supplied, which ensures that only appropriate data types are processed during instance retrieval. During initialization, the component stores the target concept and individual as attributes while initializing an expression placeholder intended to represent the degree of membership. This architecture allows subclasses to focus on populating the expression with specific logic for identifying instances with minimum or maximum membership degrees without needing to re-implement the validation or storage mechanisms.

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


