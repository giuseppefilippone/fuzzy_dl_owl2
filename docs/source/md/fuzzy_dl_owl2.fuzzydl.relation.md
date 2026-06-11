# Summary

Defines a data structure for representing fuzzy role assertions connecting two individuals through a specific relationship type constrained by a lower bound degree.

## Description

The implementation centers on a container that links a subject and an object individual via a named role while enforcing a minimum degree of membership. By storing references to the participating entities and the associated truth value, the software allows for the dynamic modification of relationship participants without altering the underlying role definition. Functionality includes the ability to generate human-readable representations of the assertion, both with and without the degree constraint, which aids in logging and debugging within fuzzy description logic systems. Furthermore, the design supports object cloning to ensure that independent copies of assertions can be created and manipulated without affecting the original instance.
