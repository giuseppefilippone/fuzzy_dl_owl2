fuzzy_dl_owl2.fuzzydl.primitive_concept_definition
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.primitive_concept_definition







.. ── LLM-GENERATED DESCRIPTION START ──

A primitive concept definition axiom for fuzzy description logics, binding a named concept to a complex fuzzy concept expression through a chosen fuzzy implication operator and a lower-bound truth degree.


Description
-----------


``PrimitiveConceptDefinition`` represents a specialised form of general concept inclusion axiom in a fuzzy ontology: it states that a named (primitive) concept is defined by, or subsumed under, a complex fuzzy concept description. Each axiom carries four pieces of state — the name of the concept being defined, the ``Concept`` expression that defines it, the fuzzy implication operator (such as Łukasiewicz, Gödel, or Product) that determines how the inclusion is interpreted, and a degree between 0 and 1 acting as a lower bound on the truth of the relationship. Reasoners consult these axioms when propagating membership degrees through a knowledge base, so the object serves both as a syntactic statement and as a parameter record for the inference engine.

Behaviour is that of a mutable value object. Accessor methods expose and allow replacement of the defining expression and the degree, while a clone operation produces an independent copy so axioms can be safely duplicated and reworked inside a knowledge base. Equality is fully structural — two axioms match only when all four components match — and the hash is derived from those same components, keeping instances usable in sets and dictionaries. Ordering is defined in terms of hash values rather than any semantic criterion, which yields a consistent but arbitrary total order, and comparisons against objects of other types simply return false instead of raising an error.

Two performance decisions reflect intended use on very large knowledge bases. The canonical string form is built lazily and cached after first access, since the same axiom tends to be rendered and hashed repeatedly during reasoning, and the repr simply reuses that cached string. Separately, a module-level lookup table precomputes the first character of each implication operator's name so that rendering never touches the enum's name descriptor, which profiling had identified as a measurable hotspot — roughly a second of cumulative time across hundreds of thousands of calls on a knowledge base containing over a million concepts.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.primitive_concept_definition._IMPL_CHAR


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.primitive_concept_definition.PrimitiveConceptDefinition


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_primitive_concept_definition_PrimitiveConceptDefinition.png
       :alt: UML Class Diagram for PrimitiveConceptDefinition
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **PrimitiveConceptDefinition**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_primitive_concept_definition_PrimitiveConceptDefinition.pdf
       :alt: UML Class Diagram for PrimitiveConceptDefinition
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **PrimitiveConceptDefinition**

