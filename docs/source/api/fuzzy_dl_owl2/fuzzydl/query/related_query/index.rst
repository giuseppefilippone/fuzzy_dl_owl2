fuzzy_dl_owl2.fuzzydl.query.related_query
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.related_query



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class defining the structure for queries that evaluate role assertions and relationships between individuals within a fuzzy description logic framework.


Description
-----------


It serves as a foundational interface for evaluating the entailment of role assertions, specifically focusing on the relationships between individuals. Designed to support operations that determine minimum or maximum degrees of membership, it acts as a shared structure for more specific query implementations. The implementation encapsulates the necessary parameters for these evaluations, including the specific role being examined, the subject and object individuals involved in the relation, and an expression representing the desired degree of membership. By defining these attributes, it provides a standardized way to construct and process queries regarding the strength or validity of connections within a logical framework.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_related_query_RelatedQuery.png
       :alt: UML Class Diagram for RelatedQuery
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RelatedQuery**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_query_related_query_RelatedQuery.pdf
       :alt: UML Class Diagram for RelatedQuery
       :align: center
       :width: 11.2cm
       :class: uml-diagram

       UML Class Diagram for **RelatedQuery**

.. py:class:: RelatedQuery

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery
      :parts: 1
      :private-bases:


   This abstract class serves as a foundational interface for queries that evaluate the entailment of role assertions, specifically focusing on the relationships between individuals. It is designed to support operations that determine minimum or maximum degrees of membership, acting as a shared structure for more specific query implementations. The class encapsulates the parameters necessary for these evaluations, including the specific role being examined, the subject and object individuals involved in the relation, and an expression representing the desired degree of membership. By defining these attributes, it provides a standardized way to construct and process queries regarding the strength or validity of connections within a logical framework.

   :param role: The role or relation type for which related individuals are retrieved.
   :type role: str
   :param ind1: The individual acting as the subject of the relation.
   :type ind1: Individual
   :param ind2: The individual acting as the object of the role assertion relation.
   :type ind2: Individual
   :param obj_expr: The objective expression representing the degree of membership of the relation.
   :type obj_expr: Expression


   .. py:attribute:: ind1
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual
      :value: None



   .. py:attribute:: ind2
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual
      :value: None



   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None



   .. py:attribute:: role
      :type:  str
      :value: None


