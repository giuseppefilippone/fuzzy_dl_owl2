fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition
====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class representing concept definitions within the FuzzyOWL2 framework.


Description
-----------


Designed to serve as a foundational interface for various fuzzy logic constructs, this class enforces a standard structure for concept definitions by requiring a specific classification upon initialization. Subclasses are expected to inherit from this base to implement specific behaviors, while the base class itself manages the storage and retrieval of the associated ``ConceptType`` enumeration. By encapsulating the type information and providing an accessor method, the design ensures that every concept definition can be categorized and identified consistently throughout the system. The implementation relies on Python's abstract base class module to prevent direct instantiation, thereby guiding developers to create concrete implementations for specific logical scenarios.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_concept_definition_ConceptDefinition.png
       :alt: UML Class Diagram for ConceptDefinition
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ConceptDefinition**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_concept_definition_ConceptDefinition.pdf
       :alt: UML Class Diagram for ConceptDefinition
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **ConceptDefinition**

.. py:class:: ConceptDefinition(type: fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType)

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition
      :parts: 1
      :private-bases:


   This abstract base class serves as the foundational representation for concept definitions within the FuzzyOWL2 framework. It is designed to be subclassed rather than instantiated directly, providing a common interface for various types of fuzzy concept definitions. Upon initialization, a specific `ConceptType` must be provided to categorize the nature of the definition, which can subsequently be retrieved using the `get_type` method.

   :param _type: The specific classification or category of the fuzzy concept definition.
   :type _type: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType


   .. py:method:: __repr__() -> str

      Returns the official string representation of the `ConceptDefinition` instance. This method delegates directly to the `__str__` method, ensuring that the output used for debugging and logging is identical to the informal string representation provided by the object.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: get_type() -> fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType

      Returns the type classification associated with this concept definition. This method acts as an accessor for the internal `_type` attribute, providing the specific `ConceptType` that categorizes the concept. It does not modify the state of the object.

      :return: The type of the concept.

      :rtype: fuzzy_dl_owl2.fuzzydl.util.constants.ConceptType



   .. py:attribute:: _type
      :type:  fuzzy_dl_owl2.fuzzyowl2.util.constants.ConceptType

