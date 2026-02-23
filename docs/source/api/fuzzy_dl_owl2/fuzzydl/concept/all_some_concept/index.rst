fuzzy_dl_owl2.fuzzydl.concept.all_some_concept
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.all_some_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a class representing universal and existential quantified role restrictions within a fuzzy description logic framework.


Description
-----------


The software models quantified role restrictions, specifically universal and existential constraints, which are fundamental constructs in description logic for defining relationships between individuals. It employs a factory pattern for instantiation, enabling logical optimizations that simplify complex expressions—such as reducing a universal restriction over the top concept to the top concept itself—before object creation. Logic for negation is implemented by inverting the quantifier type and recursively negating the nested concept, ensuring that the logical structure remains consistent during operations. Furthermore, the implementation supports structural manipulations like cloning and sub-concept replacement, allowing the system to dynamically modify concept definitions while maintaining the integrity of role hierarchies and atomic constituents.

.. ── LLM-GENERATED DESCRIPTION END ──

Attributes
----------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.All
   fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.Some


Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.AllSomeConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_all_some_concept_AllSomeConcept.png
       :alt: UML Class Diagram for AllSomeConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **AllSomeConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_all_some_concept_AllSomeConcept.pdf
       :alt: UML Class Diagram for AllSomeConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **AllSomeConcept**

