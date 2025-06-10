fuzzy_dl_owl2.fuzzydl.query.related_query
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.related_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.related_query.RelatedQuery


Module Contents
---------------

.. py:class:: RelatedQuery

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`, :py:obj:`abc.ABC`


   Entailment of a role assertion query


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



