fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept
======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized definition that aggregates multiple fuzzy concepts into a weighted sum structure within the FuzzyOWL2 framework.


Description
-----------


Extending the base definition for fuzzy logic constructs, the software facilitates the creation of complex concepts by combining a collection of existing definitions into a single aggregated entity. It specifically targets scenarios where a concept is defined through a weighted summation, distinguishing this logical operation from other types of relationships within the ontology. During initialization, the entity is explicitly marked with a type identifier corresponding to a weighted sum, which allows reasoning engines or serialization tools to correctly interpret the structure. The stored collection of concepts can be retrieved for further processing, and the internal state is represented textually using a specific notation that encapsulates the components within a parenthesized prefix.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept.WeightedSumConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_sum_concept_WeightedSumConcept.png
       :alt: UML Class Diagram for WeightedSumConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedSumConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_sum_concept_WeightedSumConcept.pdf
       :alt: UML Class Diagram for WeightedSumConcept
       :align: center
       :width: 10.1cm
       :class: uml-diagram

       UML Class Diagram for **WeightedSumConcept**

.. py:class:: WeightedSumConcept(wc: list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_sum_concept.WeightedSumConcept
      :parts: 1
      :private-bases:


   This class represents a weighted sum concept within the FuzzyOWL2 framework, serving as a specialized definition that aggregates multiple underlying concepts. It is utilized to construct complex fuzzy concepts by combining a list of existing `ConceptDefinition` objects, which act as the components of the summation. Upon instantiation, the class initializes itself with the specific concept type `WEIGHTED_SUM` and stores the provided list of concepts, allowing them to be retrieved later via the `get_weighted_concepts` method for further processing or serialization.

   :param _wc: Collection of concept definitions that comprise the weighted sum.
   :type _wc: list[ConceptDefinition]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the concept, formatted as a parenthesized expression prefixed with 'w-sum'. The internal components are converted to strings and joined by spaces within the parentheses. This method does not modify the object's state and handles empty component lists by returning the prefix with an empty body.

      :return: A string representation of the object, formatted as '(w-sum ...)' containing the space-separated elements of the internal collection.

      :rtype: str



   .. py:method:: get_weighted_concepts() -> list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]

      Retrieves the list of concept definitions that are used to calculate the weighted sum for this instance. The method returns the internal list of concepts directly, providing access to the underlying data structure. Because a reference to the internal list is returned, any modifications made to the list or its elements will be reflected in the state of the object.

      :return: A list of weighted concept definitions.

      :rtype: list[ConceptDefinition]



   .. py:attribute:: _wc
      :type:  list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]

