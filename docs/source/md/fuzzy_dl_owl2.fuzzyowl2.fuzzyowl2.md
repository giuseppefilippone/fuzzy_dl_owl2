# Summary

A translator that converts OWL2 ontologies annotated with fuzzy logic semantics into a Fuzzy Description Logic representation suitable for reasoning engines.

## Description

The software acts as a bridge between standard OWL2 structures and fuzzy logic reasoning systems by reading an ontology file and extracting specific annotations that define fuzzy concepts, properties, and datatypes. It processes the ontology in distinct stages, first resolving datatype and concept annotations to establish the fuzzy vocabulary—such as triangular membership functions or linguistic modifiers—before handling the axioms that define the logical structure. A critical aspect of the design involves managing axiom degrees, where the system distinguishes between crisp axioms and those carrying specific truth values to accurately represent uncertainty in the output. By relying on an underlying XML parser to interpret complex annotation strings, the tool iterates through various axiom types, serializes them into a text-based format, and ensures no redundancy by tracking processed items before writing the final sorted definitions to a file.
