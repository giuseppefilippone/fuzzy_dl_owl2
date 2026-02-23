fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer
====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework.


Description
-----------


Software components within the FuzzyOWL2 framework utilize this implementation to model fuzzy concepts through a geometric triangular shape defined by three distinct numerical parameters. By inheriting from a base fuzzy modifier class, the logic establishes a specific membership function where the degree of truth increases linearly from a left endpoint to a central peak and then decreases linearly to a right endpoint. The design encapsulates these three floating-point values—representing the support start, the maximum membership point, and the support end—to allow for the precise calculation of membership degrees for a given concept. Encapsulation is further supported by accessor methods that retrieve the specific boundary and peak values, alongside a string representation that aids in debugging and logging by clearly displaying the modifier's configuration.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer.TriangularModifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_triangular_modifer_TriangularModifier.png
       :alt: UML Class Diagram for TriangularModifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TriangularModifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_triangular_modifer_TriangularModifier.pdf
       :alt: UML Class Diagram for TriangularModifier
       :align: center
       :width: 8.2cm
       :class: uml-diagram

       UML Class Diagram for **TriangularModifier**

.. py:class:: TriangularModifier(a: float, b: float, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_modifer.TriangularModifier
      :parts: 1
      :private-bases:


   This class implements a triangular membership function used to define fuzzy modifiers within the FuzzyOWL2 framework. It models the degree of membership using a geometric shape defined by three specific parameters: a left endpoint representing the start of the support, a peak point indicating maximum membership, and a right endpoint marking the end of the support. Instances of this class are created by providing these three float values, which collectively determine the specific characteristics of the fuzzy modification applied to a concept.

   :param _a: The left endpoint of the triangular membership function.
   :type _a: float
   :param _b: The peak point of the triangular membership function.
   :type _b: float
   :param _c: The right endpoint of the triangular membership function.
   :type _c: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the current instance, formatted to display the internal parameters of the triangular modification. The output string follows the pattern "triangular-modifier(a, b, c)", incorporating the values of the private attributes `_a`, `_b`, and `_c`. This representation is useful for logging, debugging, or displaying the object's state in a user-friendly format without altering the object itself.

      :return: A human-readable string representation of the object, formatted as "triangular-modifier(a, b, c)".

      :rtype: str



   .. py:method:: get_a() -> float

      Returns the value of the internal attribute `_a`, which likely represents a specific parameter of the triangular modification, such as a boundary or coordinate. This method serves as a simple accessor and does not modify the state of the object. It assumes the instance has been properly initialized; otherwise, accessing the underlying attribute may raise an `AttributeError`.

      :return: The value of the internal attribute 'a'.

      :rtype: float



   .. py:method:: get_b() -> float

      Retrieves the value of the internal attribute `_b`, which typically represents the mode or upper limit parameter of the triangular distribution. This method serves as a simple accessor, returning the stored floating-point value without performing any calculations or modifying the object's state. It assumes the instance has been properly initialized, as it directly exposes the underlying private attribute.

      :return: The value of the attribute b.

      :rtype: float



   .. py:method:: get_c() -> float

      Returns the value of the internal parameter 'c' for the triangular modifier. This accessor method retrieves the floating-point number stored in the private attribute `_c` without causing any side effects or altering the object's state.

      :return: The value of the 'c' attribute.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:attribute:: _c
      :type:  float

