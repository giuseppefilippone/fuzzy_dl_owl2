fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept
======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept





.. ── LLM-GENERATED DESCRIPTION START ──

Defines a weighted-maximum fuzzy concept that aggregates a list of concept definitions under the weighted max operator for use in the FuzzyOWL2 ontology framework.


Description
-----------


**WeightedMaxConcept** extends the base *ConceptDefinition* type to represent one particular fuzzy construct: the weighted maximum aggregation over a collection of concepts. At construction time it tags itself with the ``ConceptType.WEIGHTED_MAX`` discriminator, which is how the surrounding framework distinguishes it from other fuzzy operators (such as weighted sums or minima) when serialising or reasoning over the ontology. The operands are accepted as a list of concept definitions and stored as-is, with no validation of the input — a deliberate choice that keeps the object a thin data holder and pushes integrity checking to the components that actually evaluate fuzzy membership degrees. The stored list is later exposed by reference rather than by copy, which avoids allocation overhead but means callers share mutable state with the instance, so any external modification is directly visible to the concept itself. A compact textual rendering of the form "(w-max ...)", produced by joining the string forms of the operands with spaces, makes the aggregate easy to inspect in logs and debug output without altering its state.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept.WeightedMaxConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_max_concept_WeightedMaxConcept.png
       :alt: UML Class Diagram for WeightedMaxConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedMaxConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_max_concept_WeightedMaxConcept.pdf
       :alt: UML Class Diagram for WeightedMaxConcept
       :align: center
       :width: 10.1cm
       :class: uml-diagram

       UML Class Diagram for **WeightedMaxConcept**

.. py:class:: WeightedMaxConcept(wc: list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_max_concept.WeightedMaxConcept
      :parts: 1
      :private-bases:


   This class models a specific fuzzy logic operator used within the FuzzyOWL2 ontology framework, designed to represent a weighted maximum aggregation over a set of concepts. It functions by accepting a list of `ConceptDefinition` objects during initialization, which serve as the operands for the aggregation logic. As a subclass of `ConceptDefinition`, it integrates seamlessly into the type system by registering itself as a `WEIGHTED_MAX` entity, allowing the system to distinguish it from other logical constructs. The stored concepts can be accessed via the `get_weighted_concepts` method, enabling further processing or evaluation of the fuzzy membership degrees associated with the weighted maximum operation.

   :param _wc: The list of concept definitions that are combined using the weighted maximum operator.
   :type _wc: list[ConceptDefinition]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the weighted maximum concept, formatted as a parenthesized list prefixed with 'w-max'. The internal components stored in the `_wc` attribute are converted to strings and joined by spaces to populate the content within the parentheses. This representation is useful for logging, debugging, or displaying the object's current state without modifying it.

      :return: A string representation of the object formatted as "(w-max ...)" with space-separated internal components.

      :rtype: str



   .. py:method:: get_weighted_concepts() -> list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]

      Returns the internal collection of weighted concepts stored within the instance. This method provides direct access to the list of `ConceptDefinition` objects, allowing the caller to inspect the current set of concepts. Because a reference to the internal list is returned rather than a copy, any modifications made to the list by the caller will directly affect the state of the object.

      :return: A list of ConceptDefinition objects representing the weighted concepts.

      :rtype: list[ConceptDefinition]



   .. py:attribute:: _wc
      :type:  list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]
