fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept
=======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A class representing a fuzzy nominal concept that associates a specific individual with a degree of membership within an ontology.


Description
-----------


It extends the base definition for concepts to model assertions where a named individual belongs to a concept with a specific truth value. The implementation stores a floating-point number representing the membership degree alongside a string identifier for the individual entity. By registering the entity type as FUZZY_NOMINAL during initialization, the design integrates seamlessly into the broader type system used for fuzzy description logic. Accessor methods allow the retrieval of the numerical degree and the individual name, while a string representation provides a human-readable format combining these two components.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept.FuzzyNominalConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_fuzzy_nominal_concept_FuzzyNominalConcept.png
       :alt: UML Class Diagram for FuzzyNominalConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyNominalConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_fuzzy_nominal_concept_FuzzyNominalConcept.pdf
       :alt: UML Class Diagram for FuzzyNominalConcept
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyNominalConcept**

.. py:class:: FuzzyNominalConcept(n: float, i: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_nominal_concept.FuzzyNominalConcept
      :parts: 1
      :private-bases:


   This class models a specific type of fuzzy concept within the FuzzyOWL2 framework, representing the assertion that a named individual belongs to a concept with a defined degree of membership. To use this entity, instantiate it with a floating-point value indicating the truth value or membership degree and a string representing the identifier of the individual. The object provides methods to retrieve both the degree of membership and the individual's name, allowing for the precise representation of fuzzy assertions about specific entities in an ontology.

   :param _n: The degree of membership of the individual in the fuzzy nominal concept.
   :type _n: float
   :param _i: The name or identifier of the individual entity.
   :type _i: str


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the fuzzy nominal concept, formatted as a parenthesized pair containing the degree and the individual. This method retrieves the degree and individual values by calling the `get_degree` and `get_individual` methods, respectively, and formats them into a string suitable for display or logging. It does not modify the internal state of the object, though any exceptions raised by the getter methods will propagate through this call.

      :return: A string representation of the object, formatted as "(degree individual)".

      :rtype: str



   .. py:method:: get_degree() -> float

      Retrieves the numeric degree value representing the membership or truth level of this fuzzy nominal concept. This accessor returns the internal state variable `_n` as a floating-point number. The method performs no computation and has no side effects, simply providing direct read access to the concept's current degree.

      :return: The degree value.

      :rtype: float



   .. py:method:: get_individual() -> str

      Returns the individual identifier associated with this fuzzy nominal concept. This method provides access to the internal `_i` attribute, which stores the string representation of the individual. It is a side-effect-free operation that simply retrieves the stored value without altering the object's state.

      :return: The individual string associated with this instance.

      :rtype: str



   .. py:attribute:: _i
      :type:  str


   .. py:attribute:: _n
      :type:  float

