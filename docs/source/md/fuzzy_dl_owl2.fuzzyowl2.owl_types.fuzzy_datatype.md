# Summary

An abstract base class that defines the structure for fuzzy datatypes characterized by lower and upper bounds within the FuzzyOWL2 framework.

## Description

Acting as a foundational component within the FuzzyOWL2 framework, this abstract base class represents fuzzy datatypes by encapsulating a range defined by a lower and an upper bound. The implementation manages two primary floating-point attributes that store the minimum and maximum values of the fuzzy interval, initialized to zero to ensure a consistent starting state. Accessor and mutator methods allow for the retrieval and modification of these boundaries, enabling concrete subclasses to define specific fuzzy logic behaviors based on these parameters. By abstracting the management of these bounds, the design facilitates the creation of derived classes that can focus on complex semantic definitions without re-implementing basic state management.
