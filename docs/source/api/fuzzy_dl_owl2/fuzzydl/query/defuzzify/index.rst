fuzzy_dl_owl2.fuzzydl.query.defuzzify
=====================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_defuzzify.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.defuzzify
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.defuzzify**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_query_defuzzify.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.query.defuzzify
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.query.defuzzify**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.query.defuzzify







.. ── LLM-GENERATED DESCRIPTION START ──

Defuzzification queries for a fuzzy description-logic reasoner that convert an individual's graded membership in a concept into a single crisp feature value, offering the Smallest of Maxima, Mean of Maxima, and Largest of Maxima strategies on top of a shared mixed-integer linear programming pipeline.


Description
-----------


Defuzzification is the reasoning step that bridges fuzzy and concrete knowledge: given a concept, an individual, and a named feature, a query of this kind determines the numeric value that best represents how strongly the individual belongs to the concept. Because a fuzzy membership function can plateau at its maximum degree over a range of domain values, three interchangeable strategies resolve the ambiguity — **SOM** selects the smallest value of the plateau, **LOM** the largest, and **MoM** the midpoint of its two extremes.

The design follows a classic template-method pattern. An abstract base query owns the entire workflow: it clones the knowledge base so that assertions and intermediate results never leak into the caller's ontology, runs a maximum-satisfiability query to establish the best degree to which the individual belongs to the target concept, asserts that degree back into the clone, traverses the individual's role relations to locate the feature's underlying MILP variable, and executes the final optimization, normalizing any negative result to its absolute value. Concrete subclasses contribute only the objective expression that encodes their particular strategy — a unit coefficient on the feature variable for SOM, its negation for LOM — which keeps each strategy minimal and makes adding a new one a matter of supplying a single expression. The MoM variant deliberately departs from the inherited skeleton: it leaves the preprocessing hook empty and instead builds a second clone asserted at the maximal degree, optimizes it twice to bracket the lower and upper edges of the membership plateau, and returns the arithmetic mean of the two extremes, writing the result back as a labelled feature value.

Robustness is handled uniformly across all strategies: inconsistent ontologies are caught through dedicated exceptions and surfaced as solutions explicitly flagged as inconsistent, while missing role relations or unbound optimization variables trigger warnings and null answers rather than crashes. Verbose solver logging is suppressed during setup and re-enabled only for the decisive optimization, and every query carries a human-readable representation naming its strategy, feature, and instance so that computed crisp values can be traced intelligibly in logs and debugging output.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.defuzzify_query``] — An abstract query class that converts a fuzzy membership degree into a crisp value for a named feature of an individual, by first computing the individual's maximal degree of membership in a concept and then optimizing a MILP objective built from the feature's associated variable.
* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.lom_defuzzify_query``] — A defuzzification query that applies the Largest of Maxima (LOM) method, converting a fuzzy membership value into a crisp number by selecting the largest value at which the degree of membership is maximized.
* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.mom_defuzzify_query``] — A Mean of Maxima (MoM) defuzzification query that turns a fuzzy feature of an individual into a single crisp number by averaging the smallest and largest feature values at which the individual achieves its maximum degree of membership in a given concept.
* [``fuzzy_dl_owl2.fuzzydl.query.defuzzify.som_defuzzify_query``] — Defines a defuzzification query that converts a fuzzy membership degree into a single crisp number using the Smallest of Maxima (SOM) strategy, which selects the smallest domain value at which an individual's membership in a concept reaches its peak.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/defuzzify_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/lom_defuzzify_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/mom_defuzzify_query/index
   /api/fuzzy_dl_owl2/fuzzydl/query/defuzzify/som_defuzzify_query/index