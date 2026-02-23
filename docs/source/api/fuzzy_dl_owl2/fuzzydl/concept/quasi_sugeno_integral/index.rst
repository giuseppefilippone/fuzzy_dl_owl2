fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Quasi-Sugeno integral aggregation operator that combines fuzzy concepts with specific weights.


Description
-----------


The implementation extends the standard Sugeno integral framework to support the Quasi-Sugeno variant, which acts as a weighted aggregation mechanism for fuzzy logic concepts. During initialization, strict validation ensures that the provided list of numerical weights corresponds exactly in length to the list of concepts, preventing malformed logical structures. Logical operations such as negation, conjunction, and disjunction are supported by delegating the computation to a central operator handler, allowing these integrals to participate seamlessly in broader logical expressions. Structural manipulation capabilities include creating independent copies of the instance and recursively replacing specific constituent concepts, with the replacement operation specifically returning the negation of the modified integral. A unique string identifier is generated to represent the internal state, which also serves as the basis for hashing to enable use within collection types like sets and dictionaries.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral.QsugenoIntegral


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_quasi_sugeno_integral_QsugenoIntegral.png
       :alt: UML Class Diagram for QsugenoIntegral
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **QsugenoIntegral**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_quasi_sugeno_integral_QsugenoIntegral.pdf
       :alt: UML Class Diagram for QsugenoIntegral
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **QsugenoIntegral**

.. py:class:: QsugenoIntegral(weights: list[float], concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.sugeno_integral.SugenoIntegral`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.quasi_sugeno_integral.QsugenoIntegral
      :parts: 1
      :private-bases:


   This class encapsulates the logic for a Quasi-Sugeno integral, an aggregation operator that combines a collection of concepts with specific weights. It is initialized with a list of floating-point weights and a list of Concept objects, requiring that both lists have the same length to ensure valid aggregation. The class automatically generates a string representation of the integral in the format `(qsugeno (weights...) (concepts...))` and supports standard logical operations such as negation, conjunction, and disjunction. Additionally, it provides functionality for cloning the instance and replacing specific concepts within the integral structure.

   :param type: The classification of the concept, identifying it as a Quasi-Sugeno integral.
   :type type: typing.Any
   :param name: Automatically generated string representation of the integral in the format (qsugeno (weights) (concepts)).
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `QsugenoIntegral` class, enabling the combination or intersection of the current instance with another instance of the same type. This method delegates the specific logic to the `OperatorConcept.and_` static method, ensuring consistent handling of the operation across the module. It returns a new `QsugenoIntegral` object representing the result, leaving the original operands unmodified. While the method expects a value of the same type, specific edge cases or type compatibility checks are handled by the delegated `OperatorConcept` implementation.

      :param value: The right-hand operand for the AND operation, which must be an instance of the same class.
      :type value: typing.Self

      :return: The result of the AND operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Computes the hash value for the `QsugenoIntegral` instance, allowing it to be used as a key in dictionaries or stored in sets. The implementation derives the hash from the string representation of the object, meaning that two instances with identical string representations will yield the same hash. This method relies on the stability of the `__str__` method; if the string representation of an instance changes, its hash value will also change, which can lead to unexpected behavior if the object is used in a hash-based collection after modification.

      :return: An integer hash value for the object, derived from its string representation.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the logical negation of the current Sugeno integral instance by implementing the unary minus operator behavior. When the `-` operator is applied to an object of this class, this method delegates the computation to `OperatorConcept.not_`, passing the instance itself as the argument. The operation produces and returns a new `Concept` object representing the complement of the original integral, without modifying the state of the current instance.

      :return: Returns a new Concept representing the logical negation of this instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation (`|`) for the `QsugenoIntegral` object, enabling it to be combined with another instance of the same type. This method delegates the actual computation to the `OperatorConcept.or_` static method, which applies the specific logical disjunction rules defined for the concept. It returns a new `QsugenoIntegral` instance representing the result of the operation, ensuring that the original objects remain unmodified.

      :param value: The right-hand operand to combine with the current instance using the OR operator.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns an independent duplicate of the current instance. This method constructs a new object by creating shallow copies of the internal weights and concepts lists, ensuring that subsequent modifications to the structure of the new object do not affect the original. The returned instance is a separate entity that preserves the state of the source at the moment of the call.

      :return: A new instance of the class with copies of the current weights and concepts.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a formatted string representation of the Sugeno integral instance based on its current weights and concepts. The returned string follows a specific parenthesized syntax, starting with the 'qsugeno' identifier and including space-separated lists of the instance's weights and concepts. This method provides a canonical name or serialization format for the integral configuration without modifying the object's state.

      :return: A formatted string representing the Sugeno quantifier, including its weights and concepts.

      :rtype: str



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Performs a substitution of concept `a` with concept `c` within the structure of the integral by recursively applying the replacement operation to all constituent concepts. The method constructs a new `QsugenoIntegral` instance using the original weights and the modified list of concepts, then returns the negation of this new instance. This operation does not modify the current object in place but rather generates a new conceptual entity reflecting the substitution and sign change.

      :param a: The concept to be replaced by `c`.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: A new Concept representing the negation of the Sugeno Integral computed over the original weights and the list of concepts where every instance of `a` has been replaced by `c`.

      :rtype: Concept



   .. py:attribute:: type

      Updates the type classification of the Concept instance to the specified value. This setter method assigns the provided `ConceptType` to the internal `_type` attribute, effectively overwriting the previous type definition. The operation modifies the object's state in place and does not return a value.

      :param new_type: The classification or category to assign to the concept.
      :type new_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType

