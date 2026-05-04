# Summary

A structural representation of a sigma-count concept used in fuzzy description logic to evaluate constraints based on the number of role fillers satisfying specific conditions.

## Description

The `SigmaCount` class encapsulates the components necessary to evaluate constraints based on the quantity of role fillers within a fuzzy description logic framework. It holds references to a counting variable, a target individual, a set of reference individuals, a specific role, and a concept that fillers must satisfy. By including a deep cloning utility, the design ensures that instances can be copied independently to preserve state during complex logical operations or optimizations. Additionally, standard hashing and string formatting capabilities are provided to support usage in hash-based collections and to enable clear textual representation for debugging purposes.
