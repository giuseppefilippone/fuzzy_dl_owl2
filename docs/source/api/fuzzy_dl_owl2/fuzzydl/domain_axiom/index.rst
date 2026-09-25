fuzzy_dl_owl2.fuzzydl.domain_axiom
==================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.domain_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

A minimal value object expressing a fuzzy description-logic domain axiom, binding a role name to a Concept that constrains which individuals may act as subjects of that role.


Description
-----------


DomainAxiom models the standard description-logic construct dom(R) ⊑ C: whenever the role is asserted between two individuals, the axiom enforces type consistency by requiring the subject to belong to the associated concept. Within the fuzzydl_owl2 toolkit, such axioms are gathered as part of an ontology's definition and later consumed by a fuzzy DL reasoner or translated into an OWL 2 representation. The design is deliberately minimal — the constructor performs no validation or transformation, simply storing the role identifier and the Concept reference as instance attributes, so the object remains a pure declarative statement rather than an active component. That simplicity shifts responsibility for correctness onto the caller, while keeping each axiom a small, self-contained unit of ontological knowledge that other parts of the system can enumerate, serialize, or reason over.

.. ── LLM-GENERATED DESCRIPTION END ──

Classes
-------

.. autoapisummary::

   fuzzy_dl_owl2.fuzzydl.domain_axiom.DomainAxiom


Module Contents
---------------

.. only:: html

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_domain_axiom_DomainAxiom.png
       :alt: UML Class Diagram for DomainAxiom
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **DomainAxiom**

.. only:: latex

    .. figure:: /_uml/class_fuzzy_dl_owl2_fuzzydl_domain_axiom_DomainAxiom.pdf
       :alt: UML Class Diagram for DomainAxiom
       :align: center
       :width: 9.0cm
       :class: uml-diagram

       UML Class Diagram for **DomainAxiom**

.. py:class:: DomainAxiom(role: str, concept: fuzzy_dl_owl2.fuzzydl.concept.concept.Concept)

   This class encapsulates a logical constraint that defines the domain of a specific role within an ontology or knowledge graph. It asserts that any individual acting as the subject of the specified role must be an instance of the provided concept. By associating a role identifier with a concept definition, it serves to enforce type consistency and restrict the range of valid subjects for a given relationship.

   :param role: The name of the role for which the domain is defined.
   :type role: str
   :param concept: The concept defining the domain of the role.
   :type concept: Concept


   .. py:attribute:: concept
      :type:  fuzzy_dl_owl2.fuzzydl.concept.concept.Concept


   .. py:attribute:: role
      :type:  str

