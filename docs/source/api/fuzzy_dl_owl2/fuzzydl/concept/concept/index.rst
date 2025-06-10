fuzzy_dl_owl2.fuzzydl.concept.concept
=====================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concept


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
   fuzzy_dl_owl2.fuzzydl.concept.concept.Thing


Module Contents
---------------

.. py:class:: Concept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType = ConceptType.ATOMIC, name: str = '')

   Bases: :py:obj:`Thing`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __iand__(value: Self) -> Self


   .. py:method:: __ior__(value: Self) -> Self


   .. py:method:: __irshift__(value: Self) -> Self


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: __rshift__(value: Self) -> Self


   .. py:method:: __str__() -> str


   .. py:method:: is_atomic() -> bool


   .. py:method:: is_complemented_atomic() -> bool


   .. py:attribute:: DEFAULT_NAME
      :value: 'Concept@'



   .. py:attribute:: SPECIAL_STRING
      :value: '@'



   .. py:property:: name
      :type: str



   .. py:attribute:: num_new_concepts
      :value: 1



   .. py:property:: type
      :type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType



.. py:class:: Thing

   Bases: :py:obj:`abc.ABC`


   Helper class that provides a standard way to create an ABC using
   inheritance.


   .. py:method:: __eq__(value: Self) -> bool
      :abstractmethod:



   .. py:method:: __ge__(value: Self) -> Self


   .. py:method:: __gt__(value: Self) -> Self


   .. py:method:: __invert__() -> Self


   .. py:method:: __le__(value: Self) -> Self


   .. py:method:: __lt__(value: Self) -> Self


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __neg__() -> Self
      :abstractmethod:



   .. py:method:: __repr__() -> str


   .. py:method:: classic_cnf() -> Self


   .. py:method:: classic_dnf() -> Self


   .. py:method:: clone() -> Self
      :abstractmethod:



   .. py:method:: compute_atomic_concepts() -> set[Self]
      :abstractmethod:



   .. py:method:: compute_name() -> Optional[str]
      :abstractmethod:



   .. py:method:: contains_negated_subconcept(v: list[Self], cj: Self) -> int
      :staticmethod:



   .. py:method:: contains_subconcept(v: list[Self], cj: Self) -> bool
      :staticmethod:



   .. py:method:: de_morgan() -> Self


   .. py:method:: distribute(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> Self


   .. py:method:: get_atomic_concepts() -> set[Self]


   .. py:method:: get_atomic_concepts_names() -> set[str]


   .. py:method:: get_atoms() -> list[Self]


   .. py:method:: get_clauses(is_type: Callable) -> list[Self]


   .. py:method:: get_roles() -> set[str]
      :abstractmethod:



   .. py:method:: goedel_cnf() -> Self


   .. py:method:: goedel_dnf() -> Self


   .. py:method:: has_nominals() -> bool


   .. py:method:: is_concrete() -> bool


   .. py:method:: is_simplified() -> bool

      This function check if current formula is simplified, i.e., if:
          - The only negated elements are literal of kind (~ A), where A is an AtomicProposition
          - The OR operator is between:
              - Two literals => A | B
              - One literal and a AND => A | (B & C) - (A & B) | C
              - Two (or more) OR => (A & B) | (C & D) | (E & F)
          - The AND operator is between:
              - Two literals => A & B
              - One literal and a OR => A & (B | C) - (A | B) & C
              - Two (or more) AND => (A | B) & (C | D) & (E | F)
          - The only operators are AND, OR and NOT



   .. py:method:: lukasiewicz_cnf() -> Self


   .. py:method:: lukasiewicz_dnf() -> Self


   .. py:method:: normal_form(is_type: Callable) -> Self


   .. py:method:: reduce_double_negation() -> Self


   .. py:method:: reduce_idempotency(is_type: Callable) -> Self


   .. py:method:: reduce_quantifiers() -> Self


   .. py:method:: reduce_truth_values() -> Self


   .. py:method:: remove_element(v: list[Self], i: int) -> None
      :staticmethod:



   .. py:method:: replace(a: Self, c: Self) -> Optional[Self]
      :abstractmethod:



