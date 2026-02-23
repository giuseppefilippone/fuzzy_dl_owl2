fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept
==============================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized class representing a Quantified Ordered Weighted Averaging (OWA) concept within the FuzzyOWL2 ontology language.


Description
-----------


Extending the base definition for ontology concepts, this implementation models fuzzy logic operations where a set of concepts is aggregated according to a specific linguistic quantifier. The design allows for the representation of complex, weighted aggregations by storing a quantifier string alongside a collection of underlying concept identifiers. Upon initialization, the entity is registered as a QUANTIFIED_OWA type, ensuring it integrates correctly with the broader type system used for fuzzy logic reasoning. Accessor methods expose the internal state, while the string representation formats the data into a parenthetical syntax suitable for logical parsing or display.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept.QowaConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_qowa_concept_QowaConcept.png
       :alt: UML Class Diagram for QowaConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **QowaConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_qowa_concept_QowaConcept.pdf
       :alt: UML Class Diagram for QowaConcept
       :align: center
       :width: 8.3cm
       :class: uml-diagram

       UML Class Diagram for **QowaConcept**

.. py:class:: QowaConcept(q: str, concepts: list[str])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.qowa_concept.QowaConcept
      :parts: 1
      :private-bases:


   This class encapsulates the definition of a Quantified Ordered Weighted Averaging (OWA) concept as defined in the FuzzyOWL2 ontology language. It serves as a specialized implementation of `ConceptDefinition`, designed to model fuzzy logic operations where a set of concepts is aggregated based on a linguistic quantifier. Users can instantiate this class by supplying a string representing the quantifier and a list of strings corresponding to the underlying fuzzy concepts, allowing for the representation of complex, weighted aggregations within the system.

   :param _q: The quantifier defining the aggregation weights for the OWA concept.
   :type _q: str
   :param _concepts: The list of fuzzy concepts that are aggregated by the quantified OWA operator.
   :type _concepts: list[str]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the QowaConcept instance, formatted as a parenthetical expression beginning with the 'q-owa' identifier. The representation concatenates the string value of the internal quantifier `_q` and the sequence of concepts, which are joined by spaces. This method has no side effects and is intended for displaying the object's current state or for serialization into a specific logical syntax.

      :return: A string representation of the object in the format "(q-owa <q> <concepts>)".

      :rtype: str



   .. py:method:: get_concepts() -> list[str]

      Retrieves the list of concepts currently stored within the instance. This method provides direct access to the internal `_concepts` attribute, returning a list of strings. Since the reference to the internal list is returned rather than a copy, any modifications made to the returned list will directly alter the state of the object.

      :return: A list of strings representing the concepts associated with the object.

      :rtype: list[str]



   .. py:method:: get_quantifier() -> str

      Retrieves the quantifier associated with the current concept instance. This method returns the value of the internal `_q` attribute, representing the specific quantification logic or scope defined for the object. It is a read-only operation that exposes the stored string value without modifying the instance's state.

      :return: The quantifier string.

      :rtype: str



   .. py:attribute:: _concepts
      :type:  list[str]


   .. py:attribute:: _q
      :type:  str

