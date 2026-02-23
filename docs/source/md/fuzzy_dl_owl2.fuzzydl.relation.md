# Summary

Defines a data structure for representing fuzzy role assertions that link two individuals through a named relationship constrained by a lower bound degree.

## Description

The software models a specific type of logical assertion used in fuzzy description logics, where a relationship exists between a subject and an object entity. It encapsulates the properties of this connection, including the name of the role, the two distinct individuals involved, and a degree value that acts as a lower bound for the truth of the assertion. Design choices include allowing the modification of the participating individuals after instantiation, which provides flexibility for dynamic updates within a larger reasoning system. String representations are provided to visualize the relationship both with and without the degree constraint, facilitating debugging and logging. The implementation also supports cloning to create independent copies of the assertion, ensuring that modifications to a copy do not affect the original instance.
