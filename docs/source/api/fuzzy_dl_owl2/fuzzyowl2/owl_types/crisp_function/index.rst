fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.crisp_function







.. ── LLM-GENERATED DESCRIPTION START ──

A crisp function datatype for the FuzzyOWL2 framework that stores two numeric coefficients and renders itself as a ``crisp(...)`` expression bounded by inherited interval limits.


Description
-----------


The ``CrispFunction`` class extends the ``FuzzyDatatype`` base type so that exact, non-fuzzy mathematical constraints can be represented alongside genuinely fuzzy datatypes inside a fuzzy OWL 2 ontology. Instances are deliberately lightweight value objects: the constructor stores the two coefficients ``a`` and ``b`` as private floats, and a pair of simple getters exposes them without offering any way to mutate them, which keeps the datatype predictable wherever ontology terms are shared. A notable design decision is the split of responsibility with the superclass — the string representation formats the result as ``crisp(k1, k2, a, b)``, pulling the lower and upper bounds from inherited attributes rather than duplicating interval logic in the subclass. That human-readable output doubles as a serialisation-friendly form, allowing crisp constraints to be embedded directly into generated ontology markup or inspected during debugging. Together these pieces make the class a small but essential bridge between precise, classical logic and the broader fuzzy modelling framework.

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