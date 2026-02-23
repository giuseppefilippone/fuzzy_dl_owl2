fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept
==================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a specialized logical entity representing a concept altered by a fuzzy modifier or linguistic hedge within the FuzzyOWL2 framework.


Description
-----------


Extending the base definition structure, this implementation captures the nuance of graded logical expressions by associating a specific linguistic hedge with a standard concept name. The design encapsulates two distinct string components, the modifier and the underlying concept, ensuring that the semantic relationship between them is preserved within the object's state. Accessor methods allow external logic to retrieve these individual components, while the string representation standardizes the output to a parenthesized format for easy parsing or display. By explicitly tagging the entity as a modified concept type, the integration ensures that downstream processing can distinguish these nuanced definitions from unmodified atomic concepts.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept.ModifiedConcept


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_modified_concept_ModifiedConcept.png
       :alt: UML Class Diagram for ModifiedConcept
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **ModifiedConcept**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_modified_concept_ModifiedConcept.pdf
       :alt: UML Class Diagram for ModifiedConcept
       :align: center
       :width: 7.6cm
       :class: uml-diagram

       UML Class Diagram for **ModifiedConcept**

.. py:class:: ModifiedConcept(mod: str, c: str)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.concept_definition.ConceptDefinition`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.modified_concept.ModifiedConcept
      :parts: 1
      :private-bases:


   This entity encapsulates a concept within the FuzzyOWL2 framework that has been altered by a specific fuzzy modifier, such as a linguistic hedge. It acts as a specialized definition that combines a base concept name with a modifier to represent nuanced or graded logical expressions. To use this class, instantiate it by providing the modifier string and the concept string as arguments. Once created, the object allows retrieval of the modifier and the underlying concept through dedicated accessor methods, and it provides a string representation formatted as `(modifier concept)`.

   :param _mod: The fuzzy modifier (linguistic hedge) applied to the concept.
   :type _mod: str
   :param _c: The name of the concept to which the fuzzy modifier is applied.
   :type _c: str


   .. py:method:: __str__() -> str

      Generates a human-readable string representation of the instance, formatted as a parenthesized pair containing the modifier and the underlying concept separated by a space. This method is implicitly called by the `str()` built-in and print functions, relying on the internal `_mod` and `_c` attributes to be convertible to strings. The operation is read-only and does not alter the state of the object.

      :return: A string representation of the object formatted as "(_mod _c)".

      :rtype: str



   .. py:method:: get_fuzzy_concept() -> str

      Retrieves the underlying string representation of the fuzzy concept stored within the instance. This method acts as a getter for the internal attribute `_c`, providing direct access to the core data without altering the object's state. It is the primary mechanism for obtaining the textual value associated with the modified concept.

      :return: The fuzzy concept associated with the object.

      :rtype: str



   .. py:method:: get_fuzzy_modifier() -> str

      Retrieves the fuzzy modifier string associated with the current concept instance. This value represents the specific nuance or qualification applied to the concept, distinguishing it from a standard definition. The method performs a direct lookup of the internal attribute and does not modify the state of the object.

      :return: The string representing the fuzzy modifier.

      :rtype: str



   .. py:attribute:: _c
      :type:  str


   .. py:attribute:: _mod
      :type:  str

