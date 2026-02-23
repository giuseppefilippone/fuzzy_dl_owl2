fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition
====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition



.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class that establishes a common interface for representing fuzzy concept definitions within the FuzzyOWL2 framework.


Description
-----------


Designed to serve as a structural blueprint, it ensures that all derived implementations share a consistent mechanism for identifying their specific category through a mandatory type parameter. By enforcing the provision of a ``ConceptType`` during initialization, the design guarantees that every concrete definition is explicitly categorized, which aids in the semantic processing of fuzzy logic rules. Access to this categorization is provided through a dedicated accessor method, allowing other components of the system to determine the nature of a concept without needing to understand its internal structure. The implementation leverages Python's Abstract Base Class module to prevent direct instantiation, thereby ensuring that only specialized subclasses representing specific logical constructs are utilized throughout the application.

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

