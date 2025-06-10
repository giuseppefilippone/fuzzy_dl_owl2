fuzzy_dl_owl2.fuzzydl.milp.variable
===================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.variable


Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.variable.BinaryVar
   fuzzy_dl_owl2.fuzzydl.milp.variable.FreeVar
   fuzzy_dl_owl2.fuzzydl.milp.variable.IntegerVar
   fuzzy_dl_owl2.fuzzydl.milp.variable.UpVar


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.variable.Variable


Module Contents
---------------

.. py:class:: Variable(name: str, v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType)

   .. py:method:: __eq__(value: Self) -> bool


   .. py:method:: __hash__() -> int


   .. py:method:: __ne__(value: object) -> bool


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: clone() -> Self


   .. py:method:: get_binary_variable(name: str) -> Self
      :staticmethod:



   .. py:method:: get_continuous_variable(name: str) -> Self
      :staticmethod:



   .. py:method:: get_datatype_filler_type() -> bool


   .. py:method:: get_integer_variable(name: str) -> Self
      :staticmethod:



   .. py:method:: get_lower_bound() -> float


   .. py:method:: get_new_variable(v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> Self
      :staticmethod:



   .. py:method:: get_semi_continuous_variable(name: str) -> Self
      :staticmethod:



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.VariableType


   .. py:method:: get_upper_bound() -> float


   .. py:method:: set_binary_variable() -> None


   .. py:method:: set_datatype_filler_variable() -> None


   .. py:method:: set_name(name: str) -> None


   .. py:method:: set_type(v_type: fuzzy_dl_owl2.fuzzydl.util.constants.VariableType) -> None


   .. py:attribute:: VARIABLE_NAME
      :type:  str
      :value: 'y'



   .. py:attribute:: VARIABLE_NUMBER
      :type:  int
      :value: 0



   .. py:attribute:: datatype_filler
      :type:  bool
      :value: False



   .. py:attribute:: lower_bound
      :type:  float
      :value: 0.0



   .. py:attribute:: name
      :type:  str


   .. py:attribute:: type
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.VariableType
      :value: None



   .. py:attribute:: upper_bound
      :type:  float
      :value: 0.0



.. py:data:: BinaryVar

.. py:data:: FreeVar

.. py:data:: IntegerVar

.. py:data:: UpVar

