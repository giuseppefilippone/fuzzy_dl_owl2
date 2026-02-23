fuzzy_dl_owl2.fuzzydl.modifier
==============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_modifier.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.modifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.modifier**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_modifier.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.modifier
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.modifier**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.modifier



.. ── LLM-GENERATED DESCRIPTION START ──

A framework for transforming fuzzy logic membership degrees through abstract interfaces and concrete mathematical implementations such as linear and triangular functions.


Description
-----------


An abstract base class establishes a foundational blueprint for linguistic hedges and operators, enforcing a consistent contract for altering concept structures and recalculating membership degrees within the fuzzy description logic system. Concrete implementations utilize this interface to apply specific mathematical transformations, such as piecewise linear functions defined by configurable coefficients or triangular shapes characterized by lower, peak, and upper bounds. These transformations wrap base concepts into specialized objects that clamp input values between zero and one, ensuring outputs remain within valid probability bounds while supporting complex reasoning through logical operations like conjunction and disjunction. The architecture facilitates the extension of the knowledge base with custom rules by managing string identifiers and object cloning, thereby enabling the system to handle linguistic nuances by mapping real-valued inputs to normalized membership intervals.


Modules
-------


* ``fuzzy_dl_owl2.fuzzydl.modifier.linear_modifier`` — A class that implements a piecewise linear transformation for fuzzy logic membership degrees based on a configurable coefficient.
* ``fuzzy_dl_owl2.fuzzydl.modifier.modifier`` — An abstract base class defines the interface for fuzzy logic modifiers that transform concepts and calculate membership degrees.
* ``fuzzy_dl_owl2.fuzzydl.modifier.triangular_modifier`` — Implements a triangular fuzzy logic modifier that applies a piecewise linear membership function to concepts based on defined boundary parameters.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/modifier/linear_modifier/index
   /api/fuzzy_dl_owl2/fuzzydl/modifier/modifier/index
   /api/fuzzy_dl_owl2/fuzzydl/modifier/triangular_modifier/index

