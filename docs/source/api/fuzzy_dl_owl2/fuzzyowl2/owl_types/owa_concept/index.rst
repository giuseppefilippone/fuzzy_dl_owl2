fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept
=============================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.owa_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a specialized data structure for representing Ordered Weighted Averaging (OWA) operations in fuzzy logic ontologies.


Description
-----------


The implementation extends the base definition for ontology concepts to support complex aggregation logic required by fuzzy reasoning. It encapsulates a weighting vector and a collection of concept identifiers, which together define how multiple fuzzy values are combined using the OWA operator. By storing these parameters directly, the structure allows the broader system to evaluate the weighted average of specified concepts without enforcing strict mathematical constraints on the input data, such as ensuring the weights sum to unity. Additionally, the logic includes a string serialization method that formats the internal state into a specific parenthetical syntax, facilitating easy parsing or display within the FuzzyOWL2 environment.

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

