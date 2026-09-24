fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept
======================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept





.. ── LLM-GENERATED DESCRIPTION START ──

Defines a weighted minimum aggregation operator that combines several fuzzy concept definitions into a single composite fuzzy concept within the FuzzyOWL2 framework.


Description
-----------


**WeightedMinConcept** is one of the aggregation operators offered by the fuzzy extension of OWL 2, letting ontology designers build complex concepts whose membership degree is intended to be evaluated as a weighted minimum over a collection of sub-concepts. It derives from the shared base class for concept definitions and registers itself with the *weighted minimum* concept type at construction time, which is how the rest of the framework distinguishes it from sibling operators such as weighted maximum or weighted sum when parsing, serialising, or reasoning over fuzzy ontologies. The operands are supplied as a list of concept definitions and stored exactly as given, with no validation performed in the constructor, so responsibility for well-formed input rests entirely with the caller; the same philosophy carries over to the accessor, which returns a direct reference to the internal list rather than a defensive copy, meaning any mutation by external code is immediately reflected in the object's state. A human-readable rendering is produced by joining the string forms of the operands inside a ``(w-min ...)`` wrapper, mirroring the concrete syntax used for fuzzy concept expressions and keeping printed output compact. Overall, the class is a deliberately thin, data-centric holder: it captures the structure of the aggregation and its textual presentation, while the actual weighted minimum computation is left to the downstream reasoning and serialisation machinery.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept.WeightedMinConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_min_concept_WeightedMinConcept.png
       :alt: UML Class Diagram for WeightedMinConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedMinConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_min_concept_WeightedMinConcept.pdf
       :alt: UML Class Diagram for WeightedMinConcept
       :align: center
       :width: 10.1cm
       :class: uml-diagram

       UML Class Diagram for **WeightedMinConcept**

.. py:class:: WeightedMinConcept(wc: list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_min_concept.WeightedMinConcept
      :parts: 1
      :private-bases:


   This class models a weighted minimum aggregation operator within the FuzzyOWL2 framework, designed to construct complex fuzzy concepts by combining a collection of sub-concepts. To use it, instantiate the object with a list of `ConceptDefinition` instances that represent the components to be aggregated. The class provides access to these components through a getter method and generates a string representation that visually denotes the weighted minimum operation.

   :param _wc: Collection of concept definitions that constitute the operands of the weighted minimum operation.
   :type _wc: list[ConceptDefinition]


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the weighted minimum concept, formatted as a parenthetical expression starting with the prefix "w-min". The method joins the string representations of the elements stored in the internal `_wc` attribute with spaces to form the content of the expression. This operation does not modify the object's state and depends on the string conversion behavior of the individual elements within the internal collection.

      :return: Returns a readable string representation of the object, formatted as "(w-min ...)" with the internal components space-separated.

      :rtype: str



   .. py:method:: get_weighted_concepts() -> list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]

      Retrieves the internal collection of concept definitions that have been weighted and processed by this instance. The method returns a list of `ConceptDefinition` objects representing the current state of the weighted concepts. Since this method returns a direct reference to the internal list, any modifications made to the list by the caller will immediately affect the internal state of the object.

      :return: A list of weighted concept definitions associated with the object.

      :rtype: list[ConceptDefinition]



   .. py:attribute:: _wc
      :type:  list[fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition]
