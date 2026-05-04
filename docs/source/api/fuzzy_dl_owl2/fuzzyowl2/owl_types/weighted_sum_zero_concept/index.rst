fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept
===========================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized class within the FuzzyOWL2 framework represents a fuzzy logic constraint defined by a weighted sum of component concepts equating to zero.


Description
-----------


It extends the base definition to encapsulate a collection of subordinate concept definitions that act as the operands for this specific calculation. The design facilitates the storage and retrieval of these internal components while providing a standardized string representation that identifies the constraint type and its elements. By treating the zero-sum condition as a distinct entity, the implementation allows the ontology to express complex mathematical relationships and constraints as first-class objects.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept.WeightedSumZeroConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_sum_zero_concept_WeightedSumZeroConcept.png
       :alt: UML Class Diagram for WeightedSumZeroConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedSumZeroConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_sum_zero_concept_WeightedSumZeroConcept.pdf
       :alt: UML Class Diagram for WeightedSumZeroConcept
       :align: center
       :width: 10.1cm
       :class: uml-diagram

       UML Class Diagram for **WeightedSumZeroConcept**

.. py:class:: WeightedSumZeroConcept(wc: list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_zero_concept.WeightedSumZeroConcept
      :parts: 1
      :private-bases:


   This class models a specific fuzzy logic constraint within the FuzzyOWL2 framework, representing a concept defined by a weighted sum that equates to zero. It serves as a specialized container that aggregates a collection of other concept definitions, which act as the components or operands involved in the calculation. To utilize this class, instantiate it with a list of `ConceptDefinition` objects representing the terms to be weighted. Once created, the object functions as a standard concept definition within the ontology, allowing the internal list of weighted concepts to be retrieved via the `get_weighted_concepts` method.

   :param _wc: Collection of concept definitions that constitute the operands of the weighted sum zero expression.
   :type _wc: list[ConceptDefinition]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the weighted sum zero concept. The output is formatted as a parenthesized expression starting with the identifier 'w-sum-zero', followed by the string representations of the internal weights or coefficients. This method relies on the string conversion of the elements within the internal collection and does not alter the object's state.

      :return: A string representation of the object, formatted as "(w-sum-zero ...)" containing the internal weights joined by spaces.

      :rtype: str



   .. py:method:: get_weighted_concepts() -> list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]

      Returns the list of concept definitions associated with this weighted sum zero concept. This method provides access to the internal collection of concepts that are used to form the weighted sum. Note that the returned list is a direct reference to the internal state, so modifying it may alter the object's behavior.

      :return: A list of ConceptDefinition objects representing the weighted concepts.

      :rtype: list[ConceptDefinition]



   .. py:attribute:: _wc
      :type:  list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]

