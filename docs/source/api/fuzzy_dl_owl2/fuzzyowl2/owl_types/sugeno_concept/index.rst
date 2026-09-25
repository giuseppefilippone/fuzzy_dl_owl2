fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a Sugeno fuzzy integral concept for the FuzzyOWL2 framework by pairing a list of numeric weights with the fuzzy concepts they aggregate.


Description
-----------


SugenoConcept extends the base ConceptDefinition abstraction and registers itself with the SUGENO concept type, allowing the rest of the ontology tooling to recognise it as an aggregation operator based on a Sugeno integral rather than an ordinary concept definition. It holds two parallel collections: floating-point weights that express the relative importance (the fuzzy densities) of each participating concept, and string identifiers naming those concepts, so that several fuzzy concepts can be combined into a single aggregated concept. The weights and concepts are expected to correspond positionally, and the accessors return direct references to the internal lists rather than copies, meaning callers who mutate the returned collections will change the object's underlying state. The string representation serialises the definition as a parenthesised, S-expression-like *sugeno* operator that prints the weights and concepts in matching order, producing output that is both human-readable and machine-parsable for display or export. Design-wise it is a lightweight, purely declarative data holder: it performs no aggregation arithmetic itself, instead serving as a typed container that the surrounding fuzzy description-logic reasoning and serialisation machinery can interpret.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept.SugenoConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_sugeno_concept_SugenoConcept.png
       :alt: UML Class Diagram for SugenoConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **SugenoConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_sugeno_concept_SugenoConcept.pdf
       :alt: UML Class Diagram for SugenoConcept
       :align: center
       :width: 10.6cm
       :class: uml-diagram

       UML Class Diagram for **SugenoConcept**

.. py:class:: SugenoConcept(weights: list[float], concepts: list[str])

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept.SugenoConcept
      :parts: 1
      :private-bases:


   This class models a Sugeno fuzzy integral concept within the FuzzyOWL2 framework, acting as a specialized definition that aggregates multiple fuzzy concepts based on a corresponding set of weights. It extends the base `ConceptDefinition` and requires initialization with two parallel lists: a sequence of floating-point values representing the weights and a sequence of strings identifying the specific fuzzy concepts to be combined. Once instantiated, the object provides methods to retrieve the weights and concepts, and it defines a string representation that formats the data into a standard Sugeno operator expression for serialization or display.

   :param _weights: Coefficients representing the relative importance or contribution of the corresponding fuzzy concepts in the Sugeno model.
   :type _weights: list[float]
   :param _concepts: The fuzzy concepts that are aggregated within the Sugeno concept.
   :type _concepts: list[str]


   .. py:method:: __str__() -> str

      Returns a string representation of the object formatted as a parenthesized expression, resembling an S-expression. The output string begins with the 'sugeno' identifier, followed by a space-separated list of the internal weights converted to strings, and concludes with a space-separated list of the associated concepts. This representation is primarily intended for displaying the current state of the fuzzy measure and its components in a readable or parsable format.

      :return: A string representation of the object, formatted as a Sugeno expression containing the weights and concepts.

      :rtype: str



   .. py:method:: get_concepts() -> list[str]

      Retrieves the list of linguistic concepts or labels associated with this instance. This method provides direct access to the internal `_concepts` attribute, returning the list of strings that define the terms used in the Sugeno model. As the method returns a reference to the internal list, modifying the returned collection may inadvertently alter the state of the object.

      :return: A list of strings representing the concepts stored in the object.

      :rtype: list[str]



   .. py:method:: get_weights() -> list[float]

      Retrieves the list of weights associated with the Sugeno concept, which represent the importance values used in fuzzy integration calculations. This method returns a direct reference to the internal list of floating-point numbers, meaning modifications to the returned list will alter the object's internal state.

      :return: A list of floating-point numbers representing the weights.

      :rtype: list[float]



   .. py:attribute:: _concepts
      :type:  list[str]


   .. py:attribute:: _weights
      :type:  list[float]

