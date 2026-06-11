fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized datatype class that models crisp functions using linear coefficients to integrate precise mathematical logic into a fuzzy ontology framework.


Description
-----------


Extending the base fuzzy datatype allows for the definition of exact mathematical intervals or linear transformations within an otherwise fuzzy logic environment. The core functionality relies on two primary coefficients, initialized during object creation, which determine the specific characteristics of the crisp constraint being modeled. By encapsulating these parameters and exposing them through accessor methods, the software allows for the precise definition of non-fuzzy elements that interact with the broader ontology structure. The string representation further integrates these values with conceptual bounds, offering a clear textual format for debugging or display purposes that reflects the underlying mathematical definition.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function.CrispFunction


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_crisp_function_CrispFunction.png
       :alt: UML Class Diagram for CrispFunction
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **CrispFunction**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_crisp_function_CrispFunction.pdf
       :alt: UML Class Diagram for CrispFunction
       :align: center
       :width: 7.2cm
       :class: uml-diagram

       UML Class Diagram for **CrispFunction**

.. py:class:: CrispFunction(a: float, b: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function.CrispFunction
      :parts: 1
      :private-bases:


   This class represents a crisp function within the FuzzyOWL2 framework, acting as a specialized fuzzy datatype to model precise mathematical intervals or linear transformations. It is characterized by two primary coefficients, `a` and `b`, which are supplied during instantiation, and it is conceptually bounded by lower and upper limits, `k1` and `k2`. Users can employ this class to define crisp constraints in fuzzy ontologies by initializing it with the required parameters, and the object exposes these values through getter methods while providing a string representation that includes the bounds. It serves as a fundamental building block for integrating non-fuzzy, exact logic into a broader fuzzy system.

   :param _a: The first parameter of the crisp function.
   :type _a: float
   :param _b: The second parameter defining the crisp function.
   :type _b: float


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the `CrispFunction` instance, formatted to resemble a function invocation. The string includes the values of the internal parameters `_k1`, `_k2`, `_a`, and `_b` enclosed in parentheses and prefixed by 'crisp'. This method is intended for display and debugging purposes; it does not modify the object's state and relies on the string representations of the underlying attributes.

      :return: Returns a string representation of the object, displaying the current parameter values.

      :rtype: str



   .. py:method:: get_a() -> float

      Retrieves the value of the internal attribute `_a`, which represents a specific parameter or coefficient of the crisp function. The method returns this value as a float and does not modify the state of the object. If the internal attribute has not been initialized, the method will raise an AttributeError.

      :return: Returns the value of the attribute `a`.

      :rtype: float



   .. py:method:: get_b() -> float

      Retrieves the value of the internal attribute `_b` associated with the function instance. This method serves as a getter to expose the specific parameter, likely representing a coefficient or offset, without modifying the object's state. The returned value is a floating-point number, assuming the attribute has been initialized during the object's construction.

      :return: The value of the _b attribute.

      :rtype: float



   .. py:attribute:: _a
      :type:  float


   .. py:attribute:: _b
      :type:  float

