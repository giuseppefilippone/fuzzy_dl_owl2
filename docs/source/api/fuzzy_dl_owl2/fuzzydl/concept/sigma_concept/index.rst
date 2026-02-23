fuzzy_dl_owl2.fuzzydl.concept.sigma_concept
===========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.sigma_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A Python class representing a sigma-count construct within fuzzy description logic that evaluates concept satisfaction based on the cardinality of related individuals.


Description
-----------


Sigma-count logic is encapsulated by modeling a concept that is satisfied when the number of individuals reachable via a specific role and belonging to a target concept meets a fuzzy concrete domain constraint relative to a reference set. It maintains references to the role, the target concept, the list of reference individuals, and the fuzzy concrete concept, effectively acting as a composite node within a broader description logic framework. Logical operations such as negation, conjunction, and disjunction are supported through operator overloading, which delegates the creation of new concept instances to a dedicated operator factory to ensure consistent handling of complex expressions. To facilitate use in collections and comparisons, it generates a deterministic string representation and implements deep cloning to ensure the independence of copied instances. Structural queries for atomic components or roles return empty sets, indicating that this construct is treated as a terminal node during specific graph traversals or analyses.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.sigma_concept.SigmaConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_sigma_concept_SigmaConcept.png
       :alt: UML Class Diagram for SigmaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SigmaConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_sigma_concept_SigmaConcept.pdf
       :alt: UML Class Diagram for SigmaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SigmaConcept**

