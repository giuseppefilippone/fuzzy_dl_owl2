# Summary

Foundational utilities for managing fuzzy logic vocabulary, generating compliant XML, and organizing ontology statements according to specification standards.

## Description

Centralized enumerations define the core vocabulary of fuzzy logic concepts and map parsing tokens to concrete grammar definitions, serving as a single source of truth for the framework's syntax. A domain-specific builder abstracts low-level XML manipulation to construct elements that strictly adhere to the FuzzyOWL2 specification, handling everything from root ontology nodes to complex weighted structures. To ensure consistency with reference documentation, a sorting mechanism arranges fuzzyDL statements based on specific syntax patterns, grouping and ranking commands to produce a standardized visual structure. Together, these components abstract the complexities of language processing and output generation, allowing the broader system to reliably handle fuzzy ontology operations without hardcoding implementation details.

## Modules

- [`fuzzy_dl_owl2.fuzzyowl2.util.constants`] — Establishes a centralized vocabulary of fuzzy logic concept types and parsing tokens for the FuzzyOWL2 framework.
- [`fuzzy_dl_owl2.fuzzyowl2.util.fuzzy_xml`] — A utility builder for generating XML elements that conform to the FuzzyOWL2 ontology specification.
- [`fuzzy_dl_owl2.fuzzyowl2.util.sort_dl_lines`] — Implements a sorting mechanism for fuzzyDL statements that arranges them according to the specific syntax order presented in the official PDF documentation.
