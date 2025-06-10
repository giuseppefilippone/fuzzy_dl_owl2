fuzzy_dl_owl2.fuzzydl.classification_node
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.classification_node


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.classification_node.ClassificationNode


Module Contents
---------------

.. py:class:: ClassificationNode(name: str)

   .. py:method:: __hash__() -> int


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: add_input_edge(node: Self, n: float) -> None


   .. py:method:: add_label(c: str) -> None


   .. py:method:: add_ouput_edge(node: Self, n: float) -> None


   .. py:method:: get_full_name() -> str


   .. py:method:: get_immediate_predecessors() -> set[Self]


   .. py:method:: get_immediate_successors() -> set[Self]


   .. py:method:: get_output_edges() -> dict[Self, float]


   .. py:method:: has_name(name: str) -> bool


   .. py:method:: is_nothing() -> bool


   .. py:method:: is_thing() -> bool


   .. py:method:: remove_input_edge(node: Self, n: float) -> None


   .. py:method:: remove_ouput_edge(node: Self, n: float) -> None


   .. py:attribute:: EQUIVALENT_NAMES
      :type:  set[str]


   .. py:attribute:: INPUT_EDGES
      :type:  dict[Self, float]


   .. py:attribute:: OUTPUT_EDGES
      :type:  dict[Self, float]


