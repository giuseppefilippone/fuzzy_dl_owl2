fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized definition for Ordered Weighted Averaging operations within the FuzzyOWL2 framework that aggregates fuzzy concepts using a specific set of weights.


Description
-----------


Extending the base definition structure, this implementation encapsulates the logic required to perform Ordered Weighted Averaging by storing a sequence of numerical coefficients alongside a collection of fuzzy concept identifiers. During initialization, the entity registers itself specifically as an OWA type and retains direct references to the provided lists of weights and concepts, allowing for external modification without defensive copying. Accessor methods expose the internal state, enabling the retrieval of the weighting vector and the associated terms to facilitate the calculation of aggregated fuzzy values. A string representation is provided to serialize the configuration into a parenthesized syntax, ensuring the operator can be easily read or processed by other components of the system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept.OwaConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_owa_concept_OwaConcept.png
       :alt: UML Class Diagram for OwaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **OwaConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_owa_concept_OwaConcept.pdf
       :alt: UML Class Diagram for OwaConcept
       :align: center
       :width: 10.6cm
       :class: uml-diagram

       UML Class Diagram for **OwaConcept**

.. py:class:: OwaConcept(weights: list[float], concepts: list[str])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept.OwaConcept
      :parts: 1
      :private-bases:


   This class models an Ordered Weighted Averaging (OWA) operation within the FuzzyOWL2 framework, serving as a specialized definition for fuzzy logic concepts. It encapsulates the parameters necessary to perform the aggregation, specifically a sequence of floating-point weights and a list of associated fuzzy concept identifiers. By inheriting from the base definition type, it integrates into the broader ontology structure while providing specific accessors to retrieve the weights and concepts, as well as a string representation formatted for the specific syntax of the system.

   :param _weights: Coefficients used to calculate the ordered weighted average of the fuzzy concepts.
   :type _weights: list[float]
   :param _concepts: The fuzzy concepts to be aggregated by the OWA operator.
   :type _concepts: list[str]


   .. py:method:: __str__() -> str

      Returns a string representation of the OWA concept formatted as a parenthesized expression. The output follows the structure "(owa (weights) (concepts))", where the internal weights are converted to strings and joined by spaces, and the concept labels are similarly concatenated. This representation is intended to provide a human-readable summary of the aggregation operator's configuration and associated terms.

      :return: A string representation of the object in the format `(owa (weights) (concepts))`.

      :rtype: str



   .. py:method:: get_concepts() -> list[str]

      Retrieves the list of concepts associated with the OwaConcept instance. This method returns the value of the internal `_concepts` attribute, which is a list of strings. It serves as a simple accessor to expose the stored concept data without altering the object's state.

      :return: A list of strings representing the concepts associated with this object.

      :rtype: list[str]



   .. py:method:: get_weights() -> list[float]

      Retrieves the list of floating-point weights used by the OWA operator to calculate the aggregated value. This method returns a direct reference to the internal `_weights` attribute, meaning that any modifications made to the returned list will alter the state of the object itself. It is typically used to inspect or externally manipulate the weighting criteria without invoking specific setter logic.

      :return: A list of float values representing the weights.

      :rtype: list[float]



   .. py:attribute:: _concepts
      :type:  list[str]


   .. py:attribute:: _weights
      :type:  list[float]

