fuzzy_dl_owl2.fuzzydl.concept.sigma_count
=========================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.sigma_count



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a structural representation of a sigma-count concept within fuzzy description logic to evaluate constraints based on the quantity of role fillers.


Description
-----------


A structural representation of a sigma-count concept within fuzzy description logic is provided to evaluate constraints based on the quantity of role fillers. The implementation models a condition where a target individual is considered satisfied if the number of related entities—connected via a specific role and conforming to a particular concept—falls within a fuzzy set determined by a collection of reference individuals. It encapsulates a variable for the count, the target individual, a list of reference individuals, a role name, and the concept being evaluated, storing these components to maintain the state required for subsequent processing. A deep copy mechanism is included to create independent instances of the object, while accessor methods expose the internal components for inspection. Standard Python magic methods are utilized to generate human-readable string representations and to compute hash values based on the object's string format, enabling use in collections like sets and dictionaries.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.concept.sigma_count.SigmaCount


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_sigma_count_SigmaCount.png
       :alt: UML Class Diagram for SigmaCount
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SigmaCount**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_concept_sigma_count_SigmaCount.pdf
       :alt: UML Class Diagram for SigmaCount
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SigmaCount**

.. py:class:: SigmaCount(var: fuzzy_dl_owl2.fuzzydl.milp.variable.Variable, ind: fuzzy_dl_owl2.fuzzydl.individual.individual.Individual, inds: list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual], role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   This class represents a sigma-count concept within fuzzy description logic, serving as a structural representation for evaluating constraints based on the quantity of role fillers. It defines a condition where a target individual is considered satisfied if the number of related entities—connected via a specific role and conforming to a particular concept—falls within a fuzzy set determined by a collection of reference individuals. To use this class, instantiate it with a variable for the count, the target individual, the list of reference individuals, the role name, and the concept to be evaluated. The object provides methods to access these internal components and a cloning utility to create deep copies of the instance.

   :param variable: The variable associated with the sigma-count concept, used for counting the number of role fillers that satisfy the concept C.
   :type variable: Variable
   :param individual: The individual for which the sigma-count concept is being evaluated.
   :type individual: Individual
   :param individuals: The set of individuals $\{a_1, a_2, \dots, a_n\}$ considered in the fuzzy concrete concept $D$ for the sigma-count evaluation.
   :type individuals: list[Individual]
   :param role: The relationship identifier 'r' used in the sigma-count expression to connect the individual to the fillers being counted.
   :type role: str
   :param concept: The concept C that role fillers must satisfy to be included in the sigma-count.
   :type concept: Concept


   .. py:method:: __hash__() -> int

      Computes the hash value for the instance by hashing its string representation. This allows the object to be used as a dictionary key or stored in a set. The hash is derived directly from the output of the `__str__` method, ensuring that the hash value remains consistent as long as the string representation does not change.

      :return: An integer hash value calculated from the object's string representation.

      :rtype: int



   .. py:method:: __repr__() -> str

      Returns the official string representation of the instance by delegating directly to the informal string conversion logic. This approach ensures that the output displayed in interactive sessions or logs is identical to the user-facing string format. The method performs no state modifications and depends entirely on the behavior of the `__str__` method to generate the resulting string.

      :return: The string representation of the object, identical to the output of `str()`.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the SigmaCount instance formatted as a functional expression. The output string follows the pattern 'sigma-count(...)', incorporating the object's variable, individual, individuals, role, and concept attributes as comma-separated arguments. This method is intended for display purposes and does not modify the object's state.

      :return: A string representation of the object, formatted as a sigma-count function call containing the variable, individual, individuals, role, and concept attributes.

      :rtype: str



   .. py:method:: clone() -> Self

      Creates and returns a deep copy of the current `SigmaCount` instance. The method recursively clones the `variable`, `individual`, and `concept` attributes, and generates a new list containing clones of all elements within the `individuals` collection. The `role` attribute is passed by reference rather than being cloned. This operation has no side effects on the original object, ensuring that the returned instance is independent with respect to its deep-copied components.

      :return: A new instance of `SigmaCount` that is a deep copy of the current object.

      :rtype: typing.Self



   .. py:method:: get_concept() -> fuzzy_dl_owl2.fuzzydl.concept.concept.Concept

      Returns the `Concept` object associated with the current `SigmaCount` instance. This method acts as a simple accessor, retrieving the value of the `concept` attribute without modifying the object's internal state. If the attribute has not been set, this method will raise an `AttributeError`.

      :return: The Concept object associated with this instance.

      :rtype: Concept



   .. py:method:: get_individual() -> fuzzy_dl_owl2.fuzzydl.individual.individual.Individual

      Retrieves the `Individual` entity associated with the current `SigmaCount` instance. This accessor method returns the reference to the stored object without causing any side effects or modifying the internal state.

      :return: The Individual instance associated with this object.

      :rtype: Individual



   .. py:method:: get_individuals() -> list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]

      Retrieves the collection of `Individual` objects managed by the `SigmaCount` instance. Since this method returns a direct reference to the internal list, any in-place modifications to the returned list will alter the state of the object.

      :return: A list of the individuals associated with this instance.

      :rtype: list[Individual]



   .. py:method:: get_role() -> str

      Retrieves the string value assigned to the `role` attribute of the current instance. This accessor method provides read-only access to the specific role or category associated with the `SigmaCount` object without modifying its internal state. It assumes the attribute has been properly initialized; accessing this method on an instance where the attribute is missing will result in an `AttributeError`.

      :return: The role associated with the instance.

      :rtype: str



   .. py:method:: get_variable() -> fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

      Retrieves the `Variable` instance associated with this `SigmaCount` object. This method acts as a simple accessor, returning the reference to the internal variable attribute without modifying the state of the object. It allows external code to inspect which variable is being tracked or aggregated by the counter.

      :return: The `Variable` instance stored in the `variable` attribute.

      :rtype: Variable



   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: individual
      :type:  fuzzy_dl_owl2.fuzzydl.individual.individual.Individual


   .. py:attribute:: individuals
      :type:  list[fuzzy_dl_owl2.fuzzydl.individual.individual.Individual]


   .. py:attribute:: role
      :type:  str


   .. py:attribute:: variable
      :type:  fuzzy_dl_owl2.fuzzydl.milp.variable.Variable

