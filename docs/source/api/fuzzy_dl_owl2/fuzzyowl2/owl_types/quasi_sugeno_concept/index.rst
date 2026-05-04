fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept
======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Implements a data structure for handling quasi-Sugeno integral concepts within a fuzzy ontology framework.


Description
-----------


The software defines a specialized component that models the quasi-Sugeno integral, a fuzzy logic operator used for weighted aggregation of multiple criteria. By extending a base definition class, it encapsulates a collection of numerical weights alongside a corresponding list of concept identifiers to represent the importance and structure of the aggregated elements. The implementation ensures that the specific operator type is registered during initialization and exposes the internal data through accessor methods to support downstream logical processing. Furthermore, the logic includes a string serialization mechanism that formats the weights and concepts into a parenthetical expression suitable for parsing or display within the broader system.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept.QsugenoConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_quasi_sugeno_concept_QsugenoConcept.png
       :alt: UML Class Diagram for QsugenoConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **QsugenoConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_quasi_sugeno_concept_QsugenoConcept.pdf
       :alt: UML Class Diagram for QsugenoConcept
       :align: center
       :width: 10.6cm
       :class: uml-diagram

       UML Class Diagram for **QsugenoConcept**

.. py:class:: QsugenoConcept(weights: list[float], concepts: list[str])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept.QsugenoConcept
      :parts: 1
      :private-bases:


   Represents a specific type of fuzzy logic operator known as a quasi-Sugeno integral within the FuzzyOWL2 ontology framework. It extends the base concept definition to encapsulate a weighted aggregation of multiple fuzzy concepts, requiring a list of numerical weights and a corresponding list of concept identifiers upon initialization. The structure provides access to these components via getter methods and formats the data into a specific parenthetical string representation for serialization or logical processing.

   :param _weights: The coefficients weighting the fuzzy concepts in the quasi-Sugeno aggregation.
   :type _weights: list[float]
   :param _concepts: The fuzzy concepts that are aggregated within this quasi-Sugeno concept.
   :type _concepts: list[str]


   .. py:method:: __str__() -> str

      Returns a formatted string representation of the Q-sugeno concept, structured as a parenthetical expression. The output string begins with the 'q-sugeno' identifier, followed by a space-separated sequence of the internal weights converted to strings. It concludes with a space-separated list of the underlying concepts. This method is primarily intended for generating a human-readable or serialized view of the object's state without modifying the underlying data.

      :return: A string representation of the object in the format '(q-sugeno (weights...) (concepts...))'.

      :rtype: str



   .. py:method:: get_concepts() -> list[str]

      Returns the list of concepts stored in the `QsugenoConcept` instance. This method provides direct access to the internal `_concepts` attribute, which contains the collection of string-based concepts. As the method returns a reference to the underlying list rather than a copy, any modifications made to the returned list will directly alter the object's internal state.

      :return: A list of strings representing the concepts associated with this instance.

      :rtype: list[str]



   .. py:method:: get_weights() -> list[float]

      Retrieves the list of weights associated with the Sugeno concept. This method acts as a getter for the internal `_weights` attribute, returning the floating-point values that define the importance or density of the criteria. The operation is read-only and does not alter the state of the object.

      :return: A list of floating-point numbers representing the weights.

      :rtype: list[float]



   .. py:attribute:: _concepts
      :type:  list[str]


   .. py:attribute:: _weights
      :type:  list[float]

