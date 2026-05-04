fuzzy_dl_owl2.fuzzydl.concept.concrete
======================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_concrete.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.concrete
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.concrete**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_concrete.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.concrete
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.concrete**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.concrete



.. ── LLM-GENERATED DESCRIPTION START ──

Concrete fuzzy logic concepts operating over numerical intervals are modeled through a hierarchy of classes implementing specific membership functions and arithmetic operations.


Description
-----------


An abstract base class establishes the structural foundation by managing interval bounds and enforcing geometric constraints, while delegating specific membership calculations to subclasses that represent distinct mathematical shapes. Implementations include standard fuzzy set geometries such as triangular, trapezoidal, left shoulder, and right shoulder functions, alongside a crisp binary variant and a piecewise linear model operating on a normalized domain. To support complex linguistic expressions, a wrapper mechanism applies modifiers to base concepts, transforming membership degrees to represent terms like "very" or "somewhat." Logical operations such as conjunction, disjunction, and negation are handled consistently across all implementations through operator overloading that delegates to a centralized utility, ensuring seamless integration within a broader fuzzy description logic framework. Additionally, a dedicated sub-package extends this functionality to handle uncertain values via triangular fuzzy numbers, supporting interval arithmetic, logical comparisons, and defuzzification techniques.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept``] — Defines a crisp concrete concept within a fuzzy logic framework using a binary membership function based on specific validity and satisfaction intervals.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept``] — An abstract base class defines fuzzy concepts operating over numerical intervals with configurable lower and upper bounds.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept``] — A Python implementation of a left shoulder fuzzy set that assigns full membership to lower values and linearly decreases to zero over a specified interval.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept``] — A fuzzy concept implementation that models a piecewise linear membership function operating on a normalized domain between zero and one.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept``] — A fuzzy concrete concept wrapper that applies a linguistic modifier to the membership degree of an underlying base concept.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept``] — A specialized class models a fuzzy logic concept characterized by a "right shoulder" membership function, where the degree of truth transitions linearly from zero to one as an input value increases.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept``] — Implements a trapezoidal membership function for fuzzy logic concepts, defining degrees of membership based on specific geometric parameters.
* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept``] — Implements a fuzzy logic concept characterized by a triangular membership function to model linguistic variables within a specific domain.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number``] — Implements a mathematical framework for handling uncertain values through triangular fuzzy numbers, supporting arithmetic operations, logical comparisons, and defuzzification.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/crisp_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/fuzzy_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/fuzzy_number/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/left_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/linear_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/modified_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/right_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/trapezoidal_concrete_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/concrete/triangular_concrete_concept/index

