fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier



.. ── LLM-GENERATED DESCRIPTION START ──

Defines an abstract base class that structures fuzzy modifiers acting as linguistic hedges to alter the membership degree of fuzzy concepts.


Description
-----------


Acting as a foundational contract within the FuzzyOWL2 framework, the abstract base class enforces a standard structure for linguistic hedges that mathematically adjust the truth values of fuzzy axioms. These modifiers serve to transform membership degrees through specific operations, such as intensifying a concept with terms like "very" or diluting it with terms like "somewhat." Because the definition is abstract, direct instantiation is impossible, requiring developers to subclass this component to provide concrete implementations that apply the necessary mathematical logic to fuzzy expressions.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_fuzzy_modifier_FuzzyModifier.png
       :alt: UML Class Diagram for FuzzyModifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **FuzzyModifier**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzyowl2_owl_types_fuzzy_modifier_FuzzyModifier.pdf
       :alt: UML Class Diagram for FuzzyModifier
       :align: center
       :width: 3.7cm
       :class: uml-diagram

       UML Class Diagram for **FuzzyModifier**

.. py:class:: FuzzyModifier

   Bases: :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier.FuzzyModifier
      :parts: 1
      :private-bases:


   This abstract base class defines the structure for fuzzy modifiers used within the FuzzyOWL2 framework, serving as a linguistic hedge that alters the membership degree of fuzzy concepts. It acts as a contract for implementing specific transformations, such as intensifiers like "very" or dilutors like "somewhat," which mathematically adjust the truth values of fuzzy axioms. Since this class is abstract, it cannot be instantiated directly; instead, it should be subclassed to create concrete modifier implementations that apply specific logic to fuzzy expressions.

