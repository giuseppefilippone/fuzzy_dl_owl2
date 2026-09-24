fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property







.. ── LLM-GENERATED DESCRIPTION START ──

Defines a ``ModifiedProperty`` class that pairs a fuzzy property with a linguistic modifier, such as "very" or "somewhat", within the FuzzyOWL2 framework.


Description
-----------


The class models the situation where a fuzzy relationship is qualified by a hedge that alters the degree of truth with which the underlying property holds, a common construct in fuzzy ontologies for expressing graded knowledge. At construction time it simply stores two strings — the modifier and the name of the property being modified — and deliberately performs no validation or transformation, keeping the object a lightweight, passive data carrier that other parts of the framework, such as ontology serialization or reasoning routines, can query through its getter methods. Inheriting from ``FuzzyProperty`` allows modified properties to be treated polymorphically wherever a generic fuzzy property is expected, which is the key design decision enabling them to flow through the rest of the type hierarchy unchanged. Both the informal and official string representations render the object as a parenthesized pair, "(modifier property)", so that modified properties can be embedded naturally in human-readable renderings of a fuzzy ontology; notably, ``__repr__`` delegates to ``__str__``, meaning the two representations are identical and display-oriented rather than machine-parseable.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property.ModifiedProperty


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_modified_property_ModifiedProperty.png
       :alt: UML Class Diagram for ModifiedProperty
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ModifiedProperty**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_modified_property_ModifiedProperty.pdf
       :alt: UML Class Diagram for ModifiedProperty
       :align: center
       :width: 7.3cm
       :class: uml-diagram

       UML Class Diagram for **ModifiedProperty**

.. py:class:: ModifiedProperty(mod: str, prop: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_property.FuzzyProperty`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property.ModifiedProperty
      :parts: 1
      :private-bases:


   This class models a property within the FuzzyOWL2 framework that has been subjected to a fuzzy modification, effectively combining a standard property with a linguistic hedge or modifier. It extends the base `FuzzyProperty` to allow for the representation of nuanced relationships where the property's truth value is altered by a specific factor, such as "very" or "somewhat." To use this class, instantiate it by providing the fuzzy modifier as a string and the name of the property to be modified. The resulting object stores these values and offers methods to retrieve the specific modifier and the underlying property, while its string representation formats the pair as a parenthesized tuple.

   :param _mod: The fuzzy modifier applied to the property.
   :type _mod: str
   :param _prop: The name of the underlying property to which the fuzzy modifier is applied.
   :type _prop: str


   .. py:method:: __repr__() -> str

      Returns the official string representation of the object by delegating to the informal string conversion method. This implementation invokes `str(self)`, ensuring that the output matches the result of the `__str__` method rather than providing a distinct, machine-parseable representation. Consequently, the returned value is primarily intended for display purposes and may not be sufficient to reconstruct the object instance.

      :return: The string representation of the object.

      :rtype: str



   .. py:method:: __str__() -> str

      Returns a human-readable string representation of the object, formatted as a parenthesized pair containing the fuzzy modifier followed by the property. This method is invoked automatically by the print function and string conversion operations, relying on the current state of the instance without modifying any internal data. The specific values displayed are determined by calling the respective getter methods for the fuzzy modifier and the property.

      :return: A string representation of the object in the format "(fuzzy_modifier property)".

      :rtype: str



   .. py:method:: get_fuzzy_modifier() -> str

      Retrieves the fuzzy modifier string associated with this property instance. This method serves as a getter for the internal `_mod` attribute, returning the value that defines the specific modification or matching rule applied to the property. As a read-only operation, it has no side effects on the object's state, though it may raise an `AttributeError` if the underlying attribute has not been initialized.

      :return: The string representing the fuzzy modifier.

      :rtype: str



   .. py:method:: get_property() -> str

      Retrieves the value stored in the internal `_prop` attribute. This method acts as a simple accessor to expose the underlying property data without modifying the state of the instance. It assumes the internal attribute has been initialized; otherwise, an `AttributeError` will be raised.

      :return: The value of the internal property.

      :rtype: str



   .. py:attribute:: _mod
      :type:  str


   .. py:attribute:: _prop
      :type:  str