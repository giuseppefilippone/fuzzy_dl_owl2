fuzzy_dl_owl2.fuzzyowl2
=======================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2**

.. only:: latex

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzyowl2.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzyowl2
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzyowl2**

.. py:module:: fuzzy_dl_owl2.fuzzyowl2







.. ── LLM-GENERATED DESCRIPTION START ──

A translation framework that converts fuzzy-logic-annotated OWL 2 ontologies into the S-expression knowledge-base format consumed by the FuzzyDL fuzzy description-logic reasoner.


Description
-----------


Fuzzy OWL 2 ontologies extend classical OWL 2 with degrees of truth: datatypes shaped by membership functions, linguistic hedges such as *very*, axioms annotated with a numeric truth degree, and weighted aggregation operators that combine several concepts into one. Converting such an ontology into a runnable fuzzy description-logic knowledge base requires recognizing those annotations, reconstructing the fuzzy constructs they encode, and re-serializing everything as the definition and assertion commands of the FuzzyDL reasoner, and the translation is organized as a layered pipeline in which parsing, representation, orchestration, and serialization are kept deliberately separate.

The representation layer is a family of typed data holders arranged in four parallel class hierarchies — concept definitions, fuzzy datatypes, modifiers, and properties — each anchored by a non-instantiable abstract base, with every concrete subclass tagging itself with a type discriminator so that parsers, serialisers, and reasoners can handle all constructs polymorphically through a shared contract. The hierarchy spans the classic membership-function shapes (triangular, trapezoidal, shoulder, linear, crisp), hedged variants that pair any element with a modifier, and a rich aggregation family reaching from weighted minima, maxima, and sums through ordered weighted averaging to the Choquet, Sugeno, and quasi-Sugeno integrals, which capture interactions between criteria — such as redundancy or synergy — that plain weighted averages cannot express. These objects are intentionally thin: constructors perform no validation, state is exposed through read-only accessors, no evaluation logic lives inside them, and every class renders itself in a uniform parenthesised syntax, so semantic correctness is deferred entirely to the downstream machinery.

Translation itself proceeds through two cooperating layers. A stateless parsing layer — hardened with *defusedxml* for untrusted input, dispatching case-insensitively on each annotation's fuzzy type, and raising a *ValueError* on anything outside the supported vocabulary — turns XML payloads into those typed objects, while a convenience entry point loads runtime settings and reports failures with full tracebacks rather than crashing the caller. Above it, an orchestrator class walks the ontology in stages: fuzzy annotations are first harvested from the header, datatype, class, and property declarations, parsed, and dispatched to writer hooks; then the TBox, RBox, and ABox axioms are processed in two passes so that graded axioms are emitted before crisp ones, with a deduplication set and deferred class declarations preventing redundant output. The base class supplies the pipeline and hook contract while its own low-level writers remain human-readable placeholders; the concrete FuzzyDL serializer overrides every hook to emit real commands, coping with the target language through IRI name mangling, keyword-clash avoidance, lazy one-time declaration of data properties, mapping of XML Schema datatypes onto FuzzyDL's built-in numeric, boolean, and string types (exclusive bounds nudged inward so they remain representable), and explicit error reporting — never silent dropping — for constructs the reasoner cannot express, such as cardinality restrictions, property chains, or fuzzy nominals.

A utilities layer underpins both directions of the exchange. A pair of enumerations acts as the single source of truth for the language's vocabulary, binding every keyword to a ready-made pyparsing grammar element with loosened, case-insensitive equality, so that grammars and markup are assembled from one registry rather than from string literals scattered through the code; a stateless XML builder resolves its tags through those same constants to render model objects back into specification-compliant FuzzyOWL2 markup. A data-driven sorter then reorders the generated statements to mirror the page-by-page command sequence of the FuzzyDL reference manual, classifying each line against anchored regular-expression tables and falling back to a deterministic lexicographic order, which keeps the output human-readable. The unifying philosophy is declarative and side-effect free: constants feed both grammar assembly and markup generation from one place, sorting is driven purely by data tables, and centralized type dispatch makes the supported fuzzy vocabulary easy to audit and extend.


Modules
-------


* [``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2``] — A translator that converts fuzzy-logic-annotated OWL 2 ontologies into a fuzzy description logic representation, extracting fuzzy datatypes, concepts, modifiers, and graded axioms and writing the translated knowledge base to an output file.
* [``fuzzy_dl_owl2.fuzzyowl2.fuzzyowl2_to_fuzzydl``] — A converter that translates fuzzy OWL 2 ontologies into the S-expression syntax required by the FuzzyDL reasoner, covering concepts, roles, individuals, fuzzy membership functions, and aggregation operators.


Sub-packages
------------


* [``fuzzy_dl_owl2.fuzzyowl2.owl_types``] — A type vocabulary for the FuzzyOWL2 fuzzy ontology framework, providing fuzzy concept definitions, membership-function datatypes, linguistic modifiers, and graded properties that let OWL 2 ontologies express degrees of truth instead of all-or-nothing membership.
* [``fuzzy_dl_owl2.fuzzyowl2.parser``] — A parsing layer that translates FuzzyOWL2 XML annotations into the Python object model of a fuzzy description-logic ontology, covering fuzzy concepts, membership-function datatypes, modifiers, modified roles, axiom degrees, and ontology-level fuzzy logic declarations.
* [``fuzzy_dl_owl2.fuzzyowl2.util``] — A utilities layer for the FuzzyOWL2 fuzzy-ontology framework that centralizes the language's canonical vocabulary, generates the XML markup required by the fuzzy ontology specification, and reorders fuzzyDL knowledge-base statements to mirror the reference manual's documentation sequence.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzyowl2/fuzzyowl2/index
   /api/fuzzy_dl_owl2/fuzzyowl2/fuzzyowl2_to_fuzzydl/index
   /api/fuzzy_dl_owl2/fuzzyowl2/owl_types/index
   /api/fuzzy_dl_owl2/fuzzyowl2/parser/index
   /api/fuzzy_dl_owl2/fuzzyowl2/util/index