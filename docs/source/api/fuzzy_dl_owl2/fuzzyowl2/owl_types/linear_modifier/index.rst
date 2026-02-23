fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class that applies linear transformations to fuzzy logic membership degrees within the FuzzyOWL2 framework.


Description
-----------


Extending the base functionality of fuzzy modifiers, this implementation introduces a linear transformation mechanism designed to scale or adjust membership degrees. The core logic relies on a single floating-point coefficient provided during instantiation, which dictates the intensity or nature of the linear adjustment applied to fuzzy values. By encapsulating this coefficient as a private attribute, the design ensures that the transformation parameter remains consistent and accessible only through specific accessor methods. Furthermore, the implementation includes a string representation that clearly identifies the modifier type and its associated coefficient, facilitating easier debugging and logging within the broader system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier.LinearModifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_linear_modifier_LinearModifier.png
       :alt: UML Class Diagram for LinearModifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LinearModifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_linear_modifier_LinearModifier.pdf
       :alt: UML Class Diagram for LinearModifier
       :align: center
       :width: 5.3cm
       :class: uml-diagram

       UML Class Diagram for **LinearModifier**

.. py:class:: LinearModifier(c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier.LinearModifier
      :parts: 1
      :private-bases:


   Represents a specific type of fuzzy logic modifier that applies a linear transformation, typically used to scale or adjust membership degrees within the FuzzyOWL2 framework. To utilize this entity, instantiate it with a floating-point value that serves as the coefficient for the linear operation. Once instantiated, the coefficient can be retrieved using the provided accessor method, and the object provides a string representation indicating its type and value.

   :param _c: The numeric coefficient defining the linear transformation applied by the modifier.
   :type _c: float


   .. py:method:: __str__() -> str

      Returns the informal string representation of the `LinearModifier` instance, which is intended to be readable and concise. The output is formatted as "linear-modifier({c})", where {c} represents the string conversion of the internal coefficient stored in `_c`. This method does not alter the state of the object and is implicitly called by the built-in `str()` function and print operations.

      :return: A string representation of the linear modifier, formatted as 'linear-modifier(c)' where c is the coefficient.

      :rtype: str



   .. py:method:: get_c() -> float

      Retrieves the constant term 'c' currently stored in the linear modifier. This method returns the value of the private attribute `_c` as a floating-point number. It is a read-only operation that does not modify the object's state or have any side effects.

      :return: The value of the internal attribute `_c`.

      :rtype: float



   .. py:attribute:: _c
      :type:  float

