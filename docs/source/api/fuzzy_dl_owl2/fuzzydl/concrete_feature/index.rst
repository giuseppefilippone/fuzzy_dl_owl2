fuzzy_dl_owl2.fuzzydl.concrete_feature
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concrete_feature


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature


Module Contents
---------------

.. py:class:: ConcreteFeature(name: str)
              ConcreteFeature(name: str, is_boolean: bool)
              ConcreteFeature(name: str, k1: int, k2: int)
              ConcreteFeature(name: str, k1: float, k2: float)

   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_k1() -> Optional[Union[float, int]]


   .. py:method:: get_k2() -> Optional[Union[float, int]]


   .. py:method:: get_name() -> str


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.ConcreteFeatureType


   .. py:method:: set_range(k1: Optional[Union[float, int]], k2: Optional[Union[float, int]]) -> None


   .. py:method:: set_type(new_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConcreteFeatureType) -> None


