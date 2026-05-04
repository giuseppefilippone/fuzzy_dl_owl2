fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property
===================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_property



.. ── LLM-GENERATED DESCRIPTION START ──

Represents a property within the FuzzyOWL2 framework that has been altered by a fuzzy modifier or linguistic hedge.


Description
-----------


Extending the base ``FuzzyProperty`` structure, this component enables the representation of nuanced relationships where a standard property is subjected to a linguistic hedge or fuzzy modifier. By accepting a modifier string and a property name during instantiation, the software captures the specific alteration applied to the relationship, allowing for distinctions such as "very" or "somewhat" to be preserved alongside the core property identifier. Internal storage maintains these two distinct elements, and dedicated accessors expose the underlying property and its associated modifier without modifying the object's state. String representations are generated to display the combined entity as a parenthesized pair, ensuring that the modified nature of the property is clearly communicated in textual outputs.

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

