fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates a property name and its associated fuzzy modifier to define linguistic hedges within the FuzzyOWL2 ontology framework.


Description
-----------


Designed to serve as a fundamental component for constructing fuzzy logic constraints, the implementation links a specific ontology property with a linguistic hedge or truth value. Maintaining the fuzzy modifier alongside the property identifier enables the precise application of logic that dictates how lenient or strict comparisons should be interpreted. Instantiation requires supplying the modifier and property strings, allowing the subsequent retrieval of these values to build complex fuzzy axioms while keeping the internal state encapsulated.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition.PropertyDefinition


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_property_definition_PropertyDefinition.png
       :alt: UML Class Diagram for PropertyDefinition
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **PropertyDefinition**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_property_definition_PropertyDefinition.pdf
       :alt: UML Class Diagram for PropertyDefinition
       :align: center
       :width: 7.3cm
       :class: uml-diagram

       UML Class Diagram for **PropertyDefinition**

.. py:class:: PropertyDefinition(mod: str, prop: str)

   Encapsulates a property name alongside its corresponding fuzzy modifier, serving as a fundamental building block for defining fuzzy logic constraints within the FuzzyOWL2 ontology framework. By storing these two elements together, it allows for the precise application of linguistic hedges or truth values to specific object or data properties. Users should instantiate this object by providing the modifier and property strings, and subsequently access the stored values via the dedicated getter methods to construct complex fuzzy axioms.

   :param _mod: The fuzzy modifier associated with the property definition.
   :type _mod: str
   :param _prop: The name of the property being defined.
   :type _prop: str


   .. py:method:: get_fuzzy_modifier() -> str

      Retrieves the specific string modifier used to define the fuzzy matching behavior for this property. This value is stored internally and determines how lenient or strict comparisons involving this property should be interpreted.

      :return: The string representing the fuzzy modifier.

      :rtype: str



   .. py:method:: get_property() -> str

      Returns the string value associated with this property definition. This method provides access to the internal `_prop` attribute, allowing the retrieval of the property's identifier or value without modifying the object's state. Since it directly accesses an internal attribute, it assumes the attribute has been properly initialized during object creation.

      :return: The value of the property.

      :rtype: str



   .. py:attribute:: _mod
      :type:  str


   .. py:attribute:: _prop
      :type:  str

