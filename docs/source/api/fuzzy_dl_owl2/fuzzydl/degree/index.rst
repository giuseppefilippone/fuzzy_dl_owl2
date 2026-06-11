fuzzy_dl_owl2.fuzzydl.degree
============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_degree.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.degree
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.degree**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_degree.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.degree
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.degree**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.degree



.. ── LLM-GENERATED DESCRIPTION START ──

A polymorphic framework for representing fuzzy logic degrees as concrete numeric values or symbolic algebraic entities to support arithmetic operations and constraint generation within mixed-integer linear programming models.


Description
-----------


The architecture establishes a unified interface for quantifying concept satisfaction, allowing the system to treat fixed numbers, dynamic expressions, and unknown variables interchangeably through a shared abstract contract. By enforcing standard arithmetic manipulations such as addition, subtraction, and scalar multiplication, the design enables these diverse degree types to seamlessly integrate into mathematical modeling workflows without exposing their underlying implementation details. Concrete implementations distinguish between numeric constants and symbolic entities, ensuring that type checking and evaluation logic correctly handle static values versus dynamic components that require solving. This abstraction facilitates the automatic generation of linear programming constraints and inequalities, bridging the gap between high-level fuzzy logic reasoning and low-level solver mechanics.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.degree.degree``] — An abstract base class defines the interface for representing degrees used to quantify concept satisfaction within a fuzzy logic system.
* [``fuzzy_dl_owl2.fuzzydl.degree.degree_expression``] — A symbolic wrapper for algebraic expressions that functions as a non-numeric degree within a fuzzy logic system, enabling dynamic satisfaction measures through mathematical manipulation.
* [``fuzzy_dl_owl2.fuzzydl.degree.degree_numeric``] — A concrete implementation of a fuzzy logic degree that encapsulates a specific numeric value to facilitate arithmetic operations and constraint generation within a mathematical model.
* [``fuzzy_dl_owl2.fuzzydl.degree.degree_variable``] — A symbolic wrapper for algebraic variables allows degrees of satisfaction in a fuzzy logic system to be treated as unknowns that must be solved for rather than fixed constants.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/degree/degree/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/degree_expression/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/degree_numeric/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/degree_variable/index

