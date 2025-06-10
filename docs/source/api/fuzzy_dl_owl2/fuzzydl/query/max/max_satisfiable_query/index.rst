fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.query.max.max_satisfiable_query.MaxSatisfiableQuery


Module Contents
---------------

.. py:class:: MaxSatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)
              MaxSatisfiableQuery(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.query.satisfiable_query.SatisfiableQuery`


   Maximal satisfiability degree of a fuzzy concept.


   .. py:method:: __str__() -> str

      Solves the query over a fuzzy KB



   .. py:method:: preprocess(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> None

      Performs some preprocessing steps of the query over a fuzzy KB.



   .. py:method:: solve(kb: fuzzy_dl_owl2.fuzzydl.knowledge_base.KnowledgeBase) -> fuzzy_dl_owl2.fuzzydl.milp.solution.Solution

      Solve the query using given knowledge base



