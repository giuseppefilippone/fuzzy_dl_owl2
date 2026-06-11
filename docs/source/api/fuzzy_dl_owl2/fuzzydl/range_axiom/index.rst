fuzzy_dl_owl2.fuzzydl.range_axiom
=================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.range_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates a range axiom to enforce that individuals related by a specific role must belong to a defined concept.


Description
-----------


The software implements a structural component used within fuzzy description logics to define the permissible range of values for a specific role or relationship. By associating a string identifier representing a role with a specific concept object, the logic ensures that any individual connected via this relationship is an instance of the defined concept. This mechanism serves as a fundamental building block for knowledge representation, enabling the validation of entity relationships and supporting reasoning tasks regarding the properties of the system. The design relies on simple data storage to maintain the association between the role and its constraints, facilitating easy integration into broader logical frameworks.

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

