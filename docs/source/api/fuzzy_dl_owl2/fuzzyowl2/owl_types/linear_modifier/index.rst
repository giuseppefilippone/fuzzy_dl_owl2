fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier



.. ── LLM-GENERATED DESCRIPTION START ──

A fuzzy logic modifier that applies a linear transformation to membership degrees using a specific coefficient.


Description
-----------


Extending the base fuzzy modifier functionality, this implementation handles linear transformations required to scale or adjust membership degrees within the FuzzyOWL2 framework. The logic encapsulates a single floating-point coefficient that defines the specific linear operation, ensuring that the mathematical parameter is stored securely and remains accessible for reasoning tasks. By inheriting from the parent class, the design integrates seamlessly into the broader hierarchy while providing a distinct string representation that clearly identifies the modifier type and its associated value. This approach allows for precise manipulation of fuzzy set semantics through a simple, coefficient-based model.

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

