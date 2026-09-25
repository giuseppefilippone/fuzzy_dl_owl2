fuzzy_dl_owl2.fuzzydl.range_axiom
=================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.range_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Defines a role range axiom for a fuzzy description-logic knowledge base, pairing a role name with the concept that restricts which individuals may appear as its values.


Description
-----------


In description logics, a range axiom constrains the fillers of a role: whenever two individuals are connected through the given role, the target individual must be an instance of the specified concept. **RangeAxiom** captures exactly this constraint as a pair of values — the role's identifier, given as a plain string, and the Concept object describing the admissible set of individuals. The design is deliberately minimal: the constructor simply stores both inputs as instance attributes, performing no validation or reasoning of its own, because enforcement of the restriction is delegated to the reasoning engine that later consumes the knowledge base. As a result, the object serves as a lightweight, declarative building block that knowledge-base authors instantiate to state a typing constraint, leaving interpretation to the broader fuzzy DL machinery during consistency checking, classification, or query answering. Keeping the role as a bare string rather than a dedicated role object reinforces its nature as a simple data carrier within the larger fuzzydl package, where concepts carry the expressive structure and axioms merely record the relationships between them.

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