.. py:class:: PrimitiveConceptDefinition(defined: str, definition: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, implication: fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, degree: float)

   This class represents a primitive concept definition within a fuzzy logic system, functioning as a specific type of general concept inclusion axiom. It encapsulates a rule where a named concept is defined by or implies a complex fuzzy concept description, utilizing a specific fuzzy implication operator (such as Łukasiewicz or Gödel) to determine the logical connection. The axiom includes a degree of truth, a float value between 0 and 1, which acts as a lower bound representing the extent to which the definition satisfies the concept. Users can construct instances to define these logical relationships, retrieve or modify the definition and degree via accessor methods, and leverage comparison and cloning utilities for managing axioms within a knowledge base.

   :param defined: The name of the primitive concept being defined by this axiom.
   :type defined: str
   :param definition: The fuzzy concept expression that defines the primitive concept.
   :type definition: Concept
   :param degree: The lower bound of the axiom, representing the extent to which the primitive concept is satisfied by the definition.
   :type degree: float
   :param implication: Specifies the fuzzy logic operator (e.g., Łukasiewicz, Gödel, Product) used to interpret the implication relationship within the axiom.
   :type implication: LogicOperatorType


   .. py:method:: __eq__(other: Self) -> bool

      Determines whether the current instance is equal to another object by comparing their structural components. The method returns true only if the provided argument is an instance of the same class and if the `defined`, `definition`, `degree`, and `implication` attributes of both objects match exactly. If the other object is of a different type, the method returns false, and no side effects occur during the comparison.

      :param other: The object to compare against for equality.
      :type other: typing.Self

      :return: True if the other object is an instance of PrimitiveConceptDefinition and all attributes (defined, definition, degree, implication) are equal, otherwise False.

      :rtype: bool



   .. py:method:: __ge__(other: Self) -> bool

      Determines whether the current instance is greater than or equal to another instance of the same type. This comparison is implemented by negating the result of the less-than operation, effectively delegating the logic to the `__lt__` method. As a result, the specific ordering rules and handling of incompatible types are defined by the implementation of the less-than operator, and this method itself introduces no side effects.

      :param other: The object to compare against, which must be an instance of the same class.
      :type other: typing.Self

      :return: True if the instance is greater than or equal to the other instance, False otherwise.

      :rtype: bool



   .. py:method:: __gt__(other: Self) -> bool

      Determines if the current instance is greater than the provided object by comparing their hash values. This method strictly enforces type compatibility, returning False if the other object is not an instance of PrimitiveConceptDefinition rather than raising a TypeError. The comparison logic relies solely on the result of the built-in hash function, meaning the ordering is determined by the integer hash values of the instances.

      :param other: The object to compare against the current instance based on hash values.
      :type other: typing.Self

      :return: True if `other` is an instance of `PrimitiveConceptDefinition` and the hash of the current instance is greater than the hash of `other`; otherwise, False.

      :rtype: bool



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __le__(other: Self) -> bool

      Determines whether the current instance is less than or equal to another instance of the same type. The implementation delegates to the greater-than comparison operator, returning `True` if `self` is not greater than `other`. Consequently, the behavior and validity of this comparison depend entirely on the implementation of the `__gt__` method, and any exceptions raised by that method will be propagated.

      :param other: The object to compare against the current instance.
      :type other: typing.Self

      :return: True if the object is less than or equal to the other object, otherwise False.

      :rtype: bool



   .. py:method:: __lt__(other: Self) -> bool

      Determines whether the current instance is considered less than the provided object by comparing their hash values. The method returns `True` only if the `other` argument is an instance of `PrimitiveConceptDefinition` and the hash of the current instance is strictly less than the hash of the `other` instance. If `other` is not an instance of this class, or if the hash of the current instance is greater than or equal to that of `other`, the method returns `False`.

      :param other: The object to compare against, expected to be an instance of the same class.
      :type other: typing.Self

      :return: True if the other object is an instance of PrimitiveConceptDefinition and the hash of this instance is less than the hash of the other object; otherwise, False.

      :rtype: bool



   .. py:method:: __ne__(other: Self) -> bool

      Determines whether the current instance is not equal to another object of the same type. This method implements the inequality operator by returning the logical negation of the equality comparison, effectively delegating the specific logic to the `__eq__` method. It performs no side effects or state mutations, and its behavior regarding type compatibility depends entirely on the implementation of the equality check.

      :param other: The instance to compare against for inequality.
      :type other: typing.Self

      :return: True if the current instance is not equal to the other object, False otherwise.

      :rtype: bool



   .. py:method:: __repr__() -> str

      Returns the official string representation of the `PrimitiveConceptDefinition` instance. This method delegates directly to the `__str__` method, meaning the output is identical to the informal string representation. As a result, the representation provided is primarily intended for display and debugging, relying on the formatting logic defined within the string conversion implementation.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the primitive concept definition, formatted to display the logical relationship between the defined concept and its definition. The representation includes the defined concept, the first character of the implication relation's name, the definition text, and the associated degree, structured as `Defined =>_Implication Definition >= Degree`. This method is side-effect free, though it assumes the implication name is not empty to prevent index errors during string formatting.

      :return: A human-readable string representation of the object, displaying its defined status, implication name, definition, and degree.

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `PrimitiveConceptDefinition` that is a distinct copy of the current object. The new instance is initialized with the exact same values for the `defined`, `definition`, `implication`, and `degree` attributes as the original. This operation does not modify the state of the original object, allowing the clone to be manipulated independently.

      :return: A new instance of the class with identical attribute values to the current instance.

      :rtype: typing.Self



   .. py:method:: get_defined_concept() -> str

      Retrieves the specific concept string associated with this definition instance. This method acts as a direct accessor for the internal `defined` attribute, returning the stored value without performing any validation or transformation. It does not modify the state of the object.

      :return: The defined concept associated with the object.

      :rtype: str



   .. py:method:: get_definition() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the `Concept` object that defines this primitive concept instance. This method provides access to the internal `definition` attribute, allowing callers to retrieve the specific concept associated with this definition wrapper. It is a read-only operation with no side effects on the instance itself, though the returned `Concept` object may be mutable depending on its implementation.

      :return: The definition of the object, represented as a Concept.

      :rtype: Concept



   .. py:method:: get_degree() -> float

      Returns the floating-point value representing the degree associated with this definition. This method serves as a simple accessor for the internal `degree` attribute, providing the current numeric value without altering the object's state. It relies on the attribute being initialized prior to invocation to ensure a valid float is returned.

      :return: The degree value associated with the object.

      :rtype: float



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType

      Retrieves the specific logical operator type associated with this primitive concept definition. This method returns the value stored in the `implication` attribute, which represents the underlying logical classification or relationship. The operation is read-only and does not modify the state of the object.

      :return: Returns the specific logic operator type associated with the instance.

      :rtype: LogicOperatorType



   .. py:method:: set_definition(definition: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> None

      Assigns the provided `Concept` object to the `definition` attribute of the instance, thereby updating the core data held by the `PrimitiveConceptDefinition`. This method mutates the object's state by replacing any existing reference with the new value. It returns `None` as the operation is performed in place.

      :param definition: The Concept instance to assign as the definition.
      :type definition: Concept



   .. py:method:: set_degree(deg: float) -> None

      Assigns the specified floating-point value to the degree attribute of the primitive concept definition. This method updates the internal state of the instance by overwriting the existing `degree` property with the new value provided in the `deg` argument. It performs no return operation and directly modifies the object in place.

      :param deg: The new degree value.
      :type deg: float



   .. py:attribute:: _name
      :type:  Optional[str]
      :value: None



   .. py:attribute:: defined
      :type:  str


   .. py:attribute:: definition
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: degree
      :type:  float


   .. py:attribute:: implication
      :type:  fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType


.. py:data:: _IMPL_CHAR
   :type:  Dict[fuzzy_dl_owl2.fuzzydl.util.constants.LogicOperatorType, str]