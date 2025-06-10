fuzzy_dl_owl2.fuzzydl.individual.individual
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.individual.individual


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


Module Contents
---------------

.. py:class:: Individual(name: str)

   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: add_concept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: add_concrete_restriction(f_name: str, ass: fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion) -> None

      Adds a negated datatype restriction to the individual.



   .. py:method:: add_to_nominal_list(ind_name: str) -> None


   .. py:method:: clone() -> Self


   .. py:method:: clone_attributes(ind: Self) -> None


   .. py:method:: get_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: get_nominal_list() -> set[str]


   .. py:method:: get_representative_if_exists(type: fuzzy_dl_owl2.fuzzydl.util.constants.RepresentativeIndividualType, f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber)
      :abstractmethod:



   .. py:method:: is_blockable() -> bool


   .. py:method:: prune() -> None


   .. py:method:: set_label(ind_name: str) -> None


   .. py:method:: set_name(name: str) -> None


   .. py:attribute:: DEFAULT_NAME
      :type:  str
      :value: 'i'



   .. py:attribute:: concrete_role_restrictions
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.assertion.assertion.Assertion]]


   .. py:attribute:: fillers_to_show
      :type:  dict[str, set[str]]


   .. py:attribute:: list_of_concepts
      :type:  set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:attribute:: name
      :type:  str


   .. py:attribute:: nominal_list
      :type:  set[str]


   .. py:attribute:: not_self_roles
      :type:  set[str]
      :value: []



   .. py:attribute:: role_relations
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.relation.Relation]]


   .. py:attribute:: role_restrictions
      :type:  dict[str, list[fuzzy_dl_owl2.fuzzydl.restriction.restriction.Restriction]]


