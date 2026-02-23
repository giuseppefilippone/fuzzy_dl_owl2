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

Implements a suite of concrete fuzzy logic concepts that model crisp and graded membership functions through various geometric shapes and linguistic modifiers, while also providing support for fuzzy number arithmetic.


Description
-----------


An abstract base class enforces numerical domain validation and requires subclasses to define specific membership calculation methods, allowing for a diverse range of fuzzy set geometries such as triangular, trapezoidal, and left or right shoulder shapes. Beyond standard graded membership, the software includes a crisp implementation for binary evaluation and a wrapper mechanism that applies linguistic modifiers to transform the membership degrees of existing concepts. Logical operations like negation, conjunction, and disjunction are consistently handled by delegating to external operator utilities, ensuring that complex expressions can be constructed while maintaining the mathematical integrity of the underlying intervals. Furthermore, a dedicated sub-package extends these principles to fuzzy numbers, enabling arithmetic manipulations and defuzzification of uncertain values using triangular membership functions within a defined universe of discourse.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.crisp_concrete_concept`` — Implements a crisp concrete concept that provides binary membership evaluation based on specific intervals within a fuzzy logic framework.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_concrete_concept`` — An abstract base class defines the structure and behavior for fuzzy concepts operating over specific numerical intervals.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.left_concrete_concept`` — Implements a left shoulder fuzzy set concept where membership degrees are maximized at lower values and decrease linearly towards zero.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.linear_concrete_concept`` — A fuzzy concrete concept defined by a piecewise linear membership function operating on a normalized domain between zero and one.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.modified_concrete_concept`` — A fuzzy concrete concept that applies a linguistic modifier to an underlying base concept to transform its membership degrees.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.right_concrete_concept`` — Implements a right-shoulder fuzzy membership function where truth values increase linearly from zero to one over a specified interval.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.trapezoidal_concrete_concept`` — Implements a trapezoidal concrete concept that models fuzzy membership degrees using a four-point geometric shape within a defined domain.
* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.triangular_concrete_concept`` — Implements a fuzzy logic concept characterized by a triangular membership function to evaluate the degree of membership for numeric values within a specific domain.


Sub-packages
------------


* ``fuzzy_dl_owl2.fuzzydl.concept.concrete.fuzzy_number`` — Models uncertain numerical values using triangular membership functions to support arithmetic, logical operations, and defuzzification within a fuzzy logic framework.

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

