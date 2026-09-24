fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_function







.. ── LLM-GENERATED DESCRIPTION START ──

A linear membership function datatype for the FuzzyOWL2 fuzzy ontology framework, characterised by two floating-point coefficients that determine the line's slope and position when assigning degrees of membership.


Description
-----------


``LinearFunction`` is one of the concrete membership-function shapes that the FuzzyOWL2 framework supports, and it specialises the generic ``FuzzyDatatype`` base so that linear functions can be handled polymorphically alongside other shapes such as triangular, trapezoidal, or Gaussian ones. Its geometry is captured by two private floating-point coefficients, ``a`` and ``b``, which the accompanying documentation reads in two complementary ways — as the left and right endpoints of the linear shape, or as the slope and intercept of the line f(x) = ax + b — and either way, these two numbers are what determine how strongly a value belongs to a fuzzy set. Encapsulation is kept deliberately minimal: the coefficients are stored as private attributes and exposed only through read-only accessors, so the rest of the framework can inspect a function's parameters during serialisation or reasoning without any risk of altering them. The human-readable rendering follows the compact ``linear(k1, k2, a, b)`` notation, in which the lower and upper domain bounds ``k1`` and ``k2`` are expected to be supplied by the superclass rather than being initialised locally, an inherited dependency that ties the display format to the broader datatype hierarchy and would fail at runtime if the base class did not provide those bounds. That notation is intended for display, debugging, and export of the fuzzy ontology, giving a concise summary of the function's full parameterisation in a form that is easy for both humans and downstream tooling to parse.

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