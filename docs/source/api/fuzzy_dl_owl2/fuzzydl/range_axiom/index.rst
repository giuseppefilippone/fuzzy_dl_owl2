fuzzy_dl_owl2.fuzzydl.range_axiom
=================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.range_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a logical constraint that restricts the permissible types of individuals that can serve as the target of a specific role within a fuzzy description logic system.


Description
-----------


The implementation encapsulates the relationship between a named role and a concept, ensuring that any entity connected via this role adheres to the defined type restrictions. By storing the role identifier and the associated concept object, the structure facilitates the enforcement of domain rules where specific relationships must link to instances of particular classes. This component serves as a fundamental building block for knowledge representation, enabling the system to validate or reason about the properties and connections of entities based on logical constraints. The design relies on simple attribute storage to maintain the necessary context for semantic checks, integrating seamlessly with broader logic processing tasks.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.range_axiom.RangeAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_range_axiom_RangeAxiom.png
       :alt: UML Class Diagram for RangeAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **RangeAxiom**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_range_axiom_RangeAxiom.pdf
       :alt: UML Class Diagram for RangeAxiom
       :align: center
       :width: 9.0cm
       :class: uml-diagram

       UML Class Diagram for **RangeAxiom**

.. py:class:: RangeAxiom(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   This class represents a logical constraint used to define the permissible types of individuals that can be the target of a specific relationship or role. It enforces the rule that any individual related through the specified role must be an instance of the provided concept. To utilize this constraint, an instance is created by passing the role's identifier as a string and the corresponding concept object.

   :param role: The name of the role for which the range axiom is defined.
   :type role: str
   :param concept: The concept defining the range of the role, representing the set of individuals that can be related through it.
   :type concept: Concept


   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: role
      :type:  str

