fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a data structure that associates a numerical weight with a fuzzy concept identifier within the FuzzyOWL2 ontology language.


Description
-----------


The implementation extends the base definition for concepts to support degrees of membership or importance by pairing a floating-point value with a specific concept label. During initialization, the object explicitly registers itself as a weighted entity within the system hierarchy while encapsulating the numerical and textual data as private attributes to ensure data integrity. Accessor methods allow external components to retrieve the stored weight and concept identifier without modifying the internal state, facilitating read-only interactions with the fuzzy logic data. A string representation is provided to display the combined weight and concept in a parenthesized format, which aids in debugging and logging by presenting a human-readable summary of the entity's current state.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept.WeightedConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_concept_WeightedConcept.png
       :alt: UML Class Diagram for WeightedConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **WeightedConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_weighted_concept_WeightedConcept.pdf
       :alt: UML Class Diagram for WeightedConcept
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **WeightedConcept**

.. py:class:: WeightedConcept(n: float, c: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.weighted_concept.WeightedConcept
      :parts: 1
      :private-bases:


   This class models a weighted concept as defined in the FuzzyOWL2 ontology language, serving as a concrete implementation of `ConceptDefinition`. It encapsulates a relationship between a numerical weight and a named fuzzy concept, allowing for the representation of degrees of membership or importance associated with that concept. To utilize this class, instantiate it with a float for the weight and a string for the concept name; the stored values can then be accessed via the `get_number` and `get_fuzzy_concept` methods. The class also provides a string representation that displays the weight and concept name in a parenthesized format.

   :param _n: The numerical weight associated with the fuzzy concept.
   :type _n: float
   :param _c: The name or identifier of the fuzzy concept associated with the weight.
   :type _c: str


   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the weighted concept, formatted as a parenthesized pair containing the numeric weight and the concept identifier. This method is automatically invoked by the built-in `str()` function and print operations, ensuring the object is displayed clearly as "(weight concept)" without modifying the object's internal state.

      :return: A string representation of the object in the format '(_n _c)'.

      :rtype: str



   .. py:method:: get_fuzzy_concept() -> str

      Retrieves the string representation of the fuzzy concept associated with this instance. This method acts as a simple accessor for the internal attribute `_c`, returning the specific concept label or identifier without modifying the object's state. As this is a read-only operation, it has no side effects and simply exposes the value stored during the object's initialization.

      :return: The fuzzy concept associated with the instance.

      :rtype: str



   .. py:method:: get_number() -> float

      Returns the underlying numeric value of the weighted concept by accessing the internal `_n` attribute. The value is returned as a float, representing the current weight or count associated with the instance. This is a read-only operation that does not modify the object's state or any external data.

      :return: The numeric value stored in the instance.

      :rtype: float



   .. py:attribute:: _c
      :type:  str


   .. py:attribute:: _n
      :type:  float

