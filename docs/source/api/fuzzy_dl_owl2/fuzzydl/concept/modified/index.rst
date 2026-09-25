fuzzy_dl_owl2.fuzzydl.concept.modified
======================================

.. only:: html

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_modified.png
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.modified
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.modified**

.. only:: latex

    .. raw:: latex

       \begin{landscape}

       \vspace*{\fill}

    .. figure:: /_uml/module_fuzzy_dl_owl2_fuzzydl_concept_modified.pdf
       :alt: UML Class Diagram for fuzzy_dl_owl2.fuzzydl.concept.modified
       :align: center
       :width: 100%
       :class: uml-diagram

       UML Class Diagram for **fuzzy_dl_owl2.fuzzydl.concept.modified**

    .. raw:: latex

       \vspace*{\fill}

       \end{landscape}

.. py:module:: fuzzy_dl_owl2.fuzzydl.concept.modified



.. ── LLM-GENERATED DESCRIPTION START ──

A family of fuzzy description-logic concepts that pair an arbitrary concept with a linguistic modifier such as "very" or "slightly", reshaping the degree to which individuals satisfy the wrapped concept.


Description
-----------


In fuzzy ontologies, concepts carry degrees of satisfaction in the interval [0, 1] rather than crisp truth values, and applying a linguistic hedge is the mechanism for expressing notions like "very tall" or "more or less cheap". The architecture follows a *decorator* pattern: an abstract base class combines the core concept hierarchy with a concept-holding interface, pairing any concept with a Modifier and tagging the result as a distinct MODIFIED concept type, while two concrete subclasses supply the actual transformation semantics — one scales and shifts the truth value linearly, and the other reshapes it non-linearly through a triangular function. The wrapper is kept deliberately thin, so questions about the wrapped concept's structure — its atomic components, the roles it mentions, and whether it is concrete — are delegated unchanged to the inner concept, treating modification purely as a semantic transformation of membership degrees rather than a syntactic restructuring. Textual rendering places the modifier and the wrapped concept side by side within parentheses, yielding readable expressions that mirror how hedged concepts are written in fuzzy description logics.

Composition relies on Python's operator protocol, with unary minus, the ampersand, and the pipe building negations, conjunctions, and disjunctions by delegating to a shared operator-concept factory, which lets modified expressions blend seamlessly into larger logical formulas alongside every other concept type. The whole design has an immutable flavour: cloning, sub-concept replacement, and every logical operation return fresh objects rather than mutating their operands, so modified concepts can be shared safely throughout a knowledge base without aliasing side effects. Substitution of a sub-concept is deliberately left abstract at the base level so that each concrete kind must supply its own replacement logic and a missing override fails fast, and both implementations intentionally preserve polarity — a deliberate departure from the original Java version, whose substitution apparently negated its result through a copy-paste of the complement operation. Hashing is derived from the structural identity of the components — the wrapped concept, the modifier, the name, and the type — so distinct instances representing the same logical construct compare equal and behave correctly as dictionary keys or set members.


Modules
-------


* [``fuzzy_dl_owl2.fuzzydl.concept.modified.linearly_modified_concept``] — Models a fuzzy description-logic concept whose degree of satisfaction is linearly transformed by a modifier, producing expressions of the form (modifier C).
* [``fuzzy_dl_owl2.fuzzydl.concept.modified.modified_concept``] — An abstract base class for fuzzy description-logic concepts in which a linguistic modifier such as "very" or "slightly" reshapes how strongly individuals satisfy an underlying concept.
* [``fuzzy_dl_owl2.fuzzydl.concept.modified.triangularly_modified_concept``] — A fuzzy description-logic concept that wraps a base concept with a triangular modifier, non-linearly reshaping its degree of membership while remaining fully composable with other concepts through standard logical operators.

.. ── LLM-GENERATED DESCRIPTION END ──

Submodules
----------

.. toctree::
   :maxdepth: 1

   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/linearly_modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/modified_concept/index
   /api/fuzzy_dl_owl2/fuzzydl/concept/modified/triangularly_modified_concept/index

