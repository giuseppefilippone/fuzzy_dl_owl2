fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a triangular membership function for fuzzy logic ontologies by defining geometric parameters for shape calculation.


Description
-----------


A triangular membership function is modeled to represent vague or imprecise concepts within fuzzy logic systems by defining a specific geometric shape. Inheriting from a base fuzzy datatype allows the logic to integrate into the FuzzyOWL2 framework, enabling ontological reasoners to process constraints and sets defined by imprecise boundaries. The shape of the function is determined by three floating-point parameters representing the left endpoint, the peak, and the right endpoint, which are stored as private attributes to maintain encapsulation. Accessor methods expose these geometric values for external use, while a custom string representation offers a concise summary of the object's configuration for debugging or logging.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function.TriangularFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_triangular_function_TriangularFunction.png
       :alt: UML Class Diagram for TriangularFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **TriangularFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_triangular_function_TriangularFunction.pdf
       :alt: UML Class Diagram for TriangularFunction
       :align: center
       :width: 8.2cm
       :class: uml-diagram

       UML Class Diagram for **TriangularFunction**

.. py:class:: TriangularFunction(a: float, b: float, c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.triangular_function.TriangularFunction
      :parts: 1
      :private-bases:


   This class models a triangular membership function, which is commonly used in fuzzy logic systems to define vague or imprecise concepts. It is characterized by three specific points: the left endpoint where the membership degree begins to increase, the peak point where the membership degree reaches its maximum, and the right endpoint where the membership degree returns to zero. Inheriting from FuzzyDatatype, it serves as a concrete implementation within the FuzzyOWL2 framework, enabling the representation of fuzzy sets and constraints in ontological reasoning. To utilize this class, instantiate it with three floating-point numbers corresponding to these geometric parameters to define the shape and support of the fuzzy region.

   :param _a: The left endpoint of the triangular membership function.
   :type _a: float
   :param _b: The peak point of the triangular membership function.
   :type _b: float
   :param _c: The right endpoint of the triangular membership function.
   :type _c: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the triangular function instance, formatted to resemble a constructor call. The output string explicitly lists the values of the internal parameters `_k1`, `_k2`, `_a`, `_b`, and `_c`, providing a concise summary of the object's configuration. This method has no side effects and relies on the string conversion of the internal attributes; it is primarily used for debugging, logging, or displaying the object to the user.

      :return: A string representation of the object, formatted as a constructor call displaying the current values of the parameters.

      :rtype: str



   .. py:method:: get_a() -> float

      Retrieves the value of the internal attribute `_a`, which typically represents the lower bound or the first vertex defining the shape of the triangular function. This method provides read-only access to the parameter without modifying the object's state. It assumes that `_a` has been properly initialized as a float during the object's construction.

      :return: The value of the internal attribute `_a`.

      :rtype: float



   .. py:method:: get_b() -> float

      Retrieves the value of the internal parameter `_b`, which typically represents the peak or center point of the triangular function. This method serves as a simple accessor and returns the value as a float without modifying the object's state. The validity of the returned value depends on the initialization of the `TriangularFunction` instance.

      :return: The value of the `_b` attribute.

      :rtype: float



   .. py:method:: get_c() -> float

      Returns the value of the internal attribute `_c`, which serves as a key parameter defining the shape or range of the triangular function. As a standard accessor method, it provides read-only access to this configuration value without inducing any side effects or altering the object's state. The method guarantees that the parameter is returned as a float, ensuring compatibility with numerical operations performed by the class.

      :return: The value of the internal attribute `_c`.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float


   .. py:attribute:: _c
      :type:  float

