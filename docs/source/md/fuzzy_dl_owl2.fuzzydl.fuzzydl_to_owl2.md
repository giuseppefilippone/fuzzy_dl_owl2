# Summary

Software that translates FuzzyDL knowledge bases into OWL2 ontologies, preserving fuzzy logic semantics through specialized annotations and standard semantic web structures.

## Description

The implementation acts as a bridge between fuzzy description logic and the semantic web by parsing FuzzyDL definitions and reconstructing them within an OWL2 framework. Because standard OWL2 lacks native support for fuzzy logic, the converter preserves these semantics by generating new atomic classes for complex fuzzy constructs and attaching detailed XML annotations that encode truth degrees, modifiers, and aggregation operators like OWA or Choquet integrals. The conversion process systematically iterates through the parsed knowledge base to handle concept definitions, property hierarchies, and individual assertions, translating them into corresponding OWL axioms such as subclass, equivalent classes, and property assertions. Ultimately, the tool produces a fully compliant OWL2 ontology file where fuzzy logic rules are embedded as metadata, enabling the data to be utilized by standard semantic web tools while retaining the original nuance of the fuzzy definitions.
