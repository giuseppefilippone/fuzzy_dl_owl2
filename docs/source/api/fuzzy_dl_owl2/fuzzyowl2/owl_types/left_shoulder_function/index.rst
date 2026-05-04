fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function
========================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized data structure representing a left-shoulder membership function for fuzzy logic systems where membership values decrease as input values increase.


Description
-----------


It models concepts where membership is high for low values and drops as values rise, utilizing two floating-point parameters to establish the transition zone where the membership grade shifts from one to zero. Inheritance from a base fuzzy datatype allows the implementation to utilize inherited bounds to define the overall domain of the fuzzy set. Access to the defining parameters is provided through a string representation that aids in debugging and logging within the broader fuzzy logic framework.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function.LeftShoulderFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_left_shoulder_function_LeftShoulderFunction.png
       :alt: UML Class Diagram for LeftShoulderFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LeftShoulderFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_left_shoulder_function_LeftShoulderFunction.pdf
       :alt: UML Class Diagram for LeftShoulderFunction
       :align: center
       :width: 7.2cm
       :class: uml-diagram

       UML Class Diagram for **LeftShoulderFunction**

.. py:class:: LeftShoulderFunction(a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.left_shoulder_function.LeftShoulderFunction
      :parts: 1
      :private-bases:


   Represents a left-shoulder membership function used in fuzzy logic systems, such as FuzzyOWL2, to model concepts where membership is high for low values and decreases as values increase. To use this class, instantiate it with two floating-point parameters, `a` and `b`, which define the start and end of the transition zone where the membership value drops from 1 to 0. The function relies on bounds `k1` and `k2`, inherited from the parent `FuzzyDatatype`, to define the overall domain of the fuzzy set.

   :param _a: The left endpoint of the left-shoulder membership function.
   :type _a: float
   :param _b: The right endpoint of the left-shoulder membership function.
   :type _b: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the function instance, formatted to display its defining parameters. The output follows the pattern "left-shoulder(k1, k2, a, b)", where the values correspond to the internal attributes `_k1`, `_k2`, `_a`, and `_b`. This representation is primarily used for logging, debugging, and display purposes, and it does not modify the state of the object.

      :return: A string representation of the object, formatted as a function call with the current parameters.

      :rtype: str



   .. py:method:: get_a() -> float

      Retrieves the numeric value of the 'a' parameter, which defines a specific characteristic of the left shoulder function's shape. This method acts as a simple accessor for the private attribute `_a`, returning its current value without performing any calculations or validation. The operation is read-only and has no side effects on the object's state.

      :return: The current value of the attribute 'a'.

      :rtype: float



   .. py:method:: get_b() -> float

      Returns the value of the internal parameter `_b`, which represents a specific boundary or configuration point for the left shoulder function. This method acts as a read-only accessor, retrieving the stored floating-point value without modifying the object's state or causing any side effects.

      :return: The value of the internal attribute _b.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float