.. py:class:: SigmaConcept(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, role: str, individuals: list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual], concrete_concept: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.sigma_concept.SigmaConcept
      :parts: 1
      :private-bases:


   This class models a sigma-count construct within fuzzy description logic, defining a concept that is satisfied based on the cardinality of related individuals. Specifically, it evaluates whether the number of individuals reachable via a specific role that also belong to a given concept falls within a fuzzy concrete domain relative to a specified set of reference individuals. To utilize this class, instantiate it by providing a role string, a target concept, a list of individual objects, and a fuzzy concrete concept. The object automatically generates a string representation for its name and provides methods to access its components, clone itself deeply, and participate in logical operations such as negation, conjunction, and disjunction.

   :param concept: The concept C that related individuals must be instances of to be counted in the sigma-count.
   :type concept: Concept
   :param role: The binary relation used in the sigma-count expression to identify the connections between individuals.
   :type role: str
   :param individuals: The list of individuals constituting the set {a1, a2, ..., an} used as the reference context for evaluating the sigma-count concept.
   :type individuals: list[Individual]
   :param concrete_concept: The fuzzy concrete concept used to evaluate the sigma-count of related individuals.
   :type concrete_concept: FuzzyConcreteConcept
   :param name: Computed string representation of the sigma-count concept, automatically generated during initialization.
   :type name: str


   .. py:method:: __and__(value: Self) -> Self

      Implements the bitwise AND operation (`&`) for the `SigmaConcept` instance, allowing it to be combined with another instance of the same type. This method delegates the logic to `OperatorConcept.and_`, passing the current object and the provided value to compute the result. The operation returns a new instance representing the conjunction of the two concepts, leaving the original operands unmodified.

      :param value: The right-hand operand for the AND operation.
      :type value: typing.Self

      :return: A new instance representing the result of the AND operation between this object and the provided value.

      :rtype: typing.Self



   .. py:method:: __hash__() -> int

      Returns an integer hash value for the instance based on its string representation, enabling the object to be used as a dictionary key or stored in a set. The implementation delegates the hashing logic to the built-in `hash` function applied to the result of `str(self)`, which implies that the object should be treated as immutable or that its string representation must remain constant to maintain consistent behavior within hash-based collections.

      :return: An integer hash value based on the string representation of the object.

      :rtype: int



   .. py:method:: __neg__() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Implements the unary negation operator to return the logical negation of the current concept. This allows the use of the minus sign (`-`) to invert the meaning of a `SigmaConcept`, resulting in a new `Concept` that represents the logical NOT operation applied to the original instance. The method delegates the actual construction of the negated concept to the `OperatorConcept.not_` factory method.

      :return: A new Concept representing the logical negation of the current instance.

      :rtype: Concept



   .. py:method:: __or__(value: Self) -> Self

      Implements the bitwise OR operator (`|`) to combine the current concept with another instance of the same type. This method delegates the logic to `OperatorConcept.or_`, effectively creating a new concept that represents the logical disjunction or union of the two operands. It ensures type consistency by returning an instance of the same class as the inputs.

      :param value: The right-hand operand to combine with the current instance using the OR operation.
      :type value: typing.Self

      :return: The result of the OR operation between the current instance and the provided value.

      :rtype: typing.Self



   .. py:method:: clone() -> Self

      Creates and returns a deep copy of the current `SigmaConcept` instance. To ensure the new object is independent of the original, the method recursively clones the `concept`, `concrete_concept`, and every element within the `individuals` list. The `role` attribute is passed by reference to the new instance. This operation does not modify the original object.

      :return: A new instance of the class that is a copy of the current object, with nested concepts, individuals, and concrete concepts also cloned.

      :rtype: typing.Self



   .. py:method:: compute_atomic_concepts() -> set[fuzzy_dl_owl2.fuzzydl.concept.concept.Concept]

      Computes the set of atomic concepts associated with this SigmaConcept. In this specific implementation, the method returns an empty set, indicating that the concept does not decompose into atomic constituents or serving as a default stub for subclasses. The operation is side-effect free and generates a new set instance upon each call.

      :return: A set of atomic concepts.

      :rtype: set[Concept]



   .. py:method:: compute_name() -> str | None

      Constructs and returns a string representation of the sigma concept using a specific parenthesized syntax. The format follows the pattern `(sigma-count role concept {individuals} concrete_concept)`, where the list of individuals is converted to strings, joined by spaces, and enclosed in curly braces. This method relies on the current values of the `role`, `concept`, `individuals`, and `concrete_concept` attributes without modifying them, resulting in a deterministic string output based on the object's state. While the type hint indicates a potential return of `None`, the implementation consistently returns a formatted string, which may include literal "None" text if the underlying attributes are unset.

      :return: A formatted string representing the sigma-count, constructed from the role, concept, individuals, and concrete concept.

      :rtype: str | None



   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Retrieves the underlying `Concept` instance associated with this `SigmaConcept` object. This method acts as a simple accessor, returning the value stored in the `concept` attribute without modifying the state of the `SigmaConcept` instance. Note that because it returns a direct reference to the internal object, any mutations made to the returned `Concept` will be reflected in the original instance.

      :return: The `Concept` object associated with this instance.

      :rtype: Concept



   .. py:method:: get_fuzzy_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept

      Retrieves the fuzzy concrete concept representation associated with this instance. This method acts as a simple accessor, returning the object stored in the `concrete_concept` attribute. It performs no computation or modification of state during the retrieval process.

      :return: The FuzzyConcreteConcept instance stored in the concrete_concept attribute.

      :rtype: FuzzyConcreteConcept



   .. py:method:: get_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]

      Returns the list of `Individual` entities currently associated with this `SigmaConcept` instance. This method provides direct access to the underlying list attribute, allowing callers to inspect the collection. Note that because the reference is returned directly, any modifications made to the list (such as adding or removing elements) will immediately affect the internal state of the `SigmaConcept` object.

      :return: The list of Individual objects associated with this instance.

      :rtype: list[Individual]



   .. py:method:: get_role() -> str

      Retrieves the role associated with the SigmaConcept instance. This accessor method returns the value of the internal `role` attribute without modifying the object's state. The method assumes the attribute has been initialized; otherwise, an AttributeError will be raised.

      :return: The role associated with the instance.

      :rtype: str



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of role identifiers associated with the concept instance. The current implementation returns an empty set, serving as a default behavior for subclasses or instances where no specific roles are defined. This method has no side effects and returns a new set object on every call.

      :return: A set of strings representing the roles.

      :rtype: set[str]



   .. py:method:: replace(a: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, c: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the current instance unchanged, acting as an identity function within the replacement operation. Although the method signature implies a substitution of concept `a` with concept `c`, the implementation indicates that `SigmaConcept` is treated as an atomic or terminal entity that does not contain sub-components subject to this transformation. As a result, the method has no side effects and returns the original object regardless of the arguments provided.

      :param a: The concept to be replaced.
      :type a: Concept
      :param c: The concept to replace the original concept with.
      :type c: Concept

      :return: Returns the current instance.

      :rtype: Concept



   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: concrete_concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


   .. py:attribute:: individuals
      :type:  list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:attribute:: name
      :type:  str
      :value: '(sigma-count Uninferable Uninferable {} Uninferable)'


      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str


   .. py:attribute:: role
      :type:  str

