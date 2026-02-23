fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function
======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a trapezoidal membership function within the FuzzyOWL2 framework to model fuzzy sets with a flat top region.


Description
-----------


The software defines a geometric structure used to represent fuzzy sets where membership values rise linearly, plateau at a maximum, and then fall linearly. By inheriting from a base fuzzy datatype, it integrates into a larger ontology framework, allowing specific fuzzy intervals to be defined using four distinct floating-point coordinates. These coordinates determine the shape of the function, specifically the start of the rise, the beginning of the plateau, the end of the plateau, and the end of the fall. Accessor methods are provided to retrieve these geometric parameters, while a string representation method allows for easy debugging and logging of the function's current state.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function.TrapezoidalFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_trapezoidal_function_TrapezoidalFunction.png
       :alt: UML Class Diagram for TrapezoidalFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TrapezoidalFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_trapezoidal_function_TrapezoidalFunction.pdf
       :alt: UML Class Diagram for TrapezoidalFunction
       :align: center
       :width: 9.7cm
       :class: uml-diagram

       UML Class Diagram for **TrapezoidalFunction**

.. py:class:: TrapezoidalFunction(a: float, b: float, c: float, d: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.trapezoidal_function.TrapezoidalFunction
      :parts: 1
      :private-bases:


   This class models a trapezoidal membership function, a fundamental construct in fuzzy logic used to define a set with a flat top region where membership is complete. It is characterized by four floating-point parameters: the left endpoint `a`, the left peak `b`, the right peak `c`, and the right endpoint `d`. The function increases linearly from `a` to `b`, maintains a maximum membership value between `b` and `c`, and decreases linearly from `c` to `d`. To utilize this class, instantiate it with the four coordinates that define the specific trapezoidal shape required for the fuzzy set. As a subclass of `FuzzyDatatype`, it integrates into the FuzzyOWL2 framework to represent fuzzy data types with specific geometric boundaries.

   :param _a: The left endpoint of the trapezoidal membership function.
   :type _a: float
   :param _b: The left peak point of the trapezoidal membership function.
   :type _b: float
   :param _c: The right peak point of the trapezoidal membership function.
   :type _c: float
   :param _d: The right endpoint of the trapezoidal membership function.
   :type _d: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the trapezoidal function, formatted to resemble a constructor call. The string includes the function name followed by the six internal attributes—k1, k2, a, b, c, and d—that define the specific geometry of the trapezoid. This representation is useful for debugging and logging, providing a concise summary of the object's state without modifying the underlying data.

      :return: A string representation of the object, formatted as a function call containing the current parameter values.

      :rtype: str



   .. py:method:: get_a() -> float

      Returns the value of the internal attribute `_a`, which represents the first parameter defining the trapezoidal function's geometry. This parameter typically corresponds to the leftmost x-coordinate of the function's support or the point where the function begins to rise. The method performs a direct retrieval without modifying the object's state and returns the value as a float.

      :return: The current value of the attribute 'a'.

      :rtype: float



   .. py:method:: get_b() -> float

      Returns the value of the internal attribute `_b`, which represents the left boundary of the trapezoid's upper plateau. This method serves as a read-only accessor to retrieve the x-coordinate where the function stops increasing and reaches its maximum value. It does not modify the object's state or perform any calculations beyond returning the stored float.

      :return: The value of the attribute `_b`.

      :rtype: float



   .. py:method:: get_c() -> float

      Returns the value of the internal parameter `_c`, which represents the right endpoint of the trapezoid's top plateau. This value marks the transition point where the function's output stops being maximal and begins to decrease. As a getter method, it provides read-only access to this specific coordinate without altering the function's state.

      :return: The value of the attribute c.

      :rtype: float



   .. py:method:: get_d() -> float

      Returns the value of the parameter $d$, which defines the upper bound of the trapezoidal function's support. This value corresponds to the x-coordinate where the function's membership value returns to zero after the plateau. The method acts as a simple accessor for the internal `_d` attribute and does not modify the state of the object.

      :return: The current value of the _d attribute.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:attribute:: _c
      :type:  float


   .. py:attribute:: _d
      :type:  float

