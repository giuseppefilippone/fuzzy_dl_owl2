fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A conceptual wrapper that applies a semantic modifier to a base concept to adjust the degree of membership within a fuzzy description logic framework.


Description
-----------


Designed to function within a fuzzy description logic system, the software wraps an existing base concept and applies a specific modifier to alter the semantic interpretation or degree of satisfaction for individuals. By inheriting from both the base ``Concept`` class and an interface for holding a concept, it preserves the structural properties of the underlying entity—such as roles and atomicity—while allowing the modifier to dynamically change the logic applied to it. The implementation delegates queries regarding the internal structure, like retrieving roles or determining concreteness, directly to the wrapped concept, ensuring that the modification layer does not obscure the fundamental characteristics of the original data. Logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates the creation of new complex expressions to a dedicated operator handler, thereby enabling seamless integration into broader logical formulas.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_modified_modified_concept_ModifiedConcept.png
       :alt: UML Class Diagram for ModifiedConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ModifiedConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_modified_modified_concept_ModifiedConcept.pdf
       :alt: UML Class Diagram for ModifiedConcept
       :align: center
       :width: 12.0cm
       :class: uml-diagram

       UML Class Diagram for **ModifiedConcept**

.. py:class:: ModifiedConcept(c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, mod: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_concept_interface.HasConceptInterface`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept.ModifiedConcept
      :parts: 1
      :private-bases:


   This class represents a conceptual construct where a base concept is altered by a modifier, thereby changing the degree or manner in which an individual satisfies that concept. It functions as a wrapper around an existing concept, preserving the underlying structural properties—such as roles and atomicity—while applying the semantic shift defined by the associated modifier. Users can instantiate this entity by providing a target concept and a modifier, and it supports integration into logical expressions through standard operator overloading for negation, conjunction, and disjunction.

   :param _modifier: The modifier instance that adjusts the degree of satisfaction of the underlying concept.
   :type _modifier: Modifier


   .. py:method:: __and__() -> Self

      This method implements the bitwise AND operation (`&`) for the concept by delegating the logic to the `OperatorConcept.and_` method. It passes the current instance to the helper method, which returns a new instance of the same class, effectively creating a new concept based on the AND operation. The method does not modify the original instance in place, and any errors raised during the delegation process will propagate to the caller.

      :return: The result of the AND operation, returned as an instance of the same class.

      :rtype: typing.Self



   .. py:method:: __neg__() -> Self

      Implements the unary negation operator for the concept, effectively treating the minus sign as a logical NOT operation. When invoked, this method returns a new instance representing the logical negation of the current concept by delegating to `OperatorConcept.not_`. The original instance remains unmodified, and the returned value is of the same type as the input.

      :return: Returns a new instance representing the logical negation of the current concept.

      :rtype: typing.Self



   .. py:method:: __or__() -> Self

      Implements the bitwise OR operation for the concept, enabling the use of the pipe (`|`) operator. The method delegates the execution logic to the `OperatorConcept.or_` static method, passing the current instance as the argument. It returns a new instance of the same type, representing the result of the operation.

      :return: A new instance representing the logical disjunction (OR) of this concept with another.

      :rtype: typing.Self



   .. py:method:: __repr__() -> str

      Returns the official string representation of the object by delegating directly to the `__str__` method. This implementation ensures that the output produced by the built-in `repr()` function is identical to the informal string representation. Consequently, the method provides a consistent string format for debugging and logging purposes without implementing distinct logic for representation.

      :return: A string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the informal string representation of the ModifiedConcept instance. This method delegates the generation of the display name to the `compute_name` method, which calculates the name based on the object's current state. It is intended to provide a human-readable format and is automatically invoked by the `str()` built-in function and print operations.

      :return: The informal string representation of the object, specifically its computed name.

      :rtype: str



   .. py:method:: compute_atomic_concepts() -> set[Self]

      Computes the set of atomic concepts representing the fundamental components of the current concept state. This method delegates the actual computation to the `curr_concept` attribute, invoking its corresponding method to retrieve the results. It returns a set of atomic concepts, effectively exposing the decomposed structure of the underlying concept without modifying the object's state.

      :return: A set of atomic concepts representing the fundamental components of the current concept.

      :rtype: set[typing.Self]



   .. py:method:: compute_name() -> str | None

      Generates a formatted string representation of the entity by combining the instance's modifier and current concept attributes. The resulting string is constructed by placing the modifier and concept side-by-side within parentheses, providing a concise identifier for the modified state. This method performs a read-only operation and does not alter the object's state, though it will raise an error if the required attributes are missing.

      :return: A string representing the computed name, formatted as "({modifier} {curr_concept})".

      :rtype: str | None



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of role identifiers associated with the underlying concept instance. This method delegates the call to the `curr_concept` attribute, returning the collection of roles defined by that object. The operation relies on the internal concept reference being properly initialized; otherwise, an AttributeError may occur.

      :return: A set of role names associated with the current concept.

      :rtype: set[str]



   .. py:method:: is_concrete() -> bool

      Determines whether the underlying concept is concrete by delegating the check to the `curr_concept` attribute. It returns a boolean value that reflects the concreteness status of the wrapped concept. This method serves as a pass-through, relying entirely on the implementation of the `is_concrete` method within the `curr_concept` object.

      :return: True if the current concept is concrete, False otherwise.

      :rtype: bool



   .. py:method:: replace(concept1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, concept2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      This method serves as a no-operation implementation for the replacement logic, returning the current instance unchanged regardless of the input concepts. Although the signature suggests substituting `concept1` with `concept2`, this specific implementation indicates that the `ModifiedConcept` does not support or require internal modifications of this nature. Consequently, invoking this method has no side effects on the object's state or the provided arguments.

      :param concept1: The concept to be replaced.
      :type concept1: Concept
      :param concept2: The concept to replace the first argument with.
      :type concept2: Concept

      :return: Returns the instance itself after replacing `concept1` with `concept2`.

      :rtype: Concept



   .. py:attribute:: _modifier
      :type:  fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier


   .. py:property:: modifier
      :type: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier


      Sets the modifier applied to the concept by updating the internal state. This setter accepts a `Modifier` instance and assigns it to the private `_modifier` attribute, effectively replacing any previously associated modifier. It enables dynamic modification of the concept's behavior or properties after the object has been instantiated.

      :param value:
      :type value: Modifier

