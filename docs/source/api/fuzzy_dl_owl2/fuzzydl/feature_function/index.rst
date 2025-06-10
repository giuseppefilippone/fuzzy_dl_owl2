fuzzy_dl_owl2.fuzzydl.feature_function
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.feature_function


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.feature_function.FeatureFunction


Module Contents
---------------

.. py:class:: FeatureFunction(feature: Self)
              FeatureFunction(feature: str)
              FeatureFunction(n: float)
              FeatureFunction(feature: list[Self])
              FeatureFunction(feature1: Self, feature2: Self)
              FeatureFunction(n: float, feature: Self)

   Function involving several features.


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: get_features() -> set[str]

      Gets an array of features that take part in the function.



   .. py:method:: get_number() -> float


   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.FeatureFunctionType


   .. py:method:: to_expression(a: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, milp: fuzzy_dl_owl2.fuzzydl.milp.milp_helper.MILPHelper) -> Optional[fuzzy_dl_owl2.fuzzydl.milp.expression.Expression]

      Gets an array of features that take part in the function.



