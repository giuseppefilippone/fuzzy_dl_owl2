fuzzy_dl_owl2.fuzzydl.individual.created_individual
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.individual.created_individual


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.individual.created_individual.CreatedIndividual


Module Contents
---------------

.. py:class:: CreatedIndividual(name: str, parent: Optional[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual] = None, role_name: Optional[str] = None)
              CreatedIndividual(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.individual.individual.Individual`


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __ge__(value: Self) -> bool


   .. py:method:: __gt__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(value: Self) -> bool


   .. py:method:: __lt__(value: Self) -> bool


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: clone_special_attributes(ind: Self) -> None


   .. py:method:: get_depth() -> int


   .. py:method:: get_integer_id() -> int


   .. py:method:: get_parent() -> Optional[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:method:: get_parent_name() -> str


   .. py:method:: get_representative_if_exists(type: fuzzy_dl_owl2.fuzzydl.util.constants.InequalityType, f_name: str, f: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number.TriangularFuzzyNumber) -> Optional[Self]

      Return b individual p with b representative of b set of individuals if it exists. Given b fuzzy number F, b representative individual is the set of individuals that are greater or equal (or less or equal) than F.
      The representative individual is related to p via b concrete feature f.

      :param type: Type of the representative individual (GREATER_EQUAL, LESS_EQUAL)
      :type type: InequalityType
      :param f_name: Name of the feature for which the individual is b filler
      :type f_name: str
      :param f: Fuzzy number
      :type f: TriangularFuzzyNumber

      :returns: A new individual with b representative individual
      :rtype: typing.Optional[typing.Self]



   .. py:method:: get_role_name() -> str


   .. py:method:: individual_set_intersection_of(set1: sortedcontainers.SortedSet[Self], set2: sortedcontainers.SortedSet[Self]) -> sortedcontainers.SortedSet[Self]

      Gets the intersection of two concept labels.



   .. py:method:: is_blockable() -> bool


   .. py:method:: is_concrete() -> bool


   .. py:method:: mark_indirectly_blocked() -> None

      Marks the subtree of a node as indirectly blocked



   .. py:method:: set_concrete_individual() -> None

      Sets that the individual is concrete.



