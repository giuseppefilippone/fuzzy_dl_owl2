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

A polymorphic hierarchy of *degrees of truth* for a fuzzy description-logic reasoner, allowing graded concept-satisfaction values to be represented and manipulated uniformly whether they materialise as resolved numbers, solver variables, or symbolic linear expressions.


Description
-----------


In fuzzy description logics, concept satisfaction is graded rather than binary, and the value expressing that grade can take several different underlying forms: a plain floating-point number, a mixed-integer linear programming variable, or a full symbolic linear expression. The abstract ``Degree`` base class captures this by declaring a single polymorphic contract — folding the degree into larger expressions through addition and subtraction, scaling it by constants, building inequalities in which the degree serves as the right-hand side against a supplied expression and comparison operator, probing special numeric states such as zero or one, and providing equality and printable representations — so that reasoning code can manipulate every kind of degree uniformly, with type-specific behaviour delegated to concrete subclasses that know how to interpret their own internal representation. Three concrete realisations supply that behaviour: a float-backed degree holds a fully resolved satisfaction value, a variable-backed degree wraps an unknown MILP variable whose value the optimisation solver must later determine, and an expression-backed degree wraps a symbolic linear expression that remains unresolved until the solver assigns values to its variables.

The central architectural role is bridging the fuzzy reasoning layer and the optimisation layer: because every degree knows how to inject itself into a linear expression and how to form an inequation, graded concept and role satisfiability can be translated directly into the constraints of a mixed-integer linear programming problem. The symbolic variants consistently report themselves as non-numeric — never zero, never one — which prevents the surrounding system from attempting constant simplification on values that are not yet known and forces structural handling instead. Identity semantics follow the underlying representation: numeric degrees compare by value with strict floating-point equality, while the variable and expression wrappers delegate equality and hashing to the wrapped object, making them transparent handles that behave correctly in sets and dictionaries. All algebraic operations are purely functional, returning fresh expression or inequation objects rather than mutating their inputs, and cloning produces independent wrappers around the same underlying value, keeping the original safe from later modification while preserving its meaning.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.degree.degree``] — An abstract base class defining the polymorphic interface for *degrees of truth*—values that quantify how strongly a fuzzy concept is satisfied by an individual in a fuzzy description logic reasoner.
* [``fuzzy_dl_owl2.fuzzydl.degree.degree_expression``] — Provides a non-numeric degree type that wraps a symbolic linear expression, allowing fuzzy truth values to be manipulated algebraically and converted into inequations for an underlying mixed-integer linear programming solver.
* [``fuzzy_dl_owl2.fuzzydl.degree.degree_numeric``] — A concrete, float-backed implementation of a fuzzy degree that stores a single numeric satisfaction value and integrates it into the linear expressions and inequality constraints used by the fuzzy description-logic reasoner.
* [``fuzzy_dl_owl2.fuzzydl.degree.degree_variable``] — A symbolic degree of satisfaction that wraps a linear-programming variable, allowing unknown fuzzy truth values to be embedded in algebraic expressions and inequality constraints that a solver can later resolve.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/degree/degree/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/degree_expression/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/degree_numeric/index
   /api/fuzzy_dl_owl2/fuzzydl/degree/degree_variable/index