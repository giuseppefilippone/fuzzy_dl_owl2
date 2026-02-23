fuzzy_dl_owl2.fuzzydl.concept.modified
======================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_modified.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.modified
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.modified**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_modified.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.modified
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.modified**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified



.. ── LLM-GENERATED DESCRIPTION START ──

Implements fuzzy description logic concepts that apply linear or triangular modifiers to base concepts to adjust membership degrees.


Description
-----------


A framework enables the semantic alteration of fuzzy description logic concepts by wrapping base entities with specific modifiers that adjust the degree of membership. An abstract wrapper preserves the structural properties of the underlying concept, such as roles and atomicity, while delegating structural queries to the original entity to ensure data integrity. Concrete implementations handle distinct mathematical transformations, such as linear and triangular adjustments, by extending the core wrapper logic. Logical operations including negation, conjunction, and disjunction are facilitated through operator overloading, which delegates the creation of complex expressions to a centralized utility to maintain consistency across the hierarchy. Furthermore, the architecture supports structural manipulation through cloning and sub-concept replacement, ensuring that modifications generate independent instances without mutating existing objects.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept`` — Represents a fuzzy description logic concept whose truth value is adjusted by a linear modifier, enabling the construction of modified concepts within a logical hierarchy.
* ``fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept`` — A conceptual wrapper that applies a semantic modifier to a base concept to adjust the degree of membership within a fuzzy description logic framework.
* ``fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept`` — A conceptual entity that applies a triangular transformation to a base concept's membership degree while supporting logical operations and structural manipulation.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/linearly_modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/triangularly_modified_concept/index

