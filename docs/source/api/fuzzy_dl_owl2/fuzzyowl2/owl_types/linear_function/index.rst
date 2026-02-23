fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function



.. ── LLM-GENERATED DESCRIPTION START ──

Extends the base fuzzy datatype to model a linear membership function used for defining fuzzy sets within the FuzzyOWL2 framework.


Description
-----------


It initializes with two floating-point parameters that define the slope and intercept of the line, establishing the mathematical relationship for calculating membership degrees. The design leverages inheritance to incorporate domain boundaries, specifically lower and upper limits, which constrain the range of the function. Read-only access to the coefficients is provided to maintain encapsulation, and a string representation is implemented to display the function alongside its domain parameters for debugging and logging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function.LinearFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_linear_function_LinearFunction.png
       :alt: UML Class Diagram for LinearFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LinearFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_linear_function_LinearFunction.pdf
       :alt: UML Class Diagram for LinearFunction
       :align: center
       :width: 7.2cm
       :class: uml-diagram

       UML Class Diagram for **LinearFunction**

.. py:class:: LinearFunction(a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function.LinearFunction
      :parts: 1
      :private-bases:


   This class models a linear membership function within the FuzzyOWL2 framework, serving as a specific implementation of a fuzzy datatype. It is defined by two primary parameters, `a` and `b`, which represent the left and right endpoints of the linear shape, respectively. These endpoints determine the slope and interval of the function, allowing it to calculate degrees of membership for values within a fuzzy set. While the constructor initializes the geometric endpoints, the class also utilizes lower and upper bounds (`k1` and `k2`) to fully define the domain of the linear function.

   :param _a: The left endpoint of the linear membership function.
   :type _a: float
   :param _b: The right endpoint of the linear membership function.
   :type _b: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the linear function instance, formatted as a function call containing the object's internal parameters. The output string displays the values of the attributes `_k1`, `_k2`, `_a`, and `_b` in sequence within the syntax `linear(...)`. This method is intended for display and debugging purposes and does not alter the state of the object.

      :return: A human-readable string representation of the object, formatted as 'linear(k1, k2, a, b)'.

      :rtype: str



   .. py:method:: get_a() -> float

      Returns the floating-point value representing the coefficient 'a' (slope) of the linear function. This accessor method retrieves the internal `_a` attribute without modifying the object's state. It assumes the object has been properly initialized with a valid numerical value for the coefficient.

      :return: The current value of the internal attribute `_a`.

      :rtype: float



   .. py:method:: get_b() -> float

      Returns the y-intercept of the linear function, corresponding to the constant term in the equation $y = mx + b$. This method provides read-only access to the internal `_b` attribute, ensuring that the value is retrieved without altering the object's state. The returned value is a float representing the point where the function crosses the y-axis.

      :return: The value of the attribute _b.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float

