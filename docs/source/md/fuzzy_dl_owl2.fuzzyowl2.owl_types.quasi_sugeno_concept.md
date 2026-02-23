# Summary

Defines a class representing a quasi-Sugeno integral fuzzy logic operator that aggregates multiple concepts using specific weights within the FuzzyOWL2 ontology framework.

## Description

The implementation extends the base concept definition to model a weighted aggregation of fuzzy concepts based on the quasi-Sugeno integral logic. Upon initialization, the object accepts a list of numerical coefficients and a corresponding list of concept identifiers, storing them as internal state to define the aggregation parameters. Accessor methods allow retrieval of these weights and concepts, enabling other components of the system to utilize the specific criteria and their associated importance values during logical processing. A string representation method formats the data into a parenthetical syntax, which facilitates serialization or display by combining the operator identifier with the space-separated weights and concept lists.
