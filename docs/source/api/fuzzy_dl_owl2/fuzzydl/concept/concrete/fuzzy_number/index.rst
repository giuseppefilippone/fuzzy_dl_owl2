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
       :width: 18.2cm
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number



.. ── LLM-GENERATED DESCRIPTION START ──

A concrete implementation of triangular fuzzy numbers that supports fuzzy arithmetic, logical operations, and defuzzification.


Description
-----------


Triangular fuzzy numbers are modeled using three distinct parameters defining the lower bound, peak, and upper bound of a membership function to represent uncertain or imprecise values. Standard arithmetic operations such as addition, subtraction, multiplication, and division are executed by applying interval arithmetic rules to these parameters, ensuring the generation of new instances with correctly calculated bounds. Logical operations like conjunction and disjunction are facilitated through delegation to an operator concept handler, allowing these numbers to integrate seamlessly into broader fuzzy logic expressions. Functionality for defuzzification converts the fuzzy representation into a single crisp value for performance evaluation, while utility methods assist in determining if an instance represents a crisp value or requires cloning for independent manipulation.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number.triangular_fuzzy_number``] — A concrete implementation of a triangular fuzzy number that supports fuzzy arithmetic, logical operations, and defuzzification.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/fuzzy_number/triangular_fuzzy_number/index

