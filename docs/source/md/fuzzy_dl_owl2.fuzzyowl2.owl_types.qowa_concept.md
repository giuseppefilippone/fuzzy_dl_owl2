# Summary

Defines a specialized data structure for modeling **Quantified Ordered Weighted Averaging (OWA)** concepts within the FuzzyOWL2 ontology language.

## Description

The implementation extends the base definition for concepts to encapsulate the logic required for quantified aggregations, specifically handling how a set of fuzzy concepts is weighted and combined based on a linguistic quantifier. By storing a quantifier string alongside a collection of concept identifiers, the structure allows for the representation of complex, weighted decision-making processes inherent in fuzzy logic systems. Accessor methods expose the internal state, enabling other components of the system to retrieve the specific quantification rules and the underlying concepts involved in the aggregation. Furthermore, the logic includes a string representation that formats the data into a specific parenthetical syntax, facilitating easy serialization and human-readable output for debugging or data exchange.
