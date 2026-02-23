# Summary

A class representing a domain axiom that restricts the subjects of a specific role to a defined concept.

## Description

It serves as a fundamental data structure within a fuzzy description logic system to enforce type consistency by linking a specific role to a concept that defines its valid subjects. By associating a role identifier with a concept object, the implementation ensures that any individual acting as the source of that relationship must be an instance of the designated class. This logical constraint is essential for maintaining ontology integrity, allowing reasoning processes to validate or infer the types of entities involved in specific relationships. The design focuses on simple storage of these two components, relying on external systems to apply the necessary validation or reasoning rules based on the defined domain.
