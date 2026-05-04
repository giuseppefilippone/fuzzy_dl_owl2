# Summary

An abstract base class defines the structural foundation for fuzzy datatypes by managing a range characterized by lower and upper bounds.

## Description

Serving as a core component within the FuzzyOWL2 framework, the software establishes a standardized representation for fuzzy intervals through the encapsulation of minimum and maximum values. It initializes these boundary parameters to a default state, providing a flexible starting point for subclasses that implement specific fuzzy logic behaviors. Accessor and mutator methods allow for the direct manipulation of these numerical limits, enabling derived classes to define the shape and support of their fuzzy sets without enforcing strict validation on the input values. This design ensures a consistent interface for handling range-based data across the system, facilitating the extension of the framework to support various types of fuzzy numbers and logic operations.
