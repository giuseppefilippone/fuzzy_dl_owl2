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

Specialized implementations of fuzzy description logic concepts that apply linear or triangular transformations to adjust the degree of satisfaction of a base concept.


Description
-----------


The architecture centers on a wrapper pattern where a base concept is combined with a modifier object to shift or scale the truth value of a fuzzy logic entity. A generalized base class handles the structural delegation of properties like atomicity and roles to the underlying concept, while specific subclasses implement distinct mathematical transformations such as linear scaling or triangular non-linear adjustments. Operator overloading is utilized throughout the hierarchy to treat these modified entities as first-class citizens within logical expressions, delegating complex operations like negation and conjunction to a central handler. To support dynamic manipulation without side effects, the design includes mechanisms for cloning instances and recursively replacing sub-concepts, ensuring that the integrity of the concept hierarchy is preserved during evaluation.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept``] — A specialized implementation of a fuzzy description logic concept that applies a linear transformation to the degree of satisfaction of a base concept.
* [``fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept``] — A fuzzy description logic construct that applies a semantic modifier to an underlying concept to alter its degree of satisfaction.
* [``fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept``] — A specialized class representing a fuzzy logic concept that has been transformed by a triangular modifier to adjust its membership degree.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/linearly_modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/triangularly_modified_concept/index

