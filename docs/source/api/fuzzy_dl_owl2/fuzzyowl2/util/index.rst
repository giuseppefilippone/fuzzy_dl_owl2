fuzzy_dl_owl2.fuzzyowl2.util
============================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_util.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.util
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.util**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2_util.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2.util
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2.util**

.. py:module:: fuzzy_dl_owl2.fuzzyowl2.util







.. ── LLM-GENERATED DESCRIPTION START ──

A utilities layer for the FuzzyOWL2 fuzzy-ontology framework that centralizes the language's canonical vocabulary, generates the XML markup required by the fuzzy ontology specification, and reorders fuzzyDL knowledge-base statements to mirror the reference manual's documentation sequence.


Description
-----------


Support for the FuzzyOWL2 framework rests on three complementary capabilities: a canonical vocabulary for the fuzzy ontology language, a factory that renders fuzzy ontology model objects as specification-compliant XML, and a sorter that arranges fuzzyDL knowledge-base statements in the order the reference manual documents them. The vocabulary lives in a pair of enumerations that act as a single source of truth: one discriminates the kinds of fuzzy concepts an ontology can hold — integral-based aggregations such as Sugeno and Choquet, the weighted min/max/sum families, modified concepts, and fuzzy nominals — so downstream processing can apply the correct fuzzy semantics without inspecting a concept's internal structure, while the other binds every token of the language, from XML-like delimiters and axiom keywords to fuzzy logic names such as Łukasiewicz, Gödel, and Zadeh, to a ready-made pyparsing grammar element, letting grammars be assembled from one registry rather than from string literals scattered through parsing code. Equality comparison on those keyword members is deliberately loosened so they match case-insensitively against plain strings, raw pyparsing keywords, or each other, which simplifies token matching during parsing. The XML builder resolves all of its tag names and attribute keys through those same keyword constants, keeping the generated markup aligned with the vocabulary the parser recognizes; it is a stateless set of static factory methods that produces elements for ontology roots, fuzzy logic declarations, datatype and modifier definitions, truth degrees, weight lists, and concept-name collections, merging caller-supplied attributes over sensible defaults and pretty-printing the result for debugging, logging, or embedding into ontology documents.

The statement sorter serves human readability rather than machine semantics: a canonical ordering table of anchored, case-insensitive regular expressions mirrors the page-by-page sequence of fuzzyDL commands in the manual, each statement is classified by the first pattern that matches, and equal-index statements fall back to a deterministic lexicographic order while a large sentinel value pushes anything unrecognised to the very end, with matched clusters emitted separated by configurable blank lines. One ambiguity is knowingly left unresolved — a bare functional declaration is syntactically indistinguishable between feature-level and role-level uses, so inputs mixing both require external preclassification — and optional debug tracing logs every match attempt to make unexpected placements easy to diagnose. The overall design is deliberately declarative and side-effect free: constants feed both grammar assembly and markup generation from a single place, the builders require no instantiation or shared state, and the sorting logic is driven entirely by data tables, making everything uniform, predictable, and easy to test.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.util.constants``] — A pair of enumerations that give the FuzzyOWL2 framework its canonical vocabulary: a string-based taxonomy of fuzzy concept types, and a keyword registry that binds every token of the FuzzyOWL2 language to a ready-made pyparsing grammar element.
* [``fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml``] — A stateless builder utility that constructs the XML elements required by the FuzzyOWL2 fuzzy ontology specification and renders them as human-readable strings.
* [``fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines``] — A utility for reordering fuzzyDL knowledge-base statements so that they follow the page-by-page order in which the commands are documented in the fuzzyDL PDF manual.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/util/constants/index
   /api/fuzzy_dl_owl2/fuzzyowl2/util/fuzzy_xml/index
   /api/fuzzy_dl_owl2/fuzzyowl2/util/sort_dl_lines/index