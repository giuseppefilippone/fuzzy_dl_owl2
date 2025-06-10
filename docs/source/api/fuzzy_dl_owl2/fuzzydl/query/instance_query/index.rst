fuzzy_dl_owl2.fuzzydl.query.instance_query
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.instance_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.instance_query.InstanceQuery


Module Contents
---------------

.. py:class:: InstanceQuery(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, individual: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.query.Query`, :py:obj:`abc.ABC`


   Instance checking query


   .. py:attribute:: conc
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: ind
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: obj_expr
      :type:  fuzzy_dl_owl2.fuzzydl.milp.expression.Expression
      :value: None



