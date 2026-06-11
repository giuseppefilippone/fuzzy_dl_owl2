fuzzy_dl_owl2.fuzzydl.domain_axiom
==================================

.. py:module:: fuzzy_dl_owl2.fuzzydl.domain_axiom



.. ── LLM-GENERATED DESCRIPTION START ──

Encapsulates a logical constraint defining the domain of a specific role within an ontology by associating it with a concept.


Description
-----------


Designed to enforce type consistency within a knowledge graph or fuzzy description logic system, the software links a specific role identifier to a concept definition. This association asserts that any individual acting as the subject of the specified relationship must be an instance of the provided concept, thereby restricting the range of valid subjects. The implementation functions as a data container that stores these references directly without performing immediate validation, allowing downstream reasoning processes to utilize the constraint for logical inference and consistency checks.

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

