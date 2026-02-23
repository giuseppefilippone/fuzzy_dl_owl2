fuzzy_dl_owl2.fuzzydl.concrete_feature
======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concrete_feature



.. ── LLM-GENERATED DESCRIPTION START ──

A data structure representing a typed attribute with optional numeric bounds, supporting string, boolean, integer, and real types.


Description
-----------


The implementation defines a data model for attributes that possess a specific name and a data type, which can be a string, boolean, integer, or real number. During instantiation, the logic automatically determines the appropriate type by inspecting the provided arguments, where a single name implies a string, a boolean flag sets the type explicitly, and numeric pairs define integer or real ranges. Internal state management relies on private initialization methods that configure the feature's boundaries and classification, ensuring that numeric types store lower and upper bounds while non-numeric types do not. Functionality includes the ability to clone instances to create independent copies, modify the type or range constraints after creation, and retrieve the feature's identifier or classification for use in broader logic.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concrete_feature.ConcreteFeature


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concrete_feature_ConcreteFeature.png
       :alt: UML Class Diagram for ConcreteFeature
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConcreteFeature**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concrete_feature_ConcreteFeature.pdf
       :alt: UML Class Diagram for ConcreteFeature
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConcreteFeature**

.. py:class:: ConcreteFeature(name: str)
              ConcreteFeature(name: str, is_boolean: bool)
              ConcreteFeature(name: str, k1: int, k2: int)
              ConcreteFeature(name: str, k1: float, k2: float)

   This class models a specific attribute of an individual, characterized by a name and a data type such as string, boolean, integer, or real. The type is automatically determined during initialization based on the provided arguments: supplying only a name defaults to a string type, passing a boolean flag explicitly sets the type to boolean, and providing numeric bounds (`k1` and `k2`) defines an integer or real range. It supports accessing and modifying the feature's type and numeric boundaries, as well as cloning the instance to create an independent copy.

   :raises ValueError: Raised when the arguments provided during initialization are invalid, such as having an incorrect number of arguments or types that do not match the expected signature for a boolean or numeric feature.


   .. py:method:: __concrete_feature_init_1(name: str) -> None

      Initializes the `ConcreteFeature` instance with a specific name and default configuration for range constraints and data type. This method assigns the provided string to the `name` attribute, sets the lower and upper bounds (`k1` and `k2`) to `None`, and explicitly sets the feature type to `ConcreteFeatureType.STRING`. It directly mutates the instance's state, effectively resetting any pre-existing values for the bounds and type, and is intended for use when creating features that do not initially require numeric range definitions.

      :param name: The name of the concrete feature.
      :type name: str



   .. py:method:: __concrete_feature_init_2(name: str, is_boolean: bool) -> None

      Initializes the feature instance by delegating the assignment of the feature's name to the primary initialization method, `__concrete_feature_init_1`. This method accepts a string for the name and a boolean flag to determine the feature's data type. If the `is_boolean` flag is set to True, the instance's type attribute is explicitly set to `ConcreteFeatureType.BOOLEAN`; if the flag is False, the type attribute remains in whatever state it was left by the preceding initialization call. This process mutates the instance's state in-place.

      :param name: The name or identifier of the feature.
      :type name: str
      :param is_boolean: Flag indicating whether the feature type should be set to BOOLEAN.
      :type is_boolean: bool



   .. py:method:: __concrete_feature_init_3(name: str, k1: int, k2: int) -> None

      Initializes the feature as an integer type defined by a specific range between two bounds. It delegates the assignment of the feature's name to the `__concrete_feature_init_1` method, then sets the `k1` attribute as the lower bound and the `k2` attribute as the upper bound. This method modifies the instance's state by setting the `type` attribute to `ConcreteFeatureType.INTEGER`, though it does not perform validation to ensure that the lower bound is less than the upper bound.

      :param name: The identifier or label for the feature.
      :type name: str
      :param k1: The lower bound for the range.
      :type k1: int
      :param k2: Upper bound for the range.
      :type k2: int



   .. py:method:: __concrete_feature_init_4(name: str, k1: float, k2: float) -> None

      Initializes a concrete feature instance representing a real-valued variable with a specified name and numerical range. The `k1` and `k2` parameters define the lower and upper bounds of the feature's domain, respectively. This method explicitly sets the feature type to `REAL` and delegates the initialization of the name attribute to a separate internal routine.

      :param name: Identifier for the feature.
      :type name: str
      :param k1: The lower bound for the feature's value range.
      :type k1: float
      :param k2: The upper bound for the range.
      :type k2: float



   .. py:method:: __repr__() -> str

      Returns the official string representation of the instance by delegating to the object's `__str__` method. This implementation ensures that the output of `repr()` is identical to the informal string representation provided by `str()`. Because it relies on `__str__`, the behavior and format of the output are determined by that method, and a failure to define `__str__` could lead to a recursion error.

      :return: A string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the informal string representation of the feature instance. This implementation delegates the formatting logic to the `get_name` method, effectively using the feature's name as its primary identifier when converted to a string. It is automatically invoked by the built-in `str()` function and print statements.

      :return: The name of the object.

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a new instance that duplicates the current object's configuration, ensuring the returned copy is independent of the original. The initialization logic adapts based on the feature's underlying type: boolean features are reconstructed with a specific flag, string features are initialized solely by name, and other types are instantiated using the name along with primary and secondary key values. This method does not modify the state of the existing instance.

      :return: A new instance of the class that is a copy of the current object, preserving its name and type-specific attributes.

      :rtype: typing.Self



   .. py:method:: get_k1() -> Optional[Union[float, int]]

      Returns the current value of the `k1` attribute stored within the instance. The method provides access to a numeric parameter that may be represented as either an integer or a float, or it may return None if the value is undefined or null. Since this is a getter method, it performs no side effects or modifications to the object's internal state.

      :return: The value of the k1 attribute.

      :rtype: typing.Optional[typing.Union[float, int]]



   .. py:method:: get_k2() -> Optional[Union[float, int]]

      Retrieves the current value of the `k2` attribute associated with the `ConcreteFeature` instance. The returned value can be a numeric type, specifically an integer or a float, depending on how the attribute was originally set. If the attribute is uninitialized or explicitly set to `None`, the method returns `None`. This is a read-only accessor function that does not alter the object's state or produce any side effects.

      :return: The value of the `k2` attribute, which may be an integer, a float, or None.

      :rtype: typing.Optional[typing.Union[float, int]]



   .. py:method:: get_name() -> str

      Returns the name of the feature instance. This method provides direct access to the internal `name` attribute, which serves as the identifier for the feature. It is a read-only operation that does not modify the state of the object, though it will raise an `AttributeError` if the underlying attribute has not been initialized.

      :return: The name associated with the object instance.

      :rtype: str



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.ConcreteFeatureType

      Returns the specific type classification associated with the feature instance. This method acts as a simple accessor for the internal `type` attribute, providing the `ConcreteFeatureType` that defines the nature of the object. It does not modify the instance state and has no side effects.

      :return: The concrete feature type associated with the instance.

      :rtype: ConcreteFeatureType



   .. py:method:: set_range(k1: Optional[Union[float, int]], k2: Optional[Union[float, int]]) -> None

      Updates the range boundaries for the feature by assigning the provided values to the instance attributes. The parameters `k1` and `k2` can be integers, floats, or None, allowing for partial or unset range definitions. This method directly mutates the object's state without performing validation on the relative order or magnitude of the inputs.

      :param k1: The starting value or lower bound of the range. Can be a number or None to indicate an unbounded start.
      :type k1: typing.Optional[typing.Union[float, int]]
      :param k2: The upper bound or end value of the range, or None to indicate no upper bound.
      :type k2: typing.Optional[typing.Union[float, int]]



   .. py:method:: set_type(new_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConcreteFeatureType) -> None

      Updates the type definition of the feature instance to the specified value, replacing the existing type attribute. This method mutates the object's state by directly assigning the provided `ConcreteFeatureType` to the internal `type` property. It does not return a value and assumes the input is a valid type definition compatible with the feature's schema.

      :param new_type: The concrete feature type to assign to the instance.
      :type new_type: ConcreteFeatureType


