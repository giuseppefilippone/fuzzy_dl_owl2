fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class defines the structure for fuzzy datatypes characterized by a lower and an upper bound within the FuzzyOWL2 framework.


Description
-----------


The class establishes a foundational structure for representing fuzzy intervals by managing two primary attributes that correspond to the minimum and maximum values of the range. By initializing these boundaries to zero by default, the implementation provides a neutral state that concrete subclasses can modify to define specific fuzzy logic behaviors. Accessor and mutator methods are provided to retrieve and modify these internal values, allowing for dynamic adjustment of the interval's shape and support without enforcing strict validation logic during assignment. Designed for extensibility, the abstract nature of the class ensures that specific fuzzy set implementations can inherit this boundary management logic while defining their own operational semantics.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_fuzzy_datatype_FuzzyDatatype.png
       :alt: UML Class Diagram for FuzzyDatatype
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyDatatype**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_fuzzy_datatype_FuzzyDatatype.pdf
       :alt: UML Class Diagram for FuzzyDatatype
       :align: center
       :width: 7.2cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyDatatype**

.. py:class:: FuzzyDatatype

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_datatype.FuzzyDatatype
      :parts: 1
      :private-bases:


   This abstract base class serves as a foundational component for representing fuzzy datatypes within the FuzzyOWL2 framework, specifically defining a range characterized by a lower and an upper bound. It manages two primary attributes, `k1` and `k2`, which correspond to the minimum and maximum values of the fuzzy interval, respectively. Intended to be subclassed, it provides getter and setter methods to manipulate these boundaries, allowing concrete implementations to define specific fuzzy logic behaviors based on these parameters. By default, the bounds are initialized to zero, providing a neutral starting state for derived classes.

   :param _k1: The lower bound of the fuzzy datatype.
   :type _k1: float
   :param _k2: The upper bound of the fuzzy datatype.
   :type _k2: float


   .. py:method:: __repr__() -> str

      Returns the official string representation of the `FuzzyDatatype` instance by delegating to the `__str__` method. This implementation ensures that the output used for debugging and logging is identical to the informal string representation, prioritizing human readability over a strictly unambiguous or executable Python expression.

      :return: A string representation of the object.

      :rtype: str



   .. py:method:: get_max_value() -> float

      Returns the upper bound or maximum value defining the range of this fuzzy datatype. This method accesses the internal `_k2` attribute, which typically represents the rightmost point of the support or core in fuzzy logic representations. The operation is a simple accessor and does not modify the state of the object.

      :return:

      :rtype: float



   .. py:method:: get_min_value() -> float

      Retrieves the minimum value defining the support of the fuzzy number, corresponding to the internal attribute `_k1`. This value represents the lower bound of the range where the membership function is non-zero. The method performs a direct retrieval without modifying the object's state and returns the value as a float.

      :return: The minimum value associated with the instance.

      :rtype: float



   .. py:method:: set_max_value(max: float) -> None

      Updates the upper bound parameter of the fuzzy datatype by assigning the provided float value to the internal `_k2` attribute. This method mutates the object's state in place, altering the definition of the fuzzy set's range or shape. It does not perform validation to ensure the new maximum is greater than the minimum value, so users must ensure logical consistency to avoid invalid configurations.

      :param max: The maximum value to set.
      :type max: float



   .. py:method:: set_min_value(min: float) -> None

      Assigns the specified floating-point value to the internal attribute `_k1`, effectively defining the lower bound or starting parameter for the fuzzy data type. This method directly mutates the instance's state without performing validation on the input type or logical consistency with other parameters. It returns `None`, indicating that the operation is performed solely for its side effect of updating the object's configuration.

      :param min: The new minimum value to be assigned.
      :type min: float



   .. py:attribute:: _k1
      :type:  float
      :value: 0.0



   .. py:attribute:: _k2
      :type:  float
      :value: 0.0


