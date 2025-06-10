fuzzy_dl_owl2.fuzzydl.primitive_concept_definition
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition


Module Contents
---------------

.. py:class:: PrimitiveConceptDefinition(defined: str, definition: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, implication: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, degree: float)

   General concept inclusion axiom.


   .. py:method:: __eq__(other: Self) -> bool


   .. py:method:: __ge__(other: Self) -> bool


   .. py:method:: __gt__(other: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __le__(other: Self) -> bool


   .. py:method:: __lt__(other: Self) -> bool


   .. py:method:: __ne__(other: Self) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_defined_concept() -> str


   .. py:method:: get_definition() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:method:: get_degree() -> float


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType


   .. py:method:: set_definition(definition: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None


   .. py:method:: set_degree(deg: float) -> None


   .. py:attribute:: defined
      :type:  str


   .. py:attribute:: definition
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: degree
      :type:  float


   .. py:attribute:: implication
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType


