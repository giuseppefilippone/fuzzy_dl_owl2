fuzzy_dl_owl2.fuzzyowl2.parser
==============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_parser.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.parser**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_parser.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.parser
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.parser**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.parser





.. ── LLM-GENERATED DESCRIPTION START ──

A parsing layer that translates FuzzyOWL2 XML annotations into the Python object model of a fuzzy description-logic ontology, covering fuzzy concepts, membership-function datatypes, modifiers, modified roles, axiom degrees, and ontology-level fuzzy logic declarations.


Description
-----------


Parsing is implemented as a stateless translation layer built entirely from static methods: each incoming XML string is inspected at its root element, and dispatch on the fuzzy type attribute selects the matching in-memory object to construct. Concept annotations become modified, weighted, nominal, or aggregation-style definitions — including weighted min/max/sum combinations and OWA, Choquet, Sugeno, quasi-Sugeno, and quantified-OWA constructs assembled from explicit weight and concept-name lists — while datatype annotations yield membership functions such as triangular, trapezoidal, left-shoulder, right-shoulder, linear, and crisp shapes, optionally wrapped in modifiers. Modifier annotations produce linear or triangular modifier objects, role annotations are constrained to modified properties, axiom annotations reduce to a plain float degree, and ontology annotations simply return the declared fuzzy logic as a string, so the return type is intentionally a broad union that mirrors the full FuzzyOWL2 vocabulary; anything outside that vocabulary raises a *ValueError* to signal unsupported input.

Robustness and security are treated as first-class concerns. XML processing goes through *defusedxml* rather than the standard library's parser, a deliberate hardening choice when ingesting potentially untrusted ontology files, and attribute lookups are performed case-insensitively to tolerate variations in how annotations were serialised. A convenience entry point loads runtime settings from a CONFIG.ini file before delegating to the core parsing routine, and it wraps the whole operation in error handling that reports the exception and full traceback instead of propagating it, so a missing configuration file or malformed annotation degrades gracefully rather than crashing the caller. Architecturally, all type dispatch is centralised in one place, which makes the supported vocabulary easy to audit and extend, while the actual representation of each fuzzy construct is delegated to the dedicated owl_types classes, keeping the interpretation logic cleanly separated from the object model it populates.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.parser.owl2_xml_parser``] — A parser that converts FuzzyOWL2 XML annotations into the Python object model of a fuzzy description-logic ontology, handling fuzzy concepts, membership-function datatypes, modifiers, modified roles, axiom degrees, and ontology-level fuzzy logic declarations.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/parser/owl2_xml_parser/index
