fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept
=============================================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class defines the structure and behavior for fuzzy concepts operating over specific numerical intervals.


Description
-----------


Designed to serve as a foundational template for fuzzy logic operations, the class manages a numerical domain characterized by a lower bound and an upper bound. It ensures data integrity by validating that the upper bound is never set lower than the lower bound, preventing the creation of invalid mathematical ranges. As a concrete concept type, it distinguishes itself from abstract concepts by operating directly on numerical data rather than logical relationships, and it explicitly signals its nature through a dedicated type identifier. The core functionality relies on an abstract method that forces subclasses to define the specific mathematical function used to calculate the degree of membership for a given value, allowing for various fuzzy shapes like triangular or trapezoidal distributions. Standard operations for retrieving atomic concepts or roles are implemented to return empty collections, reflecting the fact that these concrete numerical entities do not decompose into further conceptual hierarchies.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_fuzzy_concrete_concept_FuzzyConcreteConcept.png
       :alt: UML Class Diagram for FuzzyConcreteConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyConcreteConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_concrete_fuzzy_concrete_concept_FuzzyConcreteConcept.pdf
       :alt: UML Class Diagram for FuzzyConcreteConcept
       :align: center
       :width: 11.8cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyConcreteConcept**

.. py:class:: FuzzyConcreteConcept(name: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzydl.concept.concept.Concept`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept.FuzzyConcreteConcept
      :parts: 1
      :private-bases:


   This abstract base class represents a fuzzy concept defined over a specific numerical interval, characterized by a lower bound and an upper bound. It serves as a template for evaluating the degree of membership a specific numerical value has within the concept, requiring subclasses to implement the specific logic for this calculation. The class manages the interval parameters through properties, ensuring structural integrity by raising a ValueError if the upper bound is set lower than the lower bound. As a concrete concept type, it operates directly on numerical data rather than abstract relationships, providing a mechanism to quantify partial truth or satisfaction within a defined range.

   :param name: Identifier for the concept used for labeling and debugging.
   :type name: str
   :param _k1: The lower bound of the interval for which the concept is defined.
   :type _k1: float
   :param _k2: Upper bound of the interval defining the concept's domain, used to calculate membership degrees.
   :type _k2: float

   :raises ValueError: Raised when the lower bound `k1` is greater than the upper bound `k2`, which would define an invalid interval for the concept.


   .. py:method:: compute_atomic_concepts() -> set[Self]

      Returns an empty set representing the atomic concepts associated with this instance. Because this is a concrete concept, it does not decompose into or reference other atomic concepts of the same type. The method performs no computation beyond returning the empty set and has no side effects.

      :return: A set of atomic concepts represented as instances of the class.

      :rtype: set[typing.Self]



   .. py:method:: compute_name() -> str

      Retrieves the name associated with the `FuzzyConcreteConcept` instance by returning the value of the `name` attribute. This method acts as a simple accessor and does not perform any computation or modification of the underlying data. It assumes that the `name` attribute is already set; otherwise, an `AttributeError` will be raised.

      :return: The name associated with the object instance.

      :rtype: str



   .. py:method:: get_membership_degree(value: float) -> float
      :abstractmethod:


      Calculates the degree to which a specific numerical value belongs to this fuzzy concept, representing the core evaluation logic of fuzzy set theory. The method accepts a floating-point number and returns a membership coefficient, typically constrained to the range [0.0, 1.0], where 0.0 signifies complete exclusion and 1.0 signifies full inclusion. As an abstract method, it requires implementation by subclasses to define the specific shape and parameters of the membership function, such as triangular, trapezoidal, or Gaussian distributions. This operation is expected to be stateless with respect to the input value, meaning repeated calls with the same argument should yield the same result unless the concept's internal parameters change.

      :param value: The input value for which to calculate the degree of membership.
      :type value: float

      :return: A float representing the degree of membership of the input value, typically ranging from 0.0 (no membership) to 1.0 (full membership).

      :rtype: float



   .. py:method:: get_roles() -> set[str]

      Retrieves the set of roles associated with this fuzzy concrete concept. This implementation returns an empty set, indicating that no roles are defined or applicable to this specific entity. The method has no side effects and returns a new set instance on every call.

      :return: A set of strings representing the roles associated with the object.

      :rtype: set[str]



   .. py:method:: is_concrete() -> bool

      Determines whether the concept is considered concrete, returning True unconditionally for all instances of this class. This method serves as a definitive marker to distinguish `FuzzyConcreteConcept` objects from abstract or non-concrete counterparts within the conceptual hierarchy. As the implementation is constant, there are no side effects or edge cases dependent on the object's state.

      :return: True if the class is concrete, False otherwise.

      :rtype: bool



   .. py:method:: replace(concept1: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept, concept2: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept) -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      This method is designed to replace `concept1` with `concept2` within the context of the current concept, but the provided implementation currently acts as a placeholder that signals a failure. When called, it triggers an error message via `Util.error` and catches the resulting `FuzzyOntologyException` to allow execution to continue, ultimately returning `None` without modifying the object's state. Consequently, this operation does not perform a functional replacement and indicates that the feature is either unimplemented or unsupported for this specific concept type.

      :param concept1: The concept to be replaced.
      :type concept1: Concept
      :param concept2: The new concept that will replace the original concept.
      :type concept2: Concept

      :return: None

      :rtype: Concept



   .. py:attribute:: _k1
      :type:  float
      :value: 0.0



   .. py:attribute:: _k2
      :type:  float
      :value: 0.0



   .. py:property:: k1
      :type: float


      Sets the value of the `k1` attribute for the instance, converting the input to a float to ensure type consistency. This method updates the private `_k1` variable, effectively modifying the internal state of the `FuzzyConcreteConcept` object. Any subsequent operations relying on this parameter will reflect the new value.

      :param value: The new value for the k1 attribute.
      :type value: float


   .. py:property:: k2
      :type: float


      Sets the upper bound parameter k2 for the fuzzy concrete concept. This method enforces a constraint ensuring that the new value is greater than or equal to the existing k1 parameter; if k1 is larger than the provided value, a ValueError is raised. Upon successful validation, the input is converted to a float and stored in the internal state.

      :param value: The value to assign to the k2 parameter, which must be greater than or equal to k1.
      :type value: float

      :raises ValueError: Raised if the provided value is less than `k1`, as `k2` must be greater than or equal to `k1`.


   .. py:attribute:: name
      :type:  str

      Updates the name of the Concept instance to the specified string value. This setter modifies the object's internal state by assigning the provided value to the private `_name` attribute, effectively replacing any previously stored name.

      :param value: The new name to assign to the object.
      :type value: str

