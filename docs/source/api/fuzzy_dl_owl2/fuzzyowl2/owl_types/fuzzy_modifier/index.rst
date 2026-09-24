fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier
================================================

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.owl_types.fuzzy_modifier







.. ── LLM-GENERATED DESCRIPTION START ──

An abstract base class, ``FuzzyModifier``, that establishes the contract for linguistic hedges which mathematically transform the membership degrees of fuzzy concepts within the FuzzyOWL2 framework.


Description
-----------


Fuzzy modifiers—linguistic hedges such as intensifiers like *very* and dilutors like *somewhat*—are the mechanism through which the FuzzyOWL2 framework adjusts the truth values attached to fuzzy concepts and axioms. By inheriting from Python's abstract base class machinery, ``FuzzyModifier`` deliberately provides no behaviour of its own and cannot be instantiated directly; it exists purely as a structural contract that concrete implementations are expected to fulfil. Subclasses supply the actual transformation logic applied to membership degrees, which keeps the framework extensible, since new hedges can be introduced simply by subclassing without altering the surrounding ontology-handling code. Centralising the modifier contract in a single abstraction also allows the rest of the fuzzy ontology machinery to treat every modifier uniformly, regardless of the particular mathematical function each one implements.

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