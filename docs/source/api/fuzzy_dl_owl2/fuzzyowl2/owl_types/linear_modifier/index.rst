fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier
=================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier







.. ── LLM-GENERATED DESCRIPTION START ──

A concrete fuzzy modifier that applies a linear transformation, parameterised by a single floating-point coefficient, to membership degrees within the FuzzyOWL2 framework.


Description
-----------


**LinearModifier** specialises the generic *FuzzyModifier* type for the simplest and most common kind of modifier: one whose effect on a fuzzy membership degree is fully determined by a single numeric constant. The coefficient is supplied at construction time, held as a private attribute, and exposed only through a read-only accessor, a design that makes instances effectively immutable and safe to share throughout the ontology model. Deliberately, no input validation or transformation logic lives inside the object itself; it acts purely as a carrier for the parameter, leaving the actual application of the linear function to the reasoning and serialisation machinery elsewhere in the framework. The string representation, rendered in the form "linear-modifier(c)", follows the textual conventions of FuzzyOWL2 so that the modifier can be written directly into ontology serialisations and human-readable debugging output. Because it derives from the shared base modifier class, instances can be handled polymorphically alongside other modifier families wherever modified fuzzy concepts are created, queried, or rendered.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier.LinearModifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_linear_modifier_LinearModifier.png
       :alt: UML Class Diagram for LinearModifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **LinearModifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_linear_modifier_LinearModifier.pdf
       :alt: UML Class Diagram for LinearModifier
       :align: center
       :width: 5.3cm
       :class: uml-diagram

       UML Class Diagram for **LinearModifier**

.. py:class:: LinearModifier(c: float)

   Bases: :py:obj:`fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.linear_modifier.LinearModifier
      :parts: 1
      :private-bases:


   Represents a specific type of fuzzy logic modifier that applies a linear transformation, typically used to scale or adjust membership degrees within the FuzzyOWL2 framework. To utilize this entity, instantiate it with a floating-point value that serves as the coefficient for the linear operation. Once instantiated, the coefficient can be retrieved using the provided accessor method, and the object provides a string representation indicating its type and value.

   :param _c: The numeric coefficient defining the linear transformation applied by the modifier.
   :type _c: float


   .. py:method:: __str__() -> str

      Returns the informal string representation of the `LinearModifier` instance, which is intended to be readable and concise. The output is formatted as "linear-modifier({c})", where {c} represents the string conversion of the internal coefficient stored in `_c`. This method does not alter the state of the object and is implicitly called by the built-in `str()` function and print operations.

      :return: A string representation of the linear modifier, formatted as 'linear-modifier(c)' where c is the coefficient.

      :rtype: str



   .. py:method:: get_c() -> float

      Retrieves the constant term 'c' currently stored in the linear modifier. This method returns the value of the private attribute `_c` as a floating-point number. It is a read-only operation that does not modify the object's state or have any side effects.

      :return: The value of the internal attribute `_c`.

      :rtype: float



   .. py:attribute:: _c
      :type:  float