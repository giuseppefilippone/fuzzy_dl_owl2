fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition
=====================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.property_definition





.. ── LLM-GENERATED DESCRIPTION START ──

A minimal value object that binds a property name to its associated fuzzy modifier so the pair can travel together when expressing fuzzy axioms in the FuzzyOWL2 ontology framework.


Description
-----------


PropertyDefinition acts as a fundamental building block for fuzzy logic constraints by capturing the two pieces of information needed to attach a linguistic hedge to an object or data property: the modifier itself and the name of the property it applies to. Bundling these values into a single unit simplifies downstream code, since any component that constructs fuzzy axioms can retrieve both elements through dedicated getter methods rather than juggling loose strings. The design is deliberately minimal and defensive: the constructor performs no validation and simply stores the two strings in private attributes, while the absence of setter methods means instances effectively behave as immutable records once created. This immutability makes objects safe to pass around and reuse, and the getter-only interface preserves encapsulation by keeping the underlying attribute names hidden from callers. In practice, consumers instantiate the class with a modifier such as a linguistic hedge and a property name, then read both values back when translating fuzzy restrictions into concrete ontology axioms.

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
