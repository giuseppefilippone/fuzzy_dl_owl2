fuzzy_dl_owl2.fuzzydl.concept.sigma_count
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.sigma_count


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.sigma_count.SigmaCount


Module Contents
---------------

.. py:class:: SigmaCount(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, inds: list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual], role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   Sigma-count pending tasks.


   .. py:method:: __hash__() -> int


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:method:: get_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:method:: get_role() -> str


   .. py:method:: get_variable() -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: individual
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: individuals
      :type:  list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:attribute:: role
      :type:  str


   .. py:attribute:: variable
      :type:  fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


