# Summary

A specialized data structure representing a Sugeno fuzzy integral concept that aggregates multiple fuzzy concepts using a corresponding set of weights.

## Description

Acting as a component within the FuzzyOWL2 framework, this implementation extends the base definition to model the aggregation of fuzzy logic terms based on specific importance values. It requires initialization with parallel lists of floating-point coefficients and string identifiers, which are stored internally to define the relative density and the specific linguistic terms involved in the calculation. By explicitly marking the entity with the SUGENO type, the design ensures proper classification and integration with the broader ontology system. Furthermore, the logic formats the stored data into a parenthesized string expression, enabling straightforward serialization and human-readable representation of the fuzzy measure configuration.
