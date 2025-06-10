fuzzy_dl_owl2.fuzzydl.query.subsumption_query
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.subsumption_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.subsumption_query.SubsumptionQuery


Module Contents
---------------

.. py:class:: SubsumptionQuery(c1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, s_type: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:attribute:: c1
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: c2
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None



   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType


