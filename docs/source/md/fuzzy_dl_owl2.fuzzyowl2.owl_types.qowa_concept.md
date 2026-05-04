# Summary

Encapsulates the definition of a Quantified Ordered Weighted Averaging (OWA) concept used in fuzzy logic ontology modeling.

## Description

It extends the base definition for concepts to specifically handle scenarios where a set of fuzzy concepts is aggregated according to a linguistic quantifier. By accepting a string representing the quantifier and a collection of underlying concept identifiers, the implementation allows for the representation of complex, weighted aggregations required by the FuzzyOWL2 specification. The internal state is managed through private attributes that store the aggregation logic and the target concepts, which can be retrieved via accessor methods for use in broader reasoning tasks. A string representation is provided to output the structure in a parenthetical syntax, facilitating easy visualization or serialization of the logical expression.
