# Summary

A reasoning engine that executes fuzzy description logic queries by translating logical constraints into mixed-integer linear programming optimization problems to determine membership degrees and consistency.

## Description

The architecture relies on a hierarchy of abstract base classes that define standard interfaces for executing, preprocessing, and timing operations against a knowledge base, ensuring consistent behavior across diverse reasoning tasks. Concrete implementations extend these foundations to perform specific logical evaluations, such as determining the subsumption degree between concepts, verifying the satisfiability of the entire ontology, or retrieving all individuals that match a conceptual definition. To handle the inherent complexity of fuzzy logic, the system translates semantic constraints into mathematical models, utilizing mixed-integer linear programming to compute precise upper and lower bounds for membership degrees and relationships. Specialized sub-packages further organize this functionality by grouping optimization strategies for minimum and maximum value calculations, as well as defuzzification methods that convert fuzzy results into crisp numerical outputs. Throughout the process, the software manages potential inconsistencies by cloning knowledge bases to preserve state and implementing robust error handling to report logical contradictions gracefully.

## Modules

- [`fuzzy_dl_owl2.fuzzydl.query.all_instances_query`] — Retrieves all individuals from a knowledge base that satisfy a specified concept and calculates their corresponding fuzzy membership degrees.
- [`fuzzy_dl_owl2.fuzzydl.query.bnp_query`] — Encapsulates the calculation of the best non-fuzzy performance for a triangular fuzzy number within a query framework.
- [`fuzzy_dl_owl2.fuzzydl.query.classification_query`] — A specialized query implementation that triggers the classification of a knowledge base and handles potential inconsistencies by returning specific solution states.
- [`fuzzy_dl_owl2.fuzzydl.query.instance_query`] — An abstract base class that defines a framework for querying the membership degree of a specific individual within a given concept.
- [`fuzzy_dl_owl2.fuzzydl.query.kb_satisfiable_query`] — A query implementation that determines the logical consistency and satisfiability of a fuzzy description logic knowledge base.
- [`fuzzy_dl_owl2.fuzzydl.query.query`] — An abstract base class defines the standard interface for executing, preprocessing, and timing queries against a fuzzy knowledge base.
- [`fuzzy_dl_owl2.fuzzydl.query.related_query`] — An abstract base class defines the structure for queries evaluating role assertions and membership degrees between individuals in a fuzzy description logic system.
- [`fuzzy_dl_owl2.fuzzydl.query.satisfiable_query`] — Establishes a foundational interface for min/max satisfiability queries that evaluate the degree to which a specific fuzzy concept is satisfied, optionally within the context of a particular individual.
- [`fuzzy_dl_owl2.fuzzydl.query.subsumption_query`] — An abstract base class that defines the structure for evaluating the degree to which one concept is subsumed by another within a fuzzy logic framework.

## Sub-packages

- [`fuzzy_dl_owl2.fuzzydl.query.defuzzify`] — A suite of defuzzification strategies converts fuzzy membership degrees into crisp numerical values by leveraging Mixed-Integer Linear Programming to optimize objective expressions within a constrained knowledge base.
- [`fuzzy_dl_owl2.fuzzydl.query.max`] — A suite of fuzzy logic optimization queries that compute maximum truth values for concepts, individuals, and relationships using mixed-integer linear programming.
- [`fuzzy_dl_owl2.fuzzydl.query.min`] — A set of fuzzy description logic query mechanisms that calculates the greatest lower bounds of various logical relationships by transforming them into mixed-integer linear programming optimization problems.