.. py:class:: AllSomeConcept(role: str, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.interface.has_role_concept_interface.HasRoleConceptInterface`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.all_some_concept.AllSomeConcept
      :parts: 1
      :private-bases:


   Represents quantified role restrictions, specifically universal ("all") and existential ("some") restrictions, within a description logic framework. It defines conditions that an individual must satisfy regarding its relationships: for a universal restriction, every individual connected via a specific role must belong to a target concept, while for an existential restriction, at least one such connected individual must belong to the target concept. Instances are best created using the static factory methods `all` and `some`, which apply logical optimizations—such as reducing `(all r TOP)` to `TOP`—before construction. The object supports standard concept operations including negation, which inverts the quantifier type and negates the nested concept, as well as cloning and sub-concept replacement.

   :param _name: Computed string representation of the concept, formatted as "(all r C)" or "(some r C)".
   :type _name: str


   .. py:method:: __hash__() -> int

      Returns an integer hash value for the instance based on its string representation, enabling the object to be used as a dictionary key or stored in a set. The implementation delegates to the built-in `hash` function applied to `str(self)`, meaning the hash value is intrinsically linked to the output of the object's string conversion. Consequently, if the object is mutable and its string representation changes, the hash value will also change, which violates the immutability requirement for objects used in hash-based collections and may lead to unpredictable behavior.

      :return: An integer hash value derived from the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator for the concept, returning a new instance that represents the logical inverse. The method swaps the quantifier type between 'ALL' and 'SOME', retains the current role, and recursively negates the inner concept. This operation is side-effect free, leaving the original object unchanged.

      :return: The logical negation of the concept, with the quantifier type toggled between ALL and SOME and the underlying concept negated.

      :rtype: Concept



   .. py:method:: all(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:


      Constructs a new `AllSomeConcept` instance representing a universal quantification over the provided concept. This static factory method accepts a role string and a `Concept` object, initializing the instance with the specific type `ConceptType.ALL`. It serves as a convenience wrapper around the internal `new` method to simplify the creation of "all" relationships within the module.

      :param role: The name of the role or property defining the universal restriction.
      :type role: str
      :param concept: The concept defining the range of the universal restriction.
      :type concept: Concept

      :return: Returns a new instance representing a universal quantification over the specified role and concept.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a distinct copy of the current `AllSomeConcept` instance. This method generates the new object by passing the current object's `type`, `role`, and `curr_concept` attributes to the class constructor. The original object remains unmodified by this operation, although the clone will reference the same underlying attribute values as the source.

      :return: A new instance of the class with the same type, role, and current concept as the current object.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Calculates and returns the set of atomic concepts by delegating the computation to the concept object stored in the `curr_concept` attribute. This method serves as a wrapper that forwards the request, allowing the underlying concept to determine its own atomic constituents. The result is a set containing the fundamental concepts that compose the current structure, and the operation relies entirely on the implementation of the delegated method within the referenced concept.

      :return: A set of atomic concepts that constitute the current concept.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str

      Generates a string representation of the concept based on its quantifier type, formatting the output to include the role and current concept within parentheses. If the concept type is defined as 'ALL', the resulting string uses the 'all' quantifier; otherwise, it defaults to the 'some' quantifier. This method does not modify the object's state and relies on the string representations of the associated role and concept attributes.

      :return: A string representation of the concept, formatted as '(all role concept)' or '(some role concept)' based on the concept type.

      :rtype: str



   .. py:method:: get_atoms() -> list[Self]

      Retrieves the fundamental atomic elements associated with the current concept by delegating the call to the `get_atoms` method of the internal `curr_concept` attribute. The returned list contains instances of the class, representing the indivisible components that constitute the concept's structure. This method acts as a pass-through wrapper without modifying the state of the object, though it may raise an error if the underlying `curr_concept` is not initialized.

      :return: A list of instances of this class representing the atomic components of the current concept.

      :rtype: list[typing.Self]



   .. py:method:: get_roles() -> set[str]

      Returns a comprehensive set of role identifiers associated with the current instance and its related concept. The method constructs a set containing the instance's own `role` attribute and merges it with the roles retrieved from the `curr_concept` attribute via a recursive call to `get_roles`. This ensures that the returned collection includes both the local role and any roles inherited or defined by the linked concept object.

      :return: A set of role strings representing the union of the instance's role and the roles of the current concept.

      :rtype: set[str]



   .. py:method:: is_complemented_atomic() -> bool

      Determines if the current concept represents a complemented atomic concept, which is the negation of a primitive class. Because this class models a complex restriction involving quantifiers rather than a simple negation, it cannot satisfy this condition. The method always returns False and has no side effects.

      :return: True if the object is complemented atomic, False otherwise.

      :rtype: bool



   .. py:method:: new(c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType, role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:


      Acts as a factory method for instantiating `AllSomeConcept` objects based on a specified concept type, role, and nested concept. When optimizations are enabled via the configuration, the method applies logical simplifications: if the type is `SOME` and the nested concept is `BOTTOM`, it returns the global bottom concept; conversely, if the type is `ALL` and the nested concept is `TOP`, it returns the global top concept. If these optimization conditions are not met, the method constructs and returns a new `AllSomeConcept` instance initialized with the provided arguments.

      :param c_type: Specifies the type of concept to instantiate, determining whether it represents a universal (ALL) or existential (SOME) quantification.
      :type c_type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType
      :param role: The role or property name used to define the concept restriction.
      :type role: str
      :param concept: The concept instance to be wrapped or restricted.
      :type concept: Concept

      :return: Returns a new instance representing the specified restriction. If optimizations are enabled and the result is trivial (e.g., `SOME` of `BOTTOM` or `ALL` of `TOP`), returns the corresponding `TruthConcept` singleton.

      :rtype: typing.Self



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Creates and returns a new `AllSomeConcept` instance where all occurrences of the specified concept `a` within the underlying `curr_concept` are replaced by concept `c`. The `type` and `role` attributes of the original instance are preserved in the resulting object. This method does not modify the current instance in place, ensuring immutability.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to substitute in place of `a`.
      :type c: Concept

      :return: Returns a new concept where all occurrences of concept `a` are replaced by concept `c`.

      :rtype: Concept



   .. py:method:: some(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> Self
      :staticmethod:


      Constructs a new instance of the class representing a specific type of concept relationship defined by the `SOME` type identifier. This static factory method accepts a string defining the role and a `Concept` object, delegating the actual instantiation logic to the underlying `new` method. It serves as a semantic convenience for creating objects that represent partial or existential quantification within the broader concept system.

      :param role: The name or identifier of the property or relation involved in the existential restriction.
      :type role: str
      :param concept: The concept to be represented as a 'some' concept.
      :type concept: Concept

      :return: A new instance of the class representing a "some" concept relationship initialized with the provided role and concept.

      :rtype: typing.Self



   .. py:attribute:: _name
      :type:  str


.. py:data:: All

.. py:data:: Some
