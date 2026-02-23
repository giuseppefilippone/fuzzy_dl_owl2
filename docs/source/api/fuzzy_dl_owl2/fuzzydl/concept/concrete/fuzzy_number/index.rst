fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number
===================================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_concrete_fuzzy_number.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_concrete_fuzzy_number.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number



.. ── LLM-GENERATED DESCRIPTION START ──

Models uncertain numerical values using triangular membership functions to support arithmetic, logical operations, and defuzzification within a fuzzy logic framework.


Description
-----------


Uncertainty is represented through a triangular membership function defined by lower, peak, and upper bounds, ensuring strict validation during initialization to maintain data integrity. Arithmetic manipulations rely on interval arithmetic principles to generate new instances without modifying the originals, while fuzzy logical tasks such as conjunction and disjunction are handled by delegating to an external operator system. To bridge the gap between fuzzy and crisp values, utilities for calculating the Best Non-Fuzzy Performance are included, alongside class-level mechanisms for defining a global universe of discourse that governs range management.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number`` — A Python class that models triangular fuzzy numbers, providing arithmetic and logical operations alongside utilities for defuzzification and range management.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/fuzzy_number/triangular_fuzzy_number/index

