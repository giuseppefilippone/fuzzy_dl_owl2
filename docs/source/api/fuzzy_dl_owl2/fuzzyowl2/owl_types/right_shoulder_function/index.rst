fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function
=========================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class representing a right shoulder fuzzy membership function used to model concepts where membership increases linearly to a maximum value.


Description
-----------


Extending the base fuzzy datatype, the implementation models a specific type of membership function where values below a certain threshold possess zero membership while values above a second threshold achieve full membership. Between these two boundary points, the degree of membership increases linearly, creating a sloped transition that effectively represents linguistic concepts such as "high" or "large" within a fuzzy ontology. The design stores these defining parameters as floating-point attributes to facilitate the calculation of membership degrees and supports integration into the broader FuzzyOWL2 framework through inheritance. Additionally, the logic includes a string representation mechanism that formats the object's configuration alongside inherited parameters, ensuring consistent output for debugging or serialization purposes.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function.RightShoulderFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_right_shoulder_function_RightShoulderFunction.png
       :alt: UML Class Diagram for RightShoulderFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RightShoulderFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_right_shoulder_function_RightShoulderFunction.pdf
       :alt: UML Class Diagram for RightShoulderFunction
       :align: center
       :width: 7.2cm
       :class: uml-diagram

       UML Class Diagram for **RightShoulderFunction**

.. py:class:: RightShoulderFunction(a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.right_shoulder_function.RightShoulderFunction
      :parts: 1
      :private-bases:


   This class models a fuzzy membership function characterized by a "right shoulder" shape, typically used to represent concepts where values greater than a certain threshold have full membership. It is designed for use within the FuzzyOWL2 framework and extends the base `FuzzyDatatype`. The function is defined by two parameters, `a` and `b`, which establish the interval where the degree of membership linearly increases from zero to one; values below `a` have zero membership, while values at or above `b` have full membership.

   :param _a: The left endpoint of the right shoulder membership function.
   :type _a: float
   :param _b: The right endpoint of the right shoulder membership function.
   :type _b: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the right-shoulder function instance, formatted to display the specific parameters defining the function's shape. The output follows the pattern "right-shoulder(k1, k2, a, b)", where the placeholders are replaced by the actual values of the internal attributes. This representation is useful for logging, debugging, or displaying the object's configuration in a concise manner.

      :return: A string representation of the object in the format 'right-shoulder(k1, k2, a, b)'.

      :rtype: str



   .. py:method:: get_a() -> float

      Retrieves the value of the internal parameter 'a' for the RightShoulderFunction instance. This method acts as a getter for the private attribute `_a`, returning the float value that defines a specific characteristic of the function's shape or position.

      :return: The value of a.

      :rtype: float



   .. py:method:: get_b() -> float

      Returns the value of the parameter 'b' for the right shoulder function. This method serves as an accessor for the internal attribute `_b`, which typically defines a specific boundary or slope point within the function's definition. The operation has no side effects and simply returns the stored floating-point value.

      :return: The value of the attribute b.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float

