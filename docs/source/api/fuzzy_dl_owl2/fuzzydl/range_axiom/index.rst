fuzzy_dl_owl2.fuzzydl.range_axiom
=================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.range_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a logical constraint that restricts the permissible types of individuals associated with a specific role within a fuzzy description logic system.


Description
-----------


Encapsulating a fundamental rule in description logic, the ``RangeAxiom`` class dictates the domain of values a specific property or role may assume. By associating a named role with a specific concept, the implementation ensures that any individual linked via that role must belong to the defined concept class. Acting as a building block for knowledge representation, the logic enables reasoning engines to validate relationships and maintain consistency within an ontology. The design relies on simple attribute storage to capture the role identifier and the corresponding concept object, thereby facilitating downstream logical processing and constraint verification.

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

