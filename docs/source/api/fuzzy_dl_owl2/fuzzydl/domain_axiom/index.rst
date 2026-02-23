fuzzy_dl_owl2.fuzzydl.domain_axiom
==================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.domain_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

A class representing a domain axiom that restricts the subjects of a specific role to a defined concept.


Description
-----------


It serves as a fundamental data structure within a fuzzy description logic system to enforce type consistency by linking a specific role to a concept that defines its valid subjects. By associating a role identifier with a concept object, the implementation ensures that any individual acting as the source of that relationship must be an instance of the designated class. This logical constraint is essential for maintaining ontology integrity, allowing reasoning processes to validate or infer the types of entities involved in specific relationships. The design focuses on simple storage of these two components, relying on external systems to apply the necessary validation or reasoning rules based on the defined domain.

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

