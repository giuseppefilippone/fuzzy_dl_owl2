fuzzy_dl_owl2.fuzzydl.concept.operator_concept
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.operator_concept


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.And
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.GoedelAnd
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.GoedelOr
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.LukasiewiczAnd
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.LukasiewiczOr
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.Not
   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.Or


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.operator_concept.OperatorConcept


Module Contents
---------------

.. py:class:: OperatorConcept(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, concepts: Iterable[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concepts_interface.HasConceptsInterface`


   Defines a logic operator concept defined as AND, OR or NOT of concepts.


   .. py:method:: __and__(value: Self) -> Self


   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __ne__(value: Self) -> bool


   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: __or__(value: Self) -> Self


   .. py:method:: and_(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: clone() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: compute_name() -> Optional[str]


   .. py:method:: de_morgan() -> Self


   .. py:method:: distribute(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> Self


   .. py:method:: get_atom() -> Optional[Self]


   .. py:method:: get_atoms() -> list[Self]


   .. py:method:: get_clauses(is_type: Callable) -> list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]


   .. py:method:: get_roles() -> set[str]


   .. py:method:: goedel_and(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: goedel_or(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: is_and(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> bool
      :staticmethod:



   .. py:method:: is_atomic() -> bool


   .. py:method:: is_complemented_atomic() -> bool


   .. py:method:: is_concrete() -> bool


   .. py:method:: is_not_at_least_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_at_most_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_choquet(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_concrete(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_exact_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_ext_neg_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_ext_pos_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_fuzzy_number(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_goedel_implies(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_has_value(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_modified(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_neg_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_owa(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_pos_threshold(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_qowa(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_quasi_sugeno(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_self(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_sigma_concept(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_sugeno(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_type(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> bool
      :staticmethod:



   .. py:method:: is_not_weighted(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_weighted_max(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_weighted_min(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_weighted_sum(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_weighted_sum_zero(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_not_zadeh_implies(op: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> bool
      :staticmethod:



   .. py:method:: is_or(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType) -> bool
      :staticmethod:



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



   .. py:method:: lukasiewicz_and(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: lukasiewicz_or(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: normal_form(is_type: Callable) -> Self


   .. py:method:: not_(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: or_(*concepts: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :staticmethod:



   .. py:method:: reduce_double_negation() -> Self


   .. py:method:: reduce_idempotency(is_type: Callable) -> Self


   .. py:method:: reduce_quantifiers() -> Self


   .. py:method:: reduce_truth_values() -> Self


   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: ABSORPTION_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: ALL_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: AND_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: BINARY_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: COMPLEMENT_LAW_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: DISTRIBUTIVE_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: OPERATORS
      :type:  dict[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:attribute:: OR_OPERATORS
      :type:  list[fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType]


   .. py:property:: concepts
      :type: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]



   .. py:attribute:: name
      :value: '(and )'



   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


.. py:data:: And

.. py:data:: GoedelAnd

.. py:data:: GoedelOr

.. py:data:: LukasiewiczAnd

.. py:data:: LukasiewiczOr

.. py:data:: Not

.. py:data:: Or

