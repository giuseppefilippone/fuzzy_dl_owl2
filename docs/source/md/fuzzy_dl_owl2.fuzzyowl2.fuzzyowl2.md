# Summary

A translator that converts OWL2 ontologies annotated with fuzzy logic into a Fuzzy Description Logic representation for use in reasoning systems.

## Description

The software processes OWL2 ontology files to extract fuzzy logic semantics defined through annotations, transforming them into a format compatible with Fuzzy Description Logic reasoners. It parses complex fuzzy constructs, such as triangular functions, linear modifiers, and aggregation operators like OWA or Sugeno integrals, from datatype, concept, and property declarations. The translation pipeline handles both standard crisp axioms and those annotated with specific truth degrees, ensuring that the structural hierarchy and logical constraints of the original ontology are preserved in the target representation. By maintaining internal registries of defined concepts, properties, and datatypes, the system prevents duplicate definitions and manages dependencies between fuzzy elements. Finally, the extracted definitions and axioms are serialized to an output file, sorted to maintain a consistent order suitable for downstream processing.
