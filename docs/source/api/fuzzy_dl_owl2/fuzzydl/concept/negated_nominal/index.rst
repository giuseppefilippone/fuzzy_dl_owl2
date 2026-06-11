fuzzy_dl_owl2.fuzzydl.concept.negated_nominal
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.negated_nominal



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a class representing the logical complement of a named individual within a fuzzy description logic framework.


Description
-----------


The software models a specific type of concept that represents the exclusion of a particular named individual from a domain, often utilized in range restrictions. By inheriting from the base ``Concept`` class, it establishes itself as an atomic concept type while storing the identifier of the individual being negated and generating a standardized string representation for that exclusion. Logical operations such as conjunction and disjunction are supported through delegation to an ``OperatorConcept`` utility, allowing these negated nominals to participate in complex expressions. However, the implementation enforces a strict constraint against double negation, raising an exception if an attempt is made to complement an already negated nominal, thereby preserving the integrity of the logical structure. Additionally, the implementation includes mechanisms for cloning instances and generating hash values based on structural identity to facilitate use in collections and comparisons.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.negated_nominal.NegatedNominal


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_negated_nominal_NegatedNominal.png
       :alt: UML Class Diagram for NegatedNominal
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **NegatedNominal**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_negated_nominal_NegatedNominal.pdf
       :alt: UML Class Diagram for NegatedNominal
       :align: center
       :width: 8.4cm
       :class: uml-diagram

       UML Class Diagram for **NegatedNominal**

.. py:class:: NegatedNominal(ind_name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.negated_nominal.NegatedNominal
      :parts: 1
      :private-bases:


   This class models a negated nominal concept within the framework of fuzzy description logic, specifically representing the complement of a named individual. It is designed to express constraints that exclude specific individuals from a domain, often utilized in range restrictions. To use it, instantiate the object with the name of the individual to be negated; the class automatically generates a standardized string representation for this exclusion. While it supports logical operations like conjunction and disjunction, it enforces a strict limitation where further negation is prohibited, raising an exception if such an operation is attempted.

   :param _ind_name: Internal storage for the identifier of the individual being negated, serving as the backing field for the public property.
   :type _ind_name: str
   :param name: The canonical string representation of the negated nominal, formatted as "(not { ind_name } )".
   :type name: str

   :raises FuzzyOntologyException: Raised when attempting to apply the negation operator to a NegatedNominal instance, as nested negation of nominals is not supported in fuzzy description logic.


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `NegatedNominal` class, enabling logical conjunction between two instances. This method accepts another `NegatedNominal` object as the right-hand operand and delegates the actual computation to the `OperatorConcept.and_` static method. The operation returns a new instance of `NegatedNominal` representing the result of the conjunction, ensuring type consistency with the operands.

      :param value: The other operand to perform the AND operation with, expected to be of the same type as the current instance.
      :type value: typing.Self

      :return: The result of the logical AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> Self

      Implements the unary negation operation for the nominal. However, since the instance already represents a negated concept, applying a further complement is not permitted by the underlying logic. Consequently, this method always raises a FuzzyOntologyException to enforce the constraint that negated nominals cannot be complemented.

      :raises FuzzyOntologyException: Raised when attempting to negate a negated nominal, as negated nominals cannot be complemented.

      :return: Raises FuzzyOntologyException indicating that negated nominals cannot be complemented.

      :rtype: typing.Self



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to combine the current instance with another `NegatedNominal` object. This method delegates the combination logic to `OperatorConcept.or_`, returning a new instance that represents the union or logical disjunction of the two operands. The operation is side-effect free, as it generates a new object rather than modifying the existing instances.

      :param value: The right-hand operand for the OR operation.
      :type value: typing.Self

      :return: Returns the result of the OR operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `NegatedNominal` that is a copy of the current object. The new instance is initialized with the same `ind_name` attribute as the original, ensuring logical equivalence while maintaining object identity separation. This method does not modify the existing instance or have any side effects on the original object's state.

      :return: A new instance of `NegatedNominal` initialized with the same individual name as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str | None

      Retrieves the name associated with the `NegatedNominal` instance. This method returns the value of the `name` attribute, which may be a string or `None` if no name has been assigned. It serves as a direct accessor without performing additional computation or modification of the instance state.

      :return: The name associated with the instance, or None if it is not set.

      :rtype: str | None



   .. py:attribute:: _ind_name
      :type:  str


   .. py:property:: ind_name
      :type: str


      Returns the name of the individual that this negated nominal excludes, i.e. the ``a`` in the concept ``(not {a})``. The value is read from the private ``_ind_name`` attribute without modifying the instance.

      :return: The name of the excluded individual.

      :rtype: str


   .. py:attribute:: name
      :type:  str
      :value: '(not { Uninferable } )'


