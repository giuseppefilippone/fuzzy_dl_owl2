fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept
======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.quasi_sugeno_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a quasi-Sugeno integral concept for FuzzyOWL2 ontologies, holding the numeric weights and fuzzy concept names that together specify a weighted fuzzy aggregation.


Description
-----------


Quasi-Sugeno integrals are fuzzy aggregation operators that blend several fuzzy concepts into a single weighted result, and the ``QsugenoConcept`` class models such an operator as a specialised kind of concept definition within the FuzzyOWL2 framework. By registering itself under the QUASI_SUGENO concept type at construction time, the object becomes recognisable to the wider ontology toolkit, which can dispatch on that type when serialising or reasoning over fuzzy axioms. The constructor simply stores the parallel lists of floating-point weights and concept identifiers without any validation, so the responsibility for supplying consistent, well-formed inputs rests entirely with the caller. Read access is provided through lightweight getters that return direct references to the internal lists rather than copies, which keeps queries cheap but means external code could inadvertently mutate the object's state. The string representation renders the whole construct in the parenthesised functional syntax used throughout FuzzyOWL2 — the operator name followed by the space-separated weights and then the concepts — making the object directly usable for export into ontology documents or for human-readable debugging. The design is intentionally that of a plain data holder: it carries no aggregation logic of its own, deferring the actual fuzzy computation to whatever component consumes these definitions.

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

