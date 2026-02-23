# Summary

Defines a structural representation of a sigma-count concept within fuzzy description logic to evaluate constraints based on the quantity of role fillers.

## Description

A structural representation of a sigma-count concept within fuzzy description logic is provided to evaluate constraints based on the quantity of role fillers. The implementation models a condition where a target individual is considered satisfied if the number of related entities—connected via a specific role and conforming to a particular concept—falls within a fuzzy set determined by a collection of reference individuals. It encapsulates a variable for the count, the target individual, a list of reference individuals, a role name, and the concept being evaluated, storing these components to maintain the state required for subsequent processing. A deep copy mechanism is included to create independent instances of the object, while accessor methods expose the internal components for inspection. Standard Python magic methods are utilized to generate human-readable string representations and to compute hash values based on the object's string format, enabling use in collections like sets and dictionaries.
