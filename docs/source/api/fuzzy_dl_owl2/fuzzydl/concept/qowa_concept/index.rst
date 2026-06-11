fuzzy_dl_owl2.fuzzydl.concept.qowa_concept
==========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.qowa_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a quantified Ordered Weighted Averaging (OWA) concept that dynamically calculates aggregation weights based on a fuzzy quantifier.


Description
-----------


Extending the standard Ordered Weighted Averaging mechanism, this implementation leverages a fuzzy quantifier to dynamically determine the weighting scheme for aggregating a collection of concepts. Rather than relying on manually specified weights, the logic calculates the necessary values by evaluating the membership degree of the provided quantifier across the range of input concepts, effectively translating linguistic terms like "most" or "at least half" into mathematical weights. The design integrates seamlessly with the broader fuzzy description logic framework by supporting essential logical operations such as negation, conjunction, and disjunction, which are handled through operator delegation. Structural integrity is maintained through cloning and replacement methods, ensuring that instances can be safely copied or modified within complex logical expressions without unintended side effects.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_qowa_concept_QowaConcept.png
       :alt: UML Class Diagram for QowaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **QowaConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_qowa_concept_QowaConcept.pdf
       :alt: UML Class Diagram for QowaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **QowaConcept**

.. py:class:: QowaConcept(quantifier: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept, concepts: list[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.owa_concept.OwaConcept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.qowa_concept.QowaConcept
      :parts: 1
      :private-bases:


   This class implements a quantified aggregation strategy that combines a collection of concepts using a fuzzy quantifier to dynamically determine the weighting scheme. Instead of requiring explicit weights, it calculates them by evaluating the membership degree of the provided quantifier across the range of input concepts. Users can instantiate this object by providing a fuzzy concrete concept as the quantifier and a list of concepts to be aggregated. During initialization, the system automatically computes the weights and generates a standardized string representation. It supports standard logical operations and ensures structural consistency through cloning and replacement methods.

   :param type: The classification identifier for the concept, indicating it is a quantified OWA.
   :type type: typing.Any
   :param _quantifier: Stores the fuzzy concrete concept representing the quantifier, which determines the aggregation weights for the OWA operation.
   :type _quantifier: FuzzyConcreteConcept
   :param name: String representation of the concept formatted as `(q-owa Q C1 ... Cn)`, automatically generated during initialization and updated when the quantifier changes.
   :type name: typing.Any


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `QowaConcept` instance, allowing it to be combined with another instance of the same type. This method delegates the actual computation to `OperatorConcept.and_`, passing the current object and the provided value as operands. The operation returns a new instance representing the result of the conjunction, leaving the original operands unchanged.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: A new instance representing the result of the AND operation between this object and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the logical negation of the current concept instance, corresponding to the unary minus operator. The method constructs an intermediate `OwaConcept` using the instance's weights and concepts, then applies a logical NOT operation via `OperatorConcept.not_`. This results in a new `Concept` object representing the complement of the original logic without modifying the original instance.

      :return: Returns a new Concept representing the logical negation of the current instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operation for the concept, allowing it to be combined with another instance of the same type using the pipe operator (`|`). This method delegates the actual combination logic to `OperatorConcept.or_`, which produces a new concept representing the logical disjunction or union of the two operands. The operation is non-destructive, ensuring that the original instances remain unmodified while a new object is returned to represent the result.

      :param value: The right-hand operand for the OR operation.
      :type value: typing.Self

      :return: The result of the logical OR or union operation between this instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a new instance of `QowaConcept` that is a shallow copy of the current object. The new instance preserves the original quantifier and creates a new list containing references to the same underlying concept objects. This ensures that structural modifications to the clone's list of concepts do not affect the original instance, although changes to the individual concept objects themselves will be reflected in both.

      :return: A new instance of the class with the same quantifier and a copy of the concepts list.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str

      Generates a standardized string representation of the QOWA concept by combining its quantifier and associated concepts into a specific parenthetical format. The returned string follows the pattern "(q-owa <quantifier> <concept1> <concept2> ...)", where the quantifier and the list of concepts are converted to strings and joined by spaces. This method does not modify the object's state and relies on the string conversion methods of the underlying quantifier and concept objects.

      :return: A string representation of the query name, formatted with the quantifier and concepts.

      :rtype: str



   .. py:method:: compute_weights(n: int) -> None

      Calculates and appends a sequence of weights to the instance's weight list based on the associated quantifier. The method iterates `n` times, calculating the normalized position `w` and determining the membership degree of the difference between the current and previous positions (which is constant at `1/n`). If the input `n` is less than or equal to zero, the method returns without making changes. This operation modifies the internal state by appending to the `weights` attribute, meaning repeated calls will extend the list rather than replace it.

      :param n: The number of weights to generate, used as the denominator for calculating the step size.
      :type n: int



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Optional[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Returns a new concept instance where all occurrences of the target concept `a` are substituted with the replacement concept `c`. This operation traverses the internal list of concepts recursively, applying the replacement to each sub-concept to ensure the substitution propagates through the entire structure. The method constructs a new `OwaConcept` using the original quantifier and the modified list of concepts, then returns the negation of that structure, leaving the original instance unmodified.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to substitute for `a` within the structure.
      :type c: Concept

      :return: A new Concept instance where all occurrences of concept `a` have been replaced by concept `c`.

      :rtype: typing.Optional[Concept]



   .. py:attribute:: _quantifier
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


   .. py:attribute:: name
      :value: '(q-owa Uninferable )'



   .. py:property:: quantifier
      :type: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


      Returns the fuzzy quantifier (a concrete concept such as "most" or "at least half") that defines the weighting of this quantifier-guided OWA concept. The value is read from the private ``_quantifier`` attribute without modifying the instance.

      :return: The fuzzy quantifier driving the OWA weights.

      :rtype: FuzzyConcreteConcept


   .. py:attribute:: type

