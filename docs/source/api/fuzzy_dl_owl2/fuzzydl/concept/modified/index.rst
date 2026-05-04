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

A collection of fuzzy description logic components that apply mathematical modifiers, such as linear scaling or triangular transformations, to adjust the satisfaction degree of base concepts.


Description
-----------


The architecture relies on a wrapper pattern where a generic base entity encapsulates a specific concept and applies a modifier to alter its semantic interpretation within a fuzzy logic context. Specific implementations handle distinct mathematical transformations, such as linear scaling or shifting of truth values and non-linear triangular adjustments, while inheriting common behaviors for structural manipulation and logical composition. Logical operations like negation, conjunction, and disjunction are supported through operator overloading, which delegates the actual computation to a central operator handler to ensure consistency across the system. To maintain immutability during inference, the design includes mechanisms for cloning entire structures and recursively replacing sub-concepts without altering the original instances, with hashing based on string representations to facilitate use within collections.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept``] — A class representing a fuzzy description logic concept whose degree of satisfaction is adjusted by a linear modifier.
* [``fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept``] — A specialized conceptual entity that wraps a base concept with a modifier to adjust the degree of truth or satisfaction within a fuzzy description logic framework.
* [``fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept``] — A specialized fuzzy logic concept that applies a triangular modifier to a base concept to non-linearly transform its degree of satisfaction.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/linearly_modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/triangularly_modified_concept/index

