fuzzy_dl_owl2.fuzzydl.milp.solution
===================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.milp.solution


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.milp.solution.Solution


Module Contents
---------------

.. py:class:: Solution(consistent: bool)
              Solution(sol: float)

   .. py:method:: __hash__() -> int


   .. py:method:: __repr__() -> str


   .. py:method:: __str__() -> str


   .. py:method:: add_showed_variable(var_name: str, value: float) -> None

      Sets the value of a showed variable.



   .. py:method:: get_showed_variables() -> dict[str, float]

      Gets the values of some variables after solving a query over a consistent KB.



   .. py:method:: get_solution() -> Union[bool, float]

      Gets the solution to some query over a consistent KB.



   .. py:method:: is_consistent_kb() -> bool

      Indicates whether the original KB is consistent or not.



   .. py:attribute:: CONSISTENT_KB
      :type:  bool
      :value: True



   .. py:attribute:: INCONSISTENT_KB
      :type:  bool
      :value: False



