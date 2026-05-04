fuzzy_dl_owl2.fuzzydl.domain_axiom
==================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.domain_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates a logical constraint that restricts the domain of a specific role to a defined concept within a fuzzy description logic ontology.


Description
-----------


The software implements a data structure designed to enforce type consistency by defining the domain of a specific role within an ontology. It asserts that any individual acting as the subject of the specified role must be an instance of the associated concept, thereby restricting the range of valid subjects for that relationship. By storing a string identifier for the role alongside a reference to a concept definition, the logic allows the system to validate that relationships adhere to the defined semantic constraints. The implementation relies on direct assignment of these parameters without performing runtime validation, serving as a foundational component for constructing and managing logical rules in a fuzzy description logic framework.

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

