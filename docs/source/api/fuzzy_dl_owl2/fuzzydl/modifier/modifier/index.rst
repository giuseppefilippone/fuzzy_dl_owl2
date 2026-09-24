fuzzy_dl_owl2.fuzzydl.modifier.modifier
=======================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.modifier.modifier





.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that establishes the shared contract for fuzzy modifiers — linguistic hedges such as *very* or *somewhat* — which transform fuzzy concepts and remap membership degrees within a fuzzy description-logic knowledge base.


Description
-----------


Serving as the blueprint for every concrete modifier, ``Modifier`` relies on Python's ABC mechanism to force subclasses to supply their own logic for four essential operations: deriving a printable name, producing an independent duplicate of the modifier, applying its transformation to a fuzzy ``Concept``, and computing the modified membership degree for a given real-valued input. The base class deliberately contains no mathematics of its own, because intensification, dilation, and other hedges differ in how they reshape membership functions; the only guaranteed contract is that the resulting degree stays within the normalized [0, 1] interval, leaving clamping and mapping details to each implementation. Each instance carries a human-readable name that may be assigned at construction time or derived lazily through the subclass's own naming logic the first time the string representation is requested, with the result cached on the instance so the computation happens at most once; no validation is performed on the stored value, so the caller is trusted to supply a well-formed string.

Hashing is based on the stored name rather than object identity, which allows structurally equivalent modifiers to be used interchangeably as dictionary keys or set members, while the debug representation simply mirrors the same string form for consistent display during interactive sessions. The mandate that every modifier be able to produce a functionally independent copy of itself reflects the knowledge base's need to reuse modifier instances across many concepts without risking shared mutable state, and the lazy naming scheme keeps freshly created modifiers self-identifying without forcing subclasses to precompute labels they may never need.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_modifier_modifier_Modifier.png
       :alt: UML Class Diagram for Modifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **Modifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_modifier_modifier_Modifier.pdf
       :alt: UML Class Diagram for Modifier
       :align: center
       :width: 9.1cm
       :class: uml-diagram

       UML Class Diagram for **Modifier**

.. py:class:: Modifier(name: str)

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.modifier.modifier.Modifier
      :parts: 1
      :private-bases:


   This abstract base class serves as a blueprint for fuzzy modifiers that alter concepts within a knowledge base. It defines the essential interface for applying transformations to fuzzy concepts and calculating membership degrees, requiring subclasses to implement specific logic for operations such as modification, cloning, and name generation. The class encapsulates a string identifier for the modifier, which can be explicitly set or derived dynamically, and provides a mechanism to map real numbers to a normalized range between 0 and 1.

   :param name: The human-readable label or identifier for the fuzzy modifier instance, used as its string representation.
   :type name: str


   .. py:method:: __hash__() -> int

      Return a hash value for this object, computed from its string representation. This approach ensures that the hash value reflects the structural identity of the object without relying on cached values or additional methods. The hash is derived from the output of the `__str__` method, which provides a consistent and unique representation of the concept's structure. This implementation does not utilize any internal caching mechanism and directly computes the hash each time it is called.

      :return: An integer hash value representing the structural identity of this object.

      :rtype: int



   .. py:method:: __repr__() -> str

      Returns a string representation of the Modifier instance by delegating to the object's `__str__` method. This implementation ensures that the official representation used for debugging and interactive sessions is identical to the informal string representation. As a result, the output format is determined by the logic defined in the string conversion handler, rather than providing a distinct, machine-parseable format.

      :return: Returns a string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns the string representation of the object, which is derived from its name. If the `name` attribute is currently `None`, the method lazily computes and caches the name by calling `compute_name` before returning it. Note that this method has the side effect of mutating the instance by setting the `name` attribute if it was previously unset.

      :return: The name of the object, computed if necessary.

      :rtype: str



   .. py:method:: clone() -> Self
      :abstractmethod:


      Generates a new instance that is a functional duplicate of the current object. The clone must be of the same concrete type and possess an identical state to the original at the moment of invocation. As this is an abstract method, subclasses are responsible for implementing the specific copying mechanism, which typically involves creating a deep copy to ensure that subsequent modifications to the clone do not impact the source object.

      :return: Returns a new instance of the same class, initialized with the same state as the current object.

      :rtype: typing.Self



   .. py:method:: compute_name() -> str
      :abstractmethod:


      Calculates and returns the name associated with this specific modifier instance. As an abstract method, it requires concrete subclasses to provide an implementation that defines how the name is derived, ensuring consistent identification across different modifier types. The returned string is typically used for logging, debugging, or as a unique identifier within the application's logic.

      :return: A string representing the computed name of the object.

      :rtype: str



   .. py:method:: get_membership_degree(value: float) -> float
      :abstractmethod:


      Calculates the modified membership degree for a given input value, typically used within fuzzy logic systems to transform existing membership values. This abstract method requires subclasses to implement the specific mathematical logic for the modifier, such as intensification or dilation, ensuring that the result is normalized to the interval [0, 1]. While the input is a real number, the implementation is expected to handle the transformation such that the output represents a valid degree of membership, potentially clamping or mapping values that fall outside standard ranges. The operation is generally side-effect free, acting as a pure function of the input value.

      :param value: The real number for which the membership degree is calculated.
      :type value: float

      :return: The degree of membership of the input value, calculated by the modifier function and normalized to the range [0, 1].

      :rtype: float



   .. py:method:: modify(concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept
      :abstractmethod:


      Applies a specific modification rule to the provided fuzzy concept, transforming its properties or membership function according to the logic defined by the concrete subclass. As an abstract method, it establishes the interface for various linguistic hedges or logical operators, requiring implementations to define the exact nature of the transformation. The method accepts a Concept object and returns a new Concept instance representing the modified state, typically without altering the original input concept.

      :param concept: The fuzzy concept to which the modifier is applied.
      :type concept: Concept

      :return: The fuzzy concept resulting from applying the modifier to the input concept.

      :rtype: Concept



   .. py:method:: set_name(name: str) -> None

      Assigns the provided string value to the `name` attribute of the current instance, effectively updating the identifier associated with the Modifier object. This operation mutates the object's state by overwriting any previously stored name. The method does not return a value and assumes the input is a valid string, as no explicit validation is performed on the argument.

      :param name: The new name to assign to the object.
      :type name: str



   .. py:attribute:: name
      :type:  str
