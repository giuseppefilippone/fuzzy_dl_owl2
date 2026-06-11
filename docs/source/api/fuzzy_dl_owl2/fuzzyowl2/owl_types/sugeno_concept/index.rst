fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.sugeno_concept



.. ── LLM-GENERATED DESCRIPTION START ──

A specialized implementation of a fuzzy concept definition that models the Sugeno fuzzy integral by aggregating linguistic terms with corresponding numerical weights.


Description
-----------


Extending the base definition for fuzzy logic constructs, this component encapsulates the logic required to represent a Sugeno fuzzy integral, which is a non-linear aggregation operator used to combine multiple criteria based on their importance. The design relies on maintaining parallel lists of floating-point weights and string-based concept identifiers, ensuring that each weight corresponds directly to a specific concept within the aggregation model. During initialization, the entity explicitly identifies itself as a Sugeno type within the broader framework, allowing the system to distinguish this specific aggregation method from other fuzzy logic operations. For serialization and display purposes, the internal state is converted into a structured string format that resembles an S-expression, clearly delineating the operator type, the sequence of weights, and the associated concepts.

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

