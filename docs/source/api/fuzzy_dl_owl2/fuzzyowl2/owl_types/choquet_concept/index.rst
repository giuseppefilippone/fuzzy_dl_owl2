fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized implementation of a fuzzy concept definition that aggregates multiple sub-concepts using the Choquet integral based on a set of fuzzy measure weights.


Description
-----------


Extending the base definition for concepts, this component models fuzzy logic constructs that rely on the Choquet integral for aggregation. It encapsulates a collection of numerical weights representing a fuzzy measure alongside a list of corresponding concept identifiers, allowing the system to define complex relationships where the importance of concept subsets is explicitly quantified. The design prioritizes direct storage and retrieval of these parameters, enabling downstream processing or serialization without immediate validation of the input data integrity. Furthermore, it provides a string representation that adheres to a specific parenthesized syntax, facilitating the export or display of the fuzzy logic structure in a human-readable format.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept.ChoquetConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_choquet_concept_ChoquetConcept.png
       :alt: UML Class Diagram for ChoquetConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ChoquetConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_choquet_concept_ChoquetConcept.pdf
       :alt: UML Class Diagram for ChoquetConcept
       :align: center
       :width: 10.6cm
       :class: uml-diagram

       UML Class Diagram for **ChoquetConcept**

.. py:class:: ChoquetConcept(weights: list[float], concepts: list[str])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.choquet_concept.ChoquetConcept
      :parts: 1
      :private-bases:


   This entity models a fuzzy concept defined via the Choquet integral within the FuzzyOWL2 framework, serving as a specialized implementation of a concept definition. It encapsulates the logic for aggregating multiple underlying concepts using a specific set of weights that represent the importance of various subsets of those concepts. To utilize this structure, instantiate it with a list of floating-point values representing the fuzzy measure weights and a corresponding list of strings identifying the concepts to be aggregated. Once initialized, the object provides methods to retrieve the weights and concept identifiers, and it formats its internal state into a specific string syntax for serialization or display.

   :param _weights: Numerical values determining the contribution of the associated concepts in the Choquet integral.
   :type _weights: list[float]
   :param _concepts: The list of concept identifiers that are aggregated to form the Choquet concept.
   :type _concepts: list[str]


   .. py:method:: __str__() -> str

      Returns a formatted string representation of the instance, encapsulating the internal weights and concepts within a parenthesized syntax starting with the 'choquet' identifier. The weights are explicitly converted to strings and joined by spaces, while the concepts are joined directly, implying that the internal concept list must consist of string objects to avoid a TypeError. This method is intended for display or logging purposes and has no side effects on the object's state.

      :return: A string representation of the object formatted as (choquet weights concepts).

      :rtype: str



   .. py:method:: get_concepts() -> list[str]

      Retrieves the list of concepts associated with the current instance. This method acts as a simple accessor, returning the internal `_concepts` attribute directly. Because it returns a reference to the underlying list rather than a copy, any modifications made to the returned list will affect the internal state of the object.

      :return: A list of strings representing the concepts associated with this object.

      :rtype: list[str]



   .. py:method:: get_weights() -> list[float]

      Returns the list of floating-point weights currently stored within the Choquet concept instance. These weights typically represent the fuzzy measure or capacity values used for aggregation. The method provides direct access to the internal `_weights` attribute; therefore, modifying the returned list in-place will alter the internal state of the object.

      :return: A list of floating-point numbers representing the weights.

      :rtype: list[float]



   .. py:attribute:: _concepts
      :type:  list[str]


   .. py:attribute:: _weights
      :type:  list[float]

